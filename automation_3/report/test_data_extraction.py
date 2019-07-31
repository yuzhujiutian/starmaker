# coding=utf-8
import datetime
import os
import re


# 删除最大和最小值，计算平均值并返回结果
def filter(data):
    print(data)
    max_data = 0
    min_data = 99999999
    data_list = []
    # print(len(data))
    if len(data) >= 5:
        for i in data:
            if int(float(i)) > int(max_data):
                max_data = i
            if int(float(i)) < int(min_data):
                min_data = i
        data.remove(max_data)
        data.remove(min_data)
    for i in data:
        data_list.append(int(float(i)))
    data_sum = 0
    for i in data_list:
        data_sum += i
    average_result = [int(int(data_sum) / len(data_list))].__str__() + "  >>>  "
    return average_result, data_list


# 从报告中提取各项数据
def get_data(version="99.99.99", test_modular="default"):
    log_result = True
    log_path = os.getcwd()
    log_list = os.listdir(log_path + "\\.logs")
    cpu_newest = 0
    mem_newest = 0
    for i in log_list:
        Suffix = os.path.splitext(i)[1]
        if Suffix == ".log":
            if "cpuinfo-logs-2019" in str(i):
                f = re.findall("\\d+", i)[0]
                if int(f) > int(cpu_newest):
                    cpu_newest = f

            if "memoryinfo-logs-2019" in str(i):
                f = re.findall("\\d+", i)[0]
                if int(f) > int(mem_newest):
                    mem_newest = f
    # 读取文件
    if cpu_newest:
        with open(log_path + "\\.logs\\cpuinfo-logs-" + str(cpu_newest) + ".log",
                  encoding="utf-8", errors="ignore") as cpu_f:
            cpu_f_log_read = cpu_f.read()
    else:
        cpu_f_log_read = False

    if mem_newest:
        with open(log_path + "\\.logs\\memoryinfo-logs-" + str(mem_newest) + ".log",
                  encoding="utf-8", errors="ignore") as mem_f:
            mem_f_log_read = mem_f.read()
    else:
        mem_f_log_read = False

    # if cpu_f_log_read and mem_f_log_read:
    #     pass
    # else:
    #     log_result = False

    # 处理内存占用数据
    if mem_f_log_read:
        duration_list = re.findall("duration：" + "(\\d+)", mem_f_log_read)
        frequency_list = re.findall("frequency：" + "(\\d+)", mem_f_log_read)
        startMemory_list = re.findall("startMemory: " + "(\\d+)", mem_f_log_read)
        endMemory_list = re.findall("endMemory: " + "(\\d+)", mem_f_log_read)
        averageMemory_list = re.findall("averageMemory: " + "(\\d+)", mem_f_log_read)
        maxMemory_list = re.findall("maxMemory: " + "(\\d+)", mem_f_log_read)
        maxFluctuation_list = re.findall("maxFluctuation: " + "(\\d+)", mem_f_log_read)

        if len(startMemory_list) >= 5:
            print("测试数据已校验，过滤后数据如下(memory有效数据共%s条)：" % len(startMemory_list))
            # 将已统计过的数据rename
            try:
                old_file = os.path.join(log_path + "\\.logs",
                                        "memoryinfo-logs-" + mem_newest + ".log")
                new_file = os.path.join(log_path + "\\.logs",
                                        "Used-" + version + "_" + test_modular + "-logs-"
                                        + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".log")
                os.rename(old_file, new_file)
            except:
                pass
        else:
            log_result = False
            print("还需要 %s 份测试数据" % (5 - len(startMemory_list)))
        duration = "duration：%s%s" % filter(duration_list)
        frequency = "frequency：%s%s" % filter(frequency_list)
        line = "------------------------------"
        start = "startMemory：%s%s" % filter(startMemory_list)
        end = "endMemory：%s%s" % filter(endMemory_list)
        ave = "averageMemory：%s%s" % filter(averageMemory_list)
        max_value = "maxMemory：%s%s" % filter(maxMemory_list)
        max_fct = "maxFluctuation：%s%s" % filter(maxFluctuation_list)

        print(line)
        print(start)
        print(end)
        print(ave)
        print(max_value)
        print(max_fct)
        print(line)

        if log_result:
            with open(log_path + '\\log_result\\' + version + "_" + 'result.log',
                      'a+', encoding='utf-8') as f:
                f.write("%s 版本   %s 模块   内存占用数据%s" % (version, test_modular, "\n"))
                f.write(duration+"\n")
                f.write(frequency+"\n")
                f.write(line+"\n")
                f.write(start+"\n")
                f.write(end+"\n")
                f.write(ave+"\n")
                f.write(max_value+"\n")
                f.write(max_fct+"\n")
                f.write(line+"\n\n\n")

    # 处理CPU占用数据
    if cpu_f_log_read:
        duration_list = re.findall("duration：" + "(\\d+)", cpu_f_log_read)
        frequency_list = re.findall("frequency：" + "(\\d+)", cpu_f_log_read)

        user_startCPU_list = re.findall("user_startCPU: " + "(\\d+)", cpu_f_log_read)
        user_endCPU_list = re.findall("user_endCPU: " + "(\\d+)", cpu_f_log_read)
        average_userCPU_list = re.findall("average_userCPU: " + "(\\d+)", cpu_f_log_read)
        user_maxCPU_list = re.findall("user_maxCPU: " + "(\\d+)", cpu_f_log_read)

        kernel_startCPU_list = re.findall("kernel_startCPU: " + "(\\d+)", cpu_f_log_read)
        kernel_endCPU_list = re.findall("kernel_endCPU: " + "(\\d+)", cpu_f_log_read)
        average_kernelCPU_list = re.findall("average_kernelCPU: " + "(\\d+)", cpu_f_log_read)
        kernel_maxCPU_list = re.findall("kernel_maxCPU: " + "(\\d+)", cpu_f_log_read)

        if len(user_startCPU_list) >= 1:
            print("测试数据已校验，过滤后数据如下(cpu有效数据共%s条)：" % len(user_startCPU_list))
            # 将已统计过的数据rename
            try:
                old_file = os.path.join(log_path + "\\.logs",
                                        "cpuinfo-logs-" + cpu_newest + ".log")
                new_file = os.path.join(log_path + "\\.logs",
                                        "Used-" + version + "_" + test_modular + "-logs-"
                                        + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".log")
                os.rename(old_file, new_file)
            except:
                pass
        else:
            log_result = False
            print("还需要 %s 份测试数据" % (5 - len(user_startCPU_list)))
        duration = "duration：%s%s" % filter(duration_list)
        frequency = "frequency：%s%s" % filter(frequency_list)
        line = "------------------------------"
        line_min = "----------"
        user_start = "user_startCPU：%s%s" % filter(user_startCPU_list)
        user_end = "user_endCPU：%s%s" % filter(user_endCPU_list)
        user_ave = "average_userCPU：%s%s" % filter(average_userCPU_list)
        user_max = "user_maxCPU：%s%s" % filter(user_maxCPU_list)

        kernel_start = "kernel_startCPU：%s%s" % filter(kernel_startCPU_list)
        kernel_end = "kernel_endCPU：%s%s" % filter(kernel_endCPU_list)
        kernel_ave = "average_kernelCPU：%s%s" % filter(average_kernelCPU_list)
        kernel_max = "kernel_maxCPU：%s%s" % filter(kernel_maxCPU_list)

        print(line)
        print(user_start)
        print(user_end)
        print(user_ave)
        print(user_max)
        print(line_min)
        print(kernel_start)
        print(kernel_end)
        print(kernel_ave)
        print(kernel_max)
        print(line)

        if log_result:
            with open(log_path + '\\log_result\\' + version + "_" + 'result.log',
                      'a+', encoding='utf-8') as f:
                f.write("%s 版本   %s 模块   CPU占用数据%s" % (version, test_modular, "\n"))
                f.write(duration + "\n")
                f.write(frequency + "\n")
                f.write(line + "\n")
                f.write(user_start + "\n")
                f.write(user_end + "\n")
                f.write(user_ave + "\n")
                f.write(user_max + "\n")
                f.write(line_min + "\n")
                f.write(kernel_start + "\n")
                f.write(kernel_end + "\n")
                f.write(kernel_ave + "\n")
                f.write(kernel_max + "\n")
                f.write(line + "\n\n\n")

    if log_result:
        return True


if __name__ == '__main__':
    # 记录报告
    ver = "7.4.8"
    modular = "live"
    if get_data(ver, modular):
        print("记录完成")
