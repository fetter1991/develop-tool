from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # headless=False 允许看到浏览器界面
    page = browser.new_page()

    # 打开百度网页
    page.goto('https://www.baidu.com')

    # 在搜索框中输入查询词
    page.fill('input[name="wd"]', 'Python Playwright')

    # 点击搜索按钮或按下 Enter 键
    # 方法1: 点击搜索按钮(元素类型)
    # page.click('input[type="submit"]')

    # 方法2: 点击搜索按钮(元素Id)
    page.click('input#su')

    # 方法3: 模拟按下 Enter 键（更通用，因为不需要找到具体的搜索按钮）
    # page.press('input[name="wd"]', 'Enter')

    # 等待搜索结果加载（可选，但通常是个好习惯）
    # page.wait_for_timeout(3000)  # 等待3秒

    input('按Enter键关闭页面....')

    # 打印页面标题或搜索结果（这里只是打印页面标题作为示例）
    # print(page.title())

    # 关闭浏览器
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
