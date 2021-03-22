#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Ping')

channel.basic_publish(exchange='', routing_key='Ping', body='Ping')
print(" [x] Sent 'Ping")
connection.close()