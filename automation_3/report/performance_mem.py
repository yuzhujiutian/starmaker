# encoding=utf-8
"""
用于生成内存使用报告

开始前内存占用
结束后内存占用
| 平均内存占用 | 最大内存占用 |
"""
import datetime
import json
import os
import time

root_dir = os.path.realpath(os.path.realpath(__file__) + "/../.." + "/report")
os.chdir(root_dir)


# 重定向日志，将print日志输出到控制台和日志文件里面
# TODO：重新封装日志写入；
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
        self.file_logger.write(info + '\n')
        self.file_logger.flush()

    def detail(self, info):
        self.detail_file_logger.write(info)
        self.detail_file_logger.flush()


r_logger = logger


class AndroidMemoryReport:
    def __init__(self, appPackage, driver):
        self.memInfos = []
        self.data_type = ""
        self.appPackage = appPackage
        self.driver = driver

    # 记录当前内存占用情况
    def profile(self):
        self.data_type = "memoryinfo"
        try:
            memInfo = self.driver.get_performance_data(self.appPackage, self.data_type, 5)
            self.memInfos.append(memInfo)
            self.saveRawToFile(memInfo)
        except Exception as e:
            print("get_memoryinfo_error：%s" % e)

    def clear(self):
        self.memInfos = []

    # 保存原始数据到文件
    def saveRawToFile(self, Info):
        r_logger(self.data_type).detail(json.dumps(Info, indent=2))

    # 保存测试数据到文件
    def saveTestData(self, Info):
        r_logger(self.data_type).write(Info)

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
        for m in self.memInfos[1:-1]:
            c = int(m[1][totalPssIndex])
            memory_list.append(c)
            totalMemory += c
            if c > maxMemory:
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
        self.saveTestData(module)
        self.saveTestData("duration：%s" % duration)
        self.saveTestData("frequency：%s" % frequency)
        self.saveTestData("memory_list：%s" % memory_list)
        self.saveTestData(">>>")
        self.saveTestData("------------------------------")
        self.saveTestData('%20s: %s' % ('startMemory', startMemory.__str__()))
        self.saveTestData('%20s: %s' % ('endMemory', endMemory.__str__()))
        self.saveTestData('%20s: %s' % ('averageMemory', averageMemory.__str__()))
        self.saveTestData('%20s: %s' % ('maxMemory', maxMemory.__str__()))
        self.saveTestData('%20s: %s%s' % ('maxFluctuation', max_fluctuation.__str__(), around.__str__()))
        self.saveTestData("------------------------------\n\n")
        time.sleep(2)

        self.clear()
