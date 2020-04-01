# coding=utf-8
import os
import sys


def confusion_substitution():
    py_files_list = []
    file_path = sys.path[0]
    file_list = os.listdir(file_path)
    # 获取文件list
    for i in file_list:
        if i[:7] == "solopi_":
            files = os.path.join(file_path, i)
            py_files_path = os.path.join(files, i[:-4] + ".py")
            py_files_list.append(py_files_path)

    print(py_files_list)




if __name__ == '__main__':
    confusion_substitution()