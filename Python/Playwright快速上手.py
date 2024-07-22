from playwright.sync_api import sync_playwright

# https://www.byhy.net/etc/playwright/01/
input('1、启动playwright driver进程')
# 启动 playwright driver 进程
p = sync_playwright().start()

input('2、启动浏览器，返回 Browser 类型对象')
# 启动浏览器，返回 Browser 类型对象
browser = p.chromium.launch(headless=False)

# 创建新页面，返回 Page 类型对象
page = browser.new_page()
page.goto("https://www.byhy.net/_files/stock1.html")
# 打印网页标题栏
print(page.title())

# 输入通讯，点击查询。这是定位与操作，是自动化重点，后文详细讲解
page.locator('#kw').fill('通讯')  # 输入通讯
page.locator('#go').click()      # 点击查询

# 打印所有搜索内容
lcs = page.locator(".result-item").all()
for lc in lcs:
    print(lc.inner_text())

input('3、调用browser.close()')
# 关闭浏览器
browser.close()

input('4、关闭 playwright driver 进程')
# 关闭 playwright driver 进程
p.stop()
