#!/usr/bin/env python

import pika

# Configura os parametros de conexoes para se conectar com o
# rabbit-server na porta 5672 no host virtual / usando o
# nome de usuario "test" e senha "test".
credentials = pika.PlainCredentials('test', 'test')
parameters = pika.COnnectionParameters('192.168.1.4',
                                        5672,
                                        '/',
                                        credentials)

# Cria uma conexao bloqueadora
connection - pika.BlockingConnection(parameters)

# Cria um canal de comunicacao.
channel = connection.channel()

# Declara para qual fila estara enviando mensagens.
channel.queue_declare(queue='test_queue')

count = 0

# Envia mensagens
while count != 1000000:
  channel.basic_publish(exchange='',
                        routing_key='test_queue',
                        body='123456789012')
    count += 1
# Fecha conexao.
connection.close()
