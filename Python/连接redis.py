import redis

r = redis.Redis(host="127.0.0.1", port=6379, password="admin", db=1, decode_responses=True)

# print(redisHandel)

# 提示用户输入key值
key_to_delete = input("请输入要删除的key值: ")

# 尝试删除key
try:
    # 使用r.delete()方法删除key，并获取返回的结果（成功删除的key数量）
    deleted_count = r.delete(key_to_delete)

    # 根据删除结果输出信息
    if deleted_count == 1:
        print(f"Key '{key_to_delete}' 已成功删除。")
    elif deleted_count == 0:
        print(f"Key '{key_to_delete}' 不存在或未删除任何key。")
    else:
        # 在正常情况下，r.delete()应该只返回0或1，但这里可以处理意外情况
        print(f"操作结果不确定，已删除{deleted_count}个key（这可能是一个错误的情况）。")

except redis.exceptions.RedisError as e:
    # 捕获并处理Redis连接或命令执行时可能发生的异常
    print(f"Redis错误: {e}")

# 验证key是否已被删除（可选）
if r.exists(key_to_delete):
    print(f"Key '{key_to_delete}' 仍然存在。")
else:
    print(f"Key '{key_to_delete}' 已确认被删除。")