import logging

import json
import pika
from auth.models import User
from pika.exceptions import AMQPConnectionError


class ProducerAuthorization:
    connection = None  # Атрибут класса для хранения соединения

    def __init__(self):
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue="GET_TOKEN_AND_USER", durable=True)
        except AMQPConnectionError as e:
            logging.error(f"Failed to connect to RabbitMQ: {e}")

    def send_user_object_and_token_to_services(self, token: str, user: User):
        if self.connection is None:
            logging.error("RabbitMQ connection is not established.")
            return  # Можно обработать ошибку, если соединение не установлено

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

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()

