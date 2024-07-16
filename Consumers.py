#本示例为消息消费者，场景（抽取消息出队）
import pika
 
credentials = pika.PlainCredentials("bohanbohan","Abc=123")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host = '192.168.11.12',
    port = 5672,
    virtual_host = '/',
    credentials = credentials))
channel = connection.channel()
# 声明队列
channel.queue_declare(queue='AiPictureHandleRequest')
 
def callback(ch, method, properties, body):
    print(f" [x] 收到消息： {body}")
 
# 接收消息并调用callback函数处理
channel.basic_consume(queue='AiPictureHandleRequest', on_message_callback=callback, auto_ack=True)
 
print(' [*] 阻塞等待消息中. 退出 CTRL+C')
channel.start_consuming()