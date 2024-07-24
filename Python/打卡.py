import pyautogui
import time
from playwright.sync_api import sync_playwright

def checkOutByMouse():
    print("程序开始执行")
    # 改为自己需要的时间
    time.sleep(15)
    pyautogui.click(x=1000, y=470)
    time.sleep(1)
    pyautogui.click(x=370, y=470)
    time.sleep(1)
    pyautogui.click(x=1470, y=945)

    # # 1秒内将鼠标移动到(100, 100)
    # pyautogui.moveTo(1000, 470, duration=1)
    # # 在当前鼠标位置点击
    # pyautogui.click()
    #
    # pyautogui.moveTo(370, 470, duration=1)
    # pyautogui.click()
    #
    # pyautogui.moveTo(1470, 945, duration=1)
    # pyautogui.click()
    print("打开完成")


def checkOutByPlaywright():
    p = sync_playwright().start()

    # 启动浏览器，返回 Browser 类型对象
    browser = p.chromium.launch(headless=False)

    # 创建新页面，返回 Page 类型对象
    page = browser.new_page()
    page.goto("https://om.tencent.com/attendances/check_out/22700602")
    # 打印网页标题栏

    page.wait_for_timeout(4000)

    # 输入通讯，点击查询。这是定位与操作，是自动化重点，后文详细讲解
    page.locator('#checkout_btn').click()  # 点击查询

    # TODO 获取打卡时间，计算后再等待
    page.wait_for_timeout(4000)
    page.locator('.btn-primary').click()  # 点击查询

    input('调用browser.close()')
    # 关闭浏览器
    browser.close()

    input('关闭 playwright driver 进程')
    # 关闭 playwright driver 进程
    p.stop()
