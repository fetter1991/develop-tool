import redis

redisHandel = redis.Redis(host="127.0.0.1", port=6379, password="admin", db=1,
                          decode_responses=True)

print(redisHandel)
