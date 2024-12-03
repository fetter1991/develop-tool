import sched
import time

# 创建调度器对象
scheduler = sched.scheduler(time.time, time.sleep)

# 定义一个函数，作为定时执行的任务
def your_function():
    # 执行你的代码
    print("循环")
    pass

# 设置定时任务，每5秒执行一次
scheduler.enter(5, 1, your_function, ())

# 启动调度器
scheduler.run()