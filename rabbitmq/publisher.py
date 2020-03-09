#!/usr/bin/env python3
import pika


def publisher(channel, i):
    channel.basic_publish(body='This is message # {}'.format(i), routing_key='foo', exchange='')


parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
connection = pika.BlockingConnection(parameters)
chan = connection.channel()
chan.queue_declare(queue='foo')

for i in range(10000000):
    publisher(chan, i)

