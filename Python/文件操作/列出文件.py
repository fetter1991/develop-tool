import os

def list_files(directory):
    file_list = []
    
    def recursive_list_files(dir_path, level):
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            
            # 如果是文件夹，则递归遍历
            if os.path.isdir(item_path):
                file_list.append({'name': item, 'level': level, 'type': 'directory'})
                recursive_list_files(item_path, level + 1)
            # 如果是文件，则添加到文件列表
            elif os.path.isfile(item_path):
                file_list.append({'name': item, 'level': level, 'type': 'file'})
    
    recursive_list_files(directory, 0)
    return file_list

# 指定要遍历的文件夹路径
directory_path = '/JAV'

# 调用函数并获取文件列表
file_list = list_files(directory_path)

# 打印文件列表
for file_info in file_list:
    print(file_info)
    # print(f"{'  ' * file_info['level']}{'[D]' if file_info['type'] == 'directory' else '[F]'} {file_info['name']}")