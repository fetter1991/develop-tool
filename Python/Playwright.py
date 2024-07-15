from playwright.sync_api import sync_playwright

# 启动 playwright driver 进程
p = sync_playwright().start()

# 启动浏览器，返回 Browser 类型对象
browser = p.chromium.launch(channel="chrome", headless=False)

# 创建新页面，返回 Page 类型对象
page = browser.new_page()
page.goto("https://www.bilibili.com/read/cv23921171")

print(page.title())

# 输入通讯，点击查询。这是定位与操作，是自动化重点，后文详细讲解
# page.locator('#kw').fill('通讯')  # 输入通讯
# page.locator('#go').click()      # 点击查询
#
# # 打印所有搜索内容
# lcs = page.locator(".result-item").all()
# for lc in lcs:
#     print(lc.inner_text())

# 关闭浏览器
# browser.close()
# 关闭 playwright driver 进程
# p.stop()
