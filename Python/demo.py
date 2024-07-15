from playwright.sync_api import sync_playwright
import os
import requests
from io import BytesIO
from pathlib import Path

wdPath = "./1/"
baseUrl = "https://www.bilibili.com/read/"

# filenames = os.listdir(wdPath)

# 打印所有文件名
# for fileFullName in filenames:
#     filename = os.path.splitext(fileFullName)[0]
#     extensions = os.path.splitext(fileFullName)[1]
#     # print('文件名:' + filename + ' 扩展名：' + extensions)
#
#     pageUrl = baseUrl + filename
#     page.goto(pageUrl)


def createNewFolder(path):
    folder_path = os.path.join(wdPath, path)
    os.mkdir(folder_path)
    # folder_path.mkdir(parents=True, exist_ok=True)



p = sync_playwright().start()
browser = p.chromium.launch(headless=False,  executable_path='c:\Program Files\Google\Chrome\Application\chrome.exe')

# 创建 BrowserContext对象
context = browser.new_context()
# 启动跟踪功能
context.tracing.start(snapshots=True, sources=True, screenshots=True)

page = context.new_page()
page.goto("https://www.bilibili.com/read/cv23921171")

page.wait_for_timeout(2000)

# # 假设我们要找的div的class是"target-div"
# # 注意：这里的选择器可能需要根据实际的HTML结构进行调整
# div_selector = '.article-container'
# div_handle = page.query_selector(div_selector)
#
# # 获取div下的所有p标签
# p_handles = div_handle.query_selector_all('.up-name')
# third_p_text = p_handles[0].text_content()
# actor = third_p_text.strip()
# createNewFolder("【"+actor+"】")

# 获取div下的所有img标签，并找到class为"img"的图片
# img_handles = div_handle.query_selector_all('img.bili-avatar-face')
# for img_handle in img_handles:
#     img_src = img_handle.get_attribute('src')
#     print(f"找到的图片地址: {img_src}")

page.goto("https://www.bilibili.com/read/cv23921172")

input('3....')
browser.close()
