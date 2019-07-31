# coding=utf-8
import os
import re


# 从txt文本批量提取UID/room_id/sm_id，需要传文件名、样本示例
def get_number(file_name, sample):
    path = os.path.abspath(file_name)
    f = open(path, "r", encoding='gbk', errors='ignore')
    num = re.findall("\\d+", sample)[0]
    front = re.findall("(.*)" + num, sample)[0]
    after = re.findall(num + "(.*)", sample)[0]
    try:
        notepad = f.read()
        id_list = re.findall(front + r'(.+?)' + after, notepad)
    finally:
        f.close()
    return id_list


if __name__ == '__main__':
    print(get_number(file_name="test.txt", sample='"sm":{"sm_id":"249746734","user_id":"'))


