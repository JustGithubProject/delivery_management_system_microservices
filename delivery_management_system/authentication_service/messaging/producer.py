import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Creating a queue
channel.queue_declare(queue="TEMP_NAME")

# Close the connection
connection.close()