# encoding=utf-8
"""
用于生成内存使用报告

开始前内存占用
结束后内存占用
| 平均内存占用 | 最大内存占用 |
"""


class AndroidMemoryReport:

    def __init__(self, appPackage, driver):
        self.memInfos = []
        self.appPackage = appPackage
        self.driver = driver

    # 记录当前内存占用情况
    def profile(self):
        try:
            memInfo = self.driver.get_performance_data(self.appPackage, 'memoryinfo', 5)
            self.memInfos.append(memInfo)
        except Exception as e:
            pass

    def clear(self):
        self.memInfos = []

    # 保存原始数据到文件
    def saveRawToFile(self, filePath):
        pass

    # todo: 生成内存报告
    def toReport(self):
        m = self.memInfos[0]
        totalPssIndex = m[0].index('totalPss')

        startMemory = self.memInfos[0][1][totalPssIndex]
        endMemory = self.memInfos[-1][1][totalPssIndex]

        totalMemory = 0
        maxMemory = 0
        for m in self.memInfos[1:-2]:
            c = int(m[1][totalPssIndex])
            totalMemory += c
            if c > maxMemory:
                maxMemory = c

        averageMemory = int(totalMemory/(len(self.memInfos) - 2))

        print('startMemory:', startMemory)
        print('endMemory:', endMemory)
        print('averageMemory:', averageMemory)
        print('maxMemory:', maxMemory)



