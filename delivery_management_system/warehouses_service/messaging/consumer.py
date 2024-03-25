import json
import pika


class ConsumerAuthorization:
    def __init__(self):
        self.json_data = None
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="GET_TOKEN_AND_USER", durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def receive_user_obj_and_token_from_auth_service(self):
        def callback(ch, method, properties, body):
            message_str = body.decode()
            self.json_data = json.loads(message_str)
            print(f" [x] Received {self.json_data['token']} and {self.json_data['user']}")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='GET_TOKEN_AND_USER', on_message_callback=callback)
        return self.json_data["token"], self.json_data["user"]

    def __enter__(self):
        return self

    def __exit__(self):
        print("EXIT ConsumerAuthorization")
