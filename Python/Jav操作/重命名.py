import os
import shutil

def rename_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        str = root
        # print(str)
        findStr = "】"
        index = str.find(findStr)
        # print(index)
        if index > 0 :
            code = str[index+1:]
        
        for file in files:
            # print(file)
            if file.endswith(".mp4"):
                mp4_file_name = os.path.splitext(file)[0]
                
            if file.endswith(".jpg") and "-fanart" in file:
                if not code in file:
                    new_name = mp4_file_name + "-fanart.jpg"
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_name)

                    shutil.move(old_path, new_path)

            if file.endswith(".jpg") and "-poster" in file:
                if not code in file:
                    new_name = mp4_file_name + "-poster.jpg"
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_name)

                    shutil.move(old_path, new_path)    

# 使用示例
rename_files("./JAV")