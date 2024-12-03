import pyautogui
import random
import time

# 设置晃动的范围和频率
RANGE = 300  # 每次晃动的最大像素距离
INTERVAL = 0.01  # 每次晃动之间的时间间隔（秒）
DURATION = 5  # 总共晃动的时间（秒）

# 获取当前鼠标位置
current_mouse_x, current_mouse_y = pyautogui.position()

# 记录开始时间
start_time = time.time()

while time.time() - start_time < DURATION:
    # 生成随机的偏移量
    dx = random.uniform(-RANGE, RANGE)
    dy = random.uniform(-RANGE, RANGE)

    # 计算新的鼠标位置
    new_mouse_x = current_mouse_x + dx
    new_mouse_y = current_mouse_y + dy

    # 移动鼠标到新的位置
    pyautogui.moveTo(new_mouse_x, new_mouse_y, duration=0.01)

    # 更新当前鼠标位置
    current_mouse_x, current_mouse_y = new_mouse_x, new_mouse_y

    # 等待一段时间
    time.sleep(INTERVAL)
