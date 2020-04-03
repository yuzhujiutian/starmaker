# encoding=utf-8
"""
用于生成内存/CPU使用报告

开始前内存/CPU占用
结束后内存/CPU占用
| 平均内存/CPU占用 | 最大内存/CPU占用 |
"""
import datetime
import json
import os
import time
# import subprocess

root_dir = os.path.realpath(os.path.realpath(__file__) + "/../.." + "/report")
os.chdir(root_dir)


# 重定向日志，将print日志输出到控制台和日志文件里面
class logger:
    def __init__(self, data_type='events'):
        log_dir = os.path.join(root_dir, '.logs')
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        self.file_logger = open(
            os.path.join(log_dir, "./%s-logs-%s.log" % (data_type, datetime.datetime.now().strftime('%Y%m%d'))),
            'a+', encoding='utf-8')
        self.detail_file_logger = open(
            os.path.join(log_dir, "./%s-logs-details-%s.log" % (data_type, datetime.datetime.now().strftime('%Y%m%d'))),
            'a+', encoding='utf-8')

    def write(self, info):
        self.file_logger.write(str(info) + '\n')
        self.file_logger.flush()

    def detail(self, info):
        self.detail_file_logger.write(str(info))
        self.detail_file_logger.flush()


r_logger = logger


class AndroidMemoryReport:
    def __init__(self, appPackage, driver):
        self.memInfos = []
        self.cpuInfos = []
        self.data_type_memory = "memoryinfo"
        self.data_type_cpu = "cpuinfo"
        self.appPackage = appPackage
        self.driver = driver

    # 记录当前内存占用情况
    def memory_profile(self):
        try:
            memInfo = self.driver.get_performance_data(self.appPackage, self.data_type_memory, 5)
            self.memInfos.append(memInfo)
            self.saveRawToFile(self.data_type_memory, memInfo)
        except Exception as e:
            print("get_memoryinfo_error：%s" % e)

    # 记录当前cpu占用情况
    def cpu_profile(self):
        try:
            cpuInfo = self.driver.get_performance_data(self.appPackage, self.data_type_cpu, 5)
            self.cpuInfos.append(cpuInfo)
            self.saveRawToFile(self.data_type_cpu, cpuInfo)
        except Exception as e:
            print("get_cpuinfo_error：%s" % e)

    # # 记录当前cpu占用情况
    # 这种方法会导致adb冲突
    # def cpu_profile(self):
    #     cpuInfo = subprocess.check_output("adb shell cat /proc/stat")
    #     print("cpu-----")
    #     print(cpuInfo)
    #     print("-----cpu")

    def memClear(self):
        self.memInfos = []

    def cpuClear(self):
        self.cpuInfos = []

    # 保存原始数据到文件
    @staticmethod
    def saveRawToFile(data_type, Info):
        r_logger(data_type).detail(json.dumps(Info, indent=2))

    # 保存测试数据到文件
    @staticmethod
    def saveTestData(data_type, Info):
        r_logger(data_type).write(Info)

    # 生成内存报告
    def toReport_memInfos(self, module_name, duration):
        m = self.memInfos[0]
        # 单次运行的性能数据，用于生成折线图查看波动曲线
        memory_list = []
        totalPssIndex = m[0].index('totalPss')

        startMemory = int(self.memInfos[0][1][totalPssIndex])
        memory_list.append(startMemory)
        endMemory = int(self.memInfos[-1][1][totalPssIndex])

        totalMemory = 0
        maxMemory = 0
        # 1:-1（包含1，不包含-1）
        for m in self.memInfos[1:-1]:
            c = int(m[1][totalPssIndex])
            memory_list.append(c)
            totalMemory += c
            if maxMemory < c:
                maxMemory = c
        memory_list.append(endMemory)

        # 最大波动
        max_fluctuation = 0
        around = []
        for i in range(len(memory_list) - 1):
            d_val = abs(memory_list[i] - memory_list[i + 1])
            if d_val > max_fluctuation:
                max_fluctuation = d_val
                around = [memory_list[i], memory_list[i + 1]]

        frequency = len(self.memInfos)
        averageMemory = int(float(totalMemory / (frequency - 2)))
        module = module_name + " memInfos_Report"
        self.saveTestData(self.data_type_memory, module)
        self.saveTestData(self.data_type_memory, "duration：%s" % duration)
        self.saveTestData(self.data_type_memory, "frequency：%s" % frequency)
        self.saveTestData(self.data_type_memory, "memory_list：%s" % memory_list)
        self.saveTestData(self.data_type_memory, ">>>")
        self.saveTestData(self.data_type_memory, "------------------------------")
        self.saveTestData(self.data_type_memory, '%20s: %s' % ('startMemory', startMemory.__str__()))
        self.saveTestData(self.data_type_memory, '%20s: %s' % ('endMemory', endMemory.__str__()))
        self.saveTestData(self.data_type_memory, '%20s: %s' % ('averageMemory', averageMemory.__str__()))
        self.saveTestData(self.data_type_memory, '%20s: %s' % ('maxMemory', maxMemory.__str__()))
        self.saveTestData(self.data_type_memory, '%20s: %s%s' % ('maxFluctuation', max_fluctuation.__str__(),
                                                                 around.__str__()))
        self.saveTestData(self.data_type_memory, "------------------------------\n\n")
        time.sleep(2)

        self.memClear()

    # 生成cpu报告
    def toReport_cpuInfos(self, module_name, duration):
        c = self.cpuInfos[0]
        filter_list = []
        userIndex = c[0].index('user')
        kernelIndex = c[0].index('kernel')

        # 过滤为空的数据
        for f_c in self.cpuInfos:
            f_cpu = f_c[1][userIndex]
            if int(float(f_cpu)):
                filter_list.append(f_c)

        user_cpu_list = []
        kernel_cpu_list = []

        # 收集频率
        frequency = len(self.cpuInfos)

        if filter_list is None:
            print("cpu数据获取异常")
            print("数据成功率：0%")
            return ValueError
        elif int(len(filter_list) / frequency * 100) <= 50:
            success_rate = "{:.0f}%".format(len(filter_list) / frequency * 100)
            print("数据成功率：%s" % success_rate)
            return ValueError
        else:
            # 数据成功率
            success_rate = "{:.0f}%".format(len(filter_list) / frequency * 100)
            success_frequency = len(filter_list)
            print("数据成功率：%s" % success_rate)
            # 开始CPU
            user_startCPU = int(float(filter_list[0][1][userIndex]))
            kernel_startCPU = int(float(filter_list[0][1][kernelIndex]))
            user_cpu_list.append(user_startCPU)
            kernel_cpu_list.append(kernel_startCPU)

            # 结束CPU
            user_endCPU = int(float(filter_list[-1][1][userIndex]))
            kernel_endCPU = int(float(filter_list[-1][1][kernelIndex]))

            # 总数
            user_totalCPU = 0
            kernel_totalCPU = 0
            # 最大值
            user_maxCPU = 0
            kernel_maxCPU = 0
            for c in filter_list[1:-1]:
                user_cpu = int(float(c[1][userIndex]))
                kernel_cpu = int(float(c[1][kernelIndex]))
                user_cpu_list.append(user_cpu)
                kernel_cpu_list.append(kernel_cpu)
                user_totalCPU += user_cpu
                kernel_totalCPU += kernel_cpu
                if user_maxCPU < user_cpu:
                    user_maxCPU = user_cpu
                if kernel_maxCPU < kernel_cpu:
                    kernel_maxCPU = kernel_cpu

            # 平均值
            average_userCPU = int(float(user_totalCPU / (frequency - 2)))
            average_kernelCPU = int(float(kernel_totalCPU / (frequency - 2)))

            # 结束CPU
            user_cpu_list.append(user_endCPU)
            kernel_cpu_list.append(kernel_endCPU)

            module = module_name + " cpuInfos_Report"
            self.saveTestData(self.data_type_cpu, module)
            self.saveTestData(self.data_type_cpu, "user：%s" % user_cpu_list)
            self.saveTestData(self.data_type_cpu, "kernel：%s" % kernel_cpu_list)
            self.saveTestData(self.data_type_cpu, "duration：%s" % duration)
            self.saveTestData(self.data_type_cpu, "frequency：%s(%s)" % (success_frequency, success_rate))
            self.saveTestData(self.data_type_cpu, "user_cpu_list：%s" % user_cpu_list)
            self.saveTestData(self.data_type_cpu, "kernel_cpu_list：%s" % kernel_cpu_list)
            self.saveTestData(self.data_type_cpu, ">>>")
            self.saveTestData(self.data_type_cpu, "------------------------------")
            self.saveTestData(self.data_type_cpu, '%20s: %s' % ('user_startCPU', user_startCPU.__str__()))
            self.saveTestData(self.data_type_cpu, '%20s: %s' % ('user_endCPU', user_endCPU.__str__()))
            self.saveTestData(self.data_type_cpu, '%20s: %s' % ('average_userCPU', average_userCPU.__str__()))
            self.saveTestData(self.data_type_cpu, '%20s: %s' % ('user_maxCPU', user_maxCPU.__str__()))
            self.saveTestData(self.data_type_cpu, "---------------")
            self.saveTestData(self.data_type_cpu, '%20s: %s' % ('kernel_startCPU', kernel_startCPU.__str__()))
            self.saveTestData(self.data_type_cpu, '%20s: %s' % ('kernel_endCPU', kernel_endCPU.__str__()))
            self.saveTestData(self.data_type_cpu, '%20s: %s' % ('average_kernelCPU', average_kernelCPU.__str__()))
            self.saveTestData(self.data_type_cpu, '%20s: %s' % ('kernel_maxCPU', kernel_maxCPU.__str__()))
            self.saveTestData(self.data_type_cpu, "------------------------------\n\n")
            time.sleep(2)

            self.cpuClear()
