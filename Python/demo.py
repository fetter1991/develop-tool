import requests
from bs4 import BeautifulSoup
import time

# while True:
url = 'https://zhiyan.woa.com/qci/8767/pipeline/#/pipeline/list?pipelineType=favorite&ordering=-id&page=1&pageSize=20&disabled=false&currentTag=&keyword=&admin_filter=&app_id_filter=&creator_filter='
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
# news = soup.find_all('div', class_='san-card')
print(soup)
# for new in news:
#     print(new.text)
# time.sleep(60)
