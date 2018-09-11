from utils import fetchRedis

import time

redis = fetchRedis()
redis.set('test', 'sdsd', ex=3)

time.sleep(2)
print(redis.get('test'))