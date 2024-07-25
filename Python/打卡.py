import pyautogui
import time
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright


# playwright打开网页打卡
# def checkOutByPlaywright(check_out_seconds):
#     p = sync_playwright().start()
#
#     # 启动浏览器，返回 Browser 类型对象
#     browser = p.chromium.launch(headless=False)
#
#     # 创建新页面，返回 Page 类型对象
#     page = browser.new_page()
#     page.goto("https://om.tencent.com/attendances/check_out/22700602")
#     # 手动进行登录操作,check_out_seconds为多少秒后打卡
#     page.wait_for_timeout(check_out_seconds)
#
#     # 点击签出按钮
#     page.locator('#checkout_btn').click()  # 点击查询
#
#     page.wait_for_timeout(4000)
#     page.locator('.btn-primary').click()  # 点击查询
#
#     # 关闭浏览器
#     input('按下按钮Enter后才会执行，相当于一个断点')
#     browser.close()
#
#     # 关闭 playwright driver 进程
#     input('关闭 playwright driver 进程')
#     p.stop()


# 鼠标点击页面
def checkOutByMouse():
    # 1秒内将鼠标移动到(1470, 945)
    # pyautogui.moveTo(1470, 945, duration=1)

    print("程序开始执行打卡操作")
    # 改为自己需要的时间
    pyautogui.click(x=1000, y=470)
    time.sleep(1)
    pyautogui.click(x=370, y=470)
    time.sleep(1)
    # pyautogui.click(x=1470, y=945)

    print("打卡完成")


# 定时任务
def countdown(check_out_seconds):
    while check_out_seconds:
        # 将时间差转换为小时、分钟和秒
        hours, remainder = divmod(check_out_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        # print(timer, end="\r")
        print(f"程序将在: {timer}后进行打卡操作", end="\r")
        time.sleep(1)
        check_out_seconds -= 1
    print("打卡时间到！")
    checkOutByMouse()


# 签入时间
checkInStr = "2024-07-25 09:28"
# 解析时间字符串A到datetime对象
checkInTime = datetime.strptime(checkInStr, '%Y-%m-%d %H:%M')

# 在签入时间的基础上加上9个小时
checkOutTime = checkInTime + timedelta(hours=9)
print(f"签出时间: {checkOutTime.strftime('%Y-%m-%d %H:%M:%S')}")

# 获取当前时间
current_time = datetime.now()
# 计算签出时间与当前时间的时间差（以秒为单位）
time_difference = int((checkOutTime - current_time).total_seconds())
# 延迟几秒钟
time_difference = time_difference + 30

# 调用打卡主体程序
countdown(time_difference)
# 一分钟后再执行一次
countdown(60)
