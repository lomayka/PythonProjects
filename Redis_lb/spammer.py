from rq import Queue
import redis
import temp
import time
from message import Message
import sys

redis_conn = redis.StrictRedis(db=0, charset='utf-8', decode_responses=True)
ps = redis_conn.pubsub()

q = Queue(name='test_queue', connection=redis_conn)

import temp

for i in range(100):
    q.enqueue(temp.check_spam, Message('1', '2', '3', 'created'))