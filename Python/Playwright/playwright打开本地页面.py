from playwright.sync_api import sync_playwright
import time
import os

current_directory = os.getcwd()
file = "../index.html"
full_path = os.path.join(current_directory, file)

def run():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)  # headless=False 以显示浏览器界面
        page = browser.new_page()
        page.goto(full_path)  # 指向你的本地HTML文件

        element_id = "text-to-change"
        text_to_type = "为了优化代码并实现仅逐字输出的效果，我们可以继续使用Playwright与Python结合，但这次我们将专注于确保JavaScript代码在浏览器中正确执行，并且Python代码主要负责启动浏览器和页面。"
        speed = 60

        page.evaluate(f"""  
            function() {{  
                // 这里假设typeText函数已经在页面中定义好了
                // 直接调用它，并传入从Python传递过来的参数
                typeText('{element_id}', '{text_to_type}', '{speed}');  
            }}  
        """)

        # 等待足够长的时间以观察逐字输出的效果
        # 注意：这里使用time.sleep是同步API中的简单方法，但更好的做法是使用Playwright的等待机制
        time.sleep(len(text_to_type) * 0.1 + 1)  # 假设每个字符之间间隔100ms，并额外等待1秒
        browser.close()


if __name__ == "__main__":
    run()
