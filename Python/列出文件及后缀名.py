import os
 
# 设置文件夹路径
folder_path = './1'
 
# 获取文件夹下所有文件和文件夹名称
filenames = os.listdir(folder_path)
 
# 打印所有文件名
for fileFullName in filenames:
    filename = os.path.splitext(fileFullName)[0]
    extensions = os.path.splitext(fileFullName)[1]
    print('文件名:'+filename+' 扩展名：'+extensions)
