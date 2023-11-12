import urllib.request
import os


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#     "Connection": "keep-alive",
#     "Accept": "text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.8"}


def download_image(url, file_name):
    try:
        # 下载图片
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, file_name)
        print("图片已成功下载！")
    except Exception as e:
        print("下载失败：", e)

if __name__ == "__main__":
    url = input("请输入图片链接：")
    file_name = input("请输入保存文件名：")

    # 检查文件名是否存在，如果不存在则添加扩展名
    if not os.path.splitext(file_name)[1]:
        file_name += os.path.splitext(url)[1]

    download_image(url, file_name)
