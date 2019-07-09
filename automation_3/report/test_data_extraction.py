# coding=utf-8
import os
import re


# 删除最大和最小值，计算平均值并返回结果
def filter(data):
    max_data = 0
    min_data = 99999999
    data_list = []
    for i in data:
        if int(i) > int(max_data):
            max_data = i
        if int(i) < int(min_data):
            min_data = i
    data.remove(max_data)
    data.remove(min_data)
    for i in data:
        data_list.append(int(i))
    data_sum = 0
    for i in data_list:
        data_sum += i
    average_result = [int(int(data_sum) / len(data_list))].__str__() + "  >>>  "
    return average_result, data_list


# 从报告中提取各项数据
def get_data(version="99.99.99", test_modular="default"):
    log_path = os.getcwd()
    log_list = os.listdir(log_path + "\\.logs")
    newest = 0
    for i in log_list:
        Suffix = os.path.splitext(i)[1]
        if Suffix == ".log":
            if "-logs-2019" in str(i):
                f = re.findall("\\d+", i)[0]
                if int(f) > int(newest):
                    newest = f

    with open(log_path + "\\.logs\\memoryinfo-logs-" + newest + ".log", encoding="utf-8", errors="ignore") as f:
        log_read = f.read()
    startMemory_list = re.findall("startMemory: " + "(\\d+)", log_read)
    endMemory_list = re.findall("endMemory: " + "(\\d+)", log_read)
    averageMemory_list = re.findall("averageMemory: " + "(\\d+)", log_read)
    maxMemory_list = re.findall("maxMemory: " + "(\\d+)", log_read)
    maxFluctuation_list = re.findall("maxFluctuation: " + "(\\d+)", log_read)
    if len(startMemory_list) >= 12:
        log_result = True
        print("测试数据已校验，过滤后数据如下：")
    else:
        log_result = False
        print("还需要 %s 份测试数据" % (12 - len(startMemory_list)))
    line = "------------------------------"
    start = "startMemory：%s%s" % filter(startMemory_list)
    end = "endMemory：%s%s" % filter(endMemory_list)
    ave = "averageMemory：%s%s" % filter(averageMemory_list)
    max = "maxMemory：%s%s" % filter(maxMemory_list)
    fct = "maxFluctuation：%s%s" % filter(maxFluctuation_list)

    print(line)
    print(start)
    print(end)
    print(ave)
    print(max)
    print(fct)
    print(line)

    if log_result:
        with open(log_path + '\\log_result\\' + version + "_" + 'result.log',
                  'a+', encoding='utf-8') as f:
            f.write("%s 版本   %s 模块   内存占用数据%s" % (version, test_modular, "\n"))
            f.write(line+"\n")
            f.write(start+"\n")
            f.write(end+"\n")
            f.write(ave+"\n")
            f.write(max+"\n")
            f.write(fct+"\n")
            f.write(line+"\n\n")
            return True


if __name__ == '__main__':
    # 记录报告
    version = "7.4.7"
    test_modular = "live"
    if get_data(version, test_modular):
        print("记录完成")
