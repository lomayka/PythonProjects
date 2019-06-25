import redis 

redis = redis.StrictRedis(db=0)
 

for i in range(10):
    redis.rpush('testList2', f'message{i}')
# redis.lpush('testList', 'message')