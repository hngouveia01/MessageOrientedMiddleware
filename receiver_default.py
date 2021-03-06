#!/usr/bin/env python

import pika

# Configura os parametros de conexao para se conectar com o
# rabbit-server na porta 5672 no host virtual / usando o
# nome de usuario "test" e senha "test".
credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('192.168.1.4',
                                       5672,
                                       '/',
                                       credentials)

# Cria conexao bloqueadora.
connection = pika.BlockingConnection(parameters)

#Estabelece canal de comunicacao
channel = connection.channel()

# Declara em qual fila estara esperando por mensagens.
channel.queue_declare(queue='test_queue')

# Ao receber uma mensagem, envia um ack (um aviso de recebimento)
# para o servidor rabbitmq.
def callback(ch, method, properties, body):
  ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='test_queue',
                      no_ack=False) #agora envia recebimento
print ' [*] waiting for messages. To exit press CTLR+C'

# Comeca a consumir as mensagens da fila.
channel.start_consuming()
