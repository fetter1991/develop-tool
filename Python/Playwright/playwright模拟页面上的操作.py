from playwright.sync_api import sync_playwright


def run(playwright):

    browser = playwright.chromium.launch(channel="chrome", headless=False)  # headless=False 允许我们看到一个实际的浏览器窗口
    # page = browser.new_page()

    # 创建 BrowserContext 对象
    context = browser.new_context()
    # 通过context 创建page
    page = context.new_page()

    # 改变页面大小
    screen_width, screen_height = 1920, 960
    page.set_viewport_size({'width': screen_width, 'height': screen_height})

    # 打开包含表格的页面
    page.goto('https://test-portal-learn.woa.com/training/mooc/home')  # 请替换为你的网页URL

    # 等待几秒钟，用来登录
    page.wait_for_timeout(5000)

    element = page.query_selector('#content')
    if element:
        print("继续下一步")
    else:
        print("需要登录")
        login_form = page.query_selector('.login_form')
        if login_form:
            page.fill('input[id="userNameInp"]', 'vincentyqwu')
            page.fill('input[id="passWordInp"]', '123')
            # 点击登录
            page.click('button[type="submit"]')

    print("鼠标悬浮")
    # 鼠标悬浮
    hover_select = ".my-mooc-btn"
    page.hover(hover_select)

    page.wait_for_timeout(1000)

    print("详情")
    # 详情
    more = ".top-content button"
    page.click(more)

    # 输出文本内容，可以用来校验是否定位成功
    # not_finish = ".group-form:nth-of-type(1) label:nth-of-type(3)"
    # cell_content = page.eval_on_selector(not_finish, 'element => element.innerText')
    # print(cell_content)

    print("未完成")
    # 未完成
    not_finish = ".group-form:nth-of-type(1) label:nth-of-type(3)"
    page.wait_for_selector(not_finish, timeout=2000)
    not_finish = ".group-form:nth-of-type(1) label:nth-of-type(3)"
    cell_content = page.eval_on_selector(not_finish, 'element => element.innerText')
    print(cell_content)
    page.click(not_finish)

    print("点击第一个元素打开新页面")
    # 点击第一个元素打开新页面
    course_list = ".content .course-item:nth-of-type(1)"
    page.wait_for_selector(course_list, timeout=2000)
    page.click(course_list)

    page.wait_for_timeout(2000)

    # pages属性是 所有窗口对应Page对象的列表
    new_page = context.pages[1]

    print("点击第一个元素打开新页面")
    # 新页面标题 校验是否打开成功
    # print(new_page.title())
    new_last_study = ".lastly-study-box button:nth-of-type(1)"
    new_page.wait_for_selector(new_last_study, timeout=2000)
    new_page.click(new_last_study)

    # 打开新页面等待2秒
    page.wait_for_timeout(2000)

    # 在新页面进行操作
    right_btn = ".right-btn button:nth-of-type(3)"
    new_page.wait_for_selector(right_btn, timeout=2000)
    new_page.click(new_last_study)
    page.wait_for_timeout(61000)

    # 等待几秒钟，关闭页面
    # page.wait_for_timeout(4000)
    input("按Enter关闭页面。。。")

    # 关闭浏览器
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
