# coding=utf-8
import csv
import os
import re


# 获取文件路径list
def get_file_path(v):
    folder = "C:/Users/cucumber/Desktop/Android " + str(v) + "性能数据"
    # folder = "C:/Users/10079/Desktop/Android " + str(v) + "性能数据"
    module_name = ["feed浏览", "feed播放_recording", "feed播放_video", "录制视频recording"]
    print("Android" + v + "性能数据")
    for i in module_name:
        file_path = os.path.join(folder, i)
        print(">>>" + i)
        print('{} {}'.format("峰值：", get_file_list(file_path)[:2]))
        print('{} {}'.format("均值：", get_file_list(file_path)[2:]))
        print("--------------------")


# 获取文件夹list
def get_file_list(file_path):
    memory = []
    cpu = []
    cpu_ave = []
    memory_ave = []
    # 获取当前路径下文件list
    file_list = os.listdir(file_path)
    files = []
    for i in range(len(file_list)):
        files.append(os.path.join(file_path, file_list[i]))
    for i in files:
        # 获取当前路径下文件list
        file_list = os.listdir(i)
        for j in file_list:
            if re.match("PSS内存", j):
                memory_file = os.path.join(i, j)
                memory.append(get_max(memory_file))
                memory_ave.append(get_single_strip_ave(memory_file))
            if re.match("应用进程-main", j):
                cpu_file = os.path.join(i, j)
                cpu.append(get_max(cpu_file))
                cpu_ave.append(get_single_strip_ave(cpu_file))

    return get_ave(cpu), get_ave(memory), get_ave(cpu_ave), get_ave(memory_ave)


# 读取csv数据
def get_max(files):
    # 打开csv文件
    with open(files, 'r') as csv_file:
        reader = csv.reader(csv_file)
        column1 = [row[1] for row in reader]
    # 获取最大值
    max_num = 0
    for i in column1[1:]:
        if float(i) > max_num:
            max_num = float(i)
    return max_num


# 获取单次数据平均值
def get_single_strip_ave(files):
    # 打开csv文件
    with open(files, 'r') as csv_file:
        reader = csv.reader(csv_file)
        column1 = [row[1] for row in reader]

    total_num = 0
    data_volume = 0
    for idx, i in enumerate(column1[1:]):
        total_num += float(i)
        data_volume = idx + 1
    single_strip_ave_num = total_num / data_volume
    return single_strip_ave_num


# 获取平均值
def get_ave(num_list):
    # 找出最大、最小值
    max_num = 0
    min_num = 999999
    for i in num_list:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    # 去除最大、最小后，计算平均值
    cnt_num = 0
    for i in num_list:
        if i == max_num or i == min_num:
            continue
        else:
            cnt_num += i
    ave_num = cnt_num / 3
    return '%.2f' % ave_num


if __name__ == '__main__':
    get_file_path("763")
