from rq import Queue
import redis
import temp
import time
from message import Message
import sys
import config


redis_conn = redis.StrictRedis(db=0, charset='utf-8', decode_responses=True)
ps = redis_conn.pubsub()

q = Queue(name='test_queue', connection=redis_conn)

def print_menu(login):
    if login == 'admin':
        ps.subscribe(config.LOG_CHANNEL)
        while True:
            mes = ps.get_message()
            if mes:
                print(mes['data'])
    else:
        redis_conn.publish(config.LOG_CHANNEL, f'{login} logined')
        print('1. send message')
        print('2. check inbox')
        print('3. exit')
        try:
            operation = str(input('operation code: '))
            operations[operation](login)
        except Exception as e:
            print(e)

def send_message(login):
    reciever = input("Reciever: ")
    text = input("Text: ")
    message = Message(login, reciever, text)
    message.status = 'queueing'
    job = q.enqueue(temp.check_spam, message)
    print('\nyour message will be processed soon')        
    input('\npress any key\n')
    print_menu(login)

def check_inbox(login):
    for item in redis_conn.lrange(login, 0, -1):
        print(item)
    input('\npress any key\n')
    print_menu(login)

def exit_prog(login):
    redis_conn.publish(config.LOG_CHANNEL, f'{login} exited')
    sys.exit(1)


def spam(login):
    for i in range(25):
        message = Message(login, 'reciever', f'text{i}')
        q.enqueue(temp.check_spam, message)

operations = {
    '1': send_message,
    '2': check_inbox,
    '3': exit_prog,
    '4': spam
}


print_menu(input('Enter your login: '))