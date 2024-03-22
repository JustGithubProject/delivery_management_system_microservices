import json
import pika
from authentication_service.auth.models import User


class ProducerAuthorization:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="GET_TOKEN_AND_USER", durable=True)

    def send_user_object_and_token_to_services(self, token: str, user: User):
        decoded_token = token.encode()
        data = {
            "token": decoded_token,
            "user": user
        }
        message_body = json.dumps(data)
        message_bytes = message_body.encode()

        self.channel.basic_publish(
            exchange='',
            routing_key="GET_TOKEN_AND_USER",
            body=message_bytes,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )
        print(f"[x] Sent: {decoded_token} and {user}")

    def __enter__(self):
        return self

    def __exit__(self):
        self.connection.close()


