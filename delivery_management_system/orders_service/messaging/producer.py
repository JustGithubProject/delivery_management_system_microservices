import pika
import json

from orders_service.order.models import (
    Order
)


class ProducerOrderToDeliveryService:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="GET_ORDER", durable=True)

    def send_order_object(self, order: Order):
        data = {
            "order": order
        }
        message_body = json.dumps(data)
        message_bytes = message_body.encode()

        self.channel.basic_publish(
            exchange='',
            routing_key="GET_ORDER",
            body=message_bytes,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )

    def __enter__(self):
        return self

    def __exit__(self):
        self.connection.close()
