from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # headless=False 允许我们看到一个实际的浏览器窗口
    page = browser.new_page()

    # 打开包含表格的页面
    # page.goto('https://om.tencent.com/attendances/check_out/22700602')  # 请替换为你的网页URL
    page.goto('https://www.baidu.com/s?wd=%E5%BC%80%E5%B0%81%E5%9F%8E%E5%A2%99%E5%9D%8D%E5%A1%8C%EF%BC%9F%E7%B3%BB%E8%B0%A3%E8%A8%80&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1')  # 请替换为你的网页URL

    # 等待几秒钟，用来手动登录
    page.wait_for_timeout(2000)

    # 定位到第一个类名为page的tr元素的第二个单元格
    # 注意：CSS选择器中的nth-child是从1开始计数的，并且这里假设单元格是<td>元素
    # 如果单元格是<th>，则将下面的'td'替换为'th'

    # box > tbody > tr.page:first-of-type td:nth-child(2)

    # selector = '.rs-label_ihUhK'
    selector = '.rs-col_8Qlx-:nth-of-type(2)'

    page.wait_for_selector(selector, timeout=2000)

    cell_content = page.eval_on_selector(selector, 'element => element.innerText')

    # 获取单元格的文本内容
    # cell_content = page.inner_text(selector)

    # 打印单元格的内容
    print(cell_content)

    # 等待几秒钟，关闭页面
    # page.wait_for_timeout(4000)

    input("按Enter关闭页面。。。")

    # 关闭浏览器
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
