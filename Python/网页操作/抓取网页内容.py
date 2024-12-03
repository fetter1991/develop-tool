import requests
from bs4 import BeautifulSoup

# 目标URL
url = 'http://www.xqishuta.net/du/151/151513/53167134.html'

# 发送HTTP GET请求
response = requests.get(url)

def replace_multiple(text, replacements):
    # 创建一个新的字符串，用于存储替换结果
    # 从原始文本开始，然后依次进行替换
    result = text
    for old, new in replacements.items():
        result = result.replace(old, new)
    return result

# 检查请求是否成功
if response.status_code == 200:
    # 或者根据网页实际编码进行设置
    response.encoding = 'utf-8'

    # 获取网页内容
    page_content = response.text

    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(page_content, 'html.parser')

    # 指定要查找的id名称
    target_id = 'content1'  # 替换为你的目标id名称

    # 查找具有指定id的元素
    element = soup.find(id=target_id)

    # 要替换的字符串对（旧字符串: 新字符串）
    replacements = {
        "&nbsp;": " ",
        "<br>": "\t\r",
    }

    # 检查是否找到了元素
    if element:
        # 赋值文本内容并替换标签
        original_string = element.get_text()
        new_string = replace_multiple(original_string, replacements)
        print(new_string)  # strip=True用于去除文本前后的空白字符
    else:
        print(f'没有找到id为： "{target_id}" 的内容.')
else:
    print(f'抓取页面失败: {response.status_code}')

