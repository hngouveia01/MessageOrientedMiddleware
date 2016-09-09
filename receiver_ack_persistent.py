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
channel.queue_declare(queue='test_queue', durable=True)

# Ao receber uma mensagem, envia um ack (aviso de recebimento)
# para o servidor rabbitmq.
def callback(ch, method, properties, body):
  ch.basic_ack(delivery_tag = method.delivery_tag)

# Funcao que sera chamada quando uma mensagem for recebida
channel.basic_consume(callback,
                      queue='test_queue')
print ' [*] waiting for messages. To exit press CTRL+C'

# Comeca a consumir as mensagens da fila.
channel.start_consumig()
