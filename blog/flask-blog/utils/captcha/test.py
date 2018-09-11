
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('key','this is key')
print(r.get('image_code'))