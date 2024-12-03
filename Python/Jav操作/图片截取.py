from PIL import Image

# 打开图片文件
img = Image.open('example.jpg')

# 定义要截取的区域，左上角为 (x1, y1)，右下角为 (x2, y2)
x1, y1, x2, y2 = 100, 100, 400, 400

# 截取指定区域的图片
cropped_img = img.crop((x1, y1, x2, y2))

# 保存截取后的图片到本地文件
cropped_img.save('cropped_example.jpg')
