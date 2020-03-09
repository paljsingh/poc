#!/usr/bin/env python3
import pika


def consumer(channel, connection):
    channel.basic_consume('foo', on_message_callback, auto_ack=True)
    channel.start_consuming()
    connection.close()


def on_message_callback(channel, method, properties, body):
    print(body)


parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
connection = pika.BlockingConnection(parameters)
chan = connection.channel()
chan.queue_declare(queue='foo')
consumer(chan, connection)