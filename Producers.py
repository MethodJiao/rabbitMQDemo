#本示例为消息生产者，场景（消息入队）
import pika
 
#认证信息
credentials = pika.PlainCredentials("bohanbohan","Abc=123")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host = '192.168.11.12',
    port = 5672,
    virtual_host = '/',
    credentials = credentials))
 
channel = connection.channel()
 
# 创建一个队列
channel.queue_declare(queue='AiPictureHandleRequest')
 
# 发送数据
channel.basic_publish(exchange='',
                      routing_key='AiPictureHandleRequest', # 消息队列名称
                      body='hello!') # 发送的数据
print(" [x] 发送消息到消息队列")
 
connection.close()