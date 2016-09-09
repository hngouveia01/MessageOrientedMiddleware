# MessageOrientedMiddleware
Avaliação de performance de um broker de mensagens utilizando Raspberry Pi

Segundo Coulouris e et al (2013, p. 52), um sistema distribuído é
aquele no qual os componentes localizados em computadores interligados em rede se
comunicam e coordenam suas ações por intermédio de mensagens. Um exemplo de
sistema distribuído pode ser a computação ubíqua: ela é a mesclagem da computação
móvel com a computação pervasiva. Em 2013 foi criado o Raspberry PI, um dispositivo
que pode ser considerado ubíquo (tanto móvel quanto pervasivo). Assumindo que o
Raspberry Pi esteja disposto num sistema distribuído, a comunicação dele com os
demais componentes do mesmo pode ser realizada através de um Broker de
mensagem, também conhecido como Middleware Orientado a Mensagem (MOM).
O desempenho de um MOM depende de sua eficiência, da rede em
que se encontra e das configurações do sistema. Um exemplo de um MOM é o
RabbitMQ que é um broker de mensagens multiplataforma que se adapta desde
ambientes de potentes servidores a computadores de placa única, como o Raspberry
Pi.
Com o advento da internet das coisas, o uso de equipamentos
ubíquos, como o Raspberry PI, se tornará indispensável para coleta e envio de
informações em tempo real. Esses dispositivos, dependendo do contexto, poderão
coletar milhares de informações em um curto período de tempo e, por conseguinte,
estas serão enviadas por meio de um broker de mensagens, como o RabbitMQ, para
uma base de dados.
Visto que informações em grande escala podem ser coletadas em
um curto período de tempo, pode­se afirmar que para o envio das mesmas o
desempenho é algo essencial para a realização do processo. Por ser um computador
de placa única, o Raspberry Pi possui recursos limitados, portanto o desempenho pode
não ser ideal.
A fim de avaliar a performance do RabbitMQ em situações simples de
envio e recebimento em um computador de placa única, o Raspberry Pi, verificou­se as
diferentes formas de acusar recebimento, máximo consumo e persistência das
mensagens. Baseado nesta avaliação, propôs­se a configuração que oferecerá a maior
velocidade de mensagens por segundo em situação de máximo consumo.
