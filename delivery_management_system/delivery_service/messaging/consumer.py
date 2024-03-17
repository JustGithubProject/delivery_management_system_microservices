import pika


class ConsumerAuthorization:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="TEMP_NAME", durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')

    def receive_user_token_from_auth_service(self):
        def callback(ch, method, properties, body):
            token = body.decode()
            print(f" [x] Received {token}")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='TEMP_NAME', on_message_callback=callback)

    def __enter__(self):
        self.channel.start_consuming()
        return self

    def __exit__(self):
        print("EXIT")