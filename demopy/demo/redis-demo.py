import redis

host = 'localhost'
port = 6379
r = redis.Redis(host=host, port=port)
print(r.keys('*'))
