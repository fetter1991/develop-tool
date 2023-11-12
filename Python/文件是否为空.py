import os

def count_files(path):
    # 初始化字典，用于记录各种文件类型的数量
    file_counts = {}

    # 遍历当前目录下所有文件和文件夹
    for root, dirs, files in os.walk(path):
        # print(len(os.listdir(root)))
        # print(len(os.listdir(dirs)))
        if len(os.listdir(root)) == 0:
            print(root)
        for file in files:
            # 获取文件扩展名
            ext = os.path.splitext(file)[-1].lower()

            # 如果文件没有扩展名，则将其视为无类型文件
            if not ext:
                ext = "unknown"

            # 将文件类型添加到字典中
            if ext in file_counts:
                file_counts[ext] += 1
            else:
                file_counts[ext] = 1

        # 输出当前文件夹下不同文件类型的数量
        print(f"Folder: {root}")
        for ext, count in file_counts.items():
            print(f"\t{ext}: {count}")

        # 清空字典，准备遍历下一个文件夹
        file_counts.clear()

if __name__ == "__main__":
    count_files("./1")