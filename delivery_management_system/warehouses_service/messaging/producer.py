import pika
import json

from warehouses_service.warehouse.models import (
    Product
)


class ProducerProductToOrderService:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="GET_PRODUCT", durable=True)

    def send_product_object(self, product: Product):
        data = {
            "product": product
        }
        message_body = json.dumps(data)
        message_bytes = message_body.encode()

        self.channel.basic_publish(
            exchange='',
            routing_key="GET_PRODUCT",
            body=message_bytes,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )

    def __enter__(self):
        return self

    def __exit__(self):
        self.connection.close()

