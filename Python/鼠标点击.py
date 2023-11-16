from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com/")

# 定位搜索框并输入关键词
search_box = driver.find_element_by_xpath("//input[@id='kw']")
search_box.send_keys("Python")

# 模拟回车键
search_box.send_keys(Keys.ENTER)

# 等待页面加载完成
driver.implicitly_wait(10)

# 获取搜索结果
results = driver.find_elements_by_xpath("//div[@class='result c-container ']")

# 输出搜索结果标题和URL
for result in results:
    title = result.find_element_by_xpath(".//h3/a")
    url = result.find_element_by_xpath(".//h3/a/@href")
    print("标题：", title.text)
    print("URL：", url.get_attribute("href"))
    print()
