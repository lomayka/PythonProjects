import redis
import time
from message import Message
import random


def check_spam(message: Message):
    redis_conn = redis.StrictRedis(db=0, encoding='utf-8', decode_responses=True)
    message.status = 'checking'
    print(message)
    time.sleep(random.randint(0, 3))
    r = bool(random.getrandbits(1))
    if r:
        redis_conn.publish('LOG', f'got spam from {message.sender}')
    else:
        message.status = 'sent'
        redis_conn.rpush(message.reciever, f'{message.sender}: {message.text}')
    return r
