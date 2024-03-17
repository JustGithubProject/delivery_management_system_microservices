import pika


class ProducerAuthorization:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="TEMP_NAME", durable=True)

    def send_user_token_to_services(self, token: str):
        message = token.encode()
        self.channel.basic_publish(
            exchange='',
            routing_key="TEMP_NAME",
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )
        print(f"[x] Sent: {message}")

    def __enter__(self):
        return self

    def __exit__(self):
        self.connection.close()


