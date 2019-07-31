# coding=utf-8
"""
调整测试数据
依次运行对应测试脚本
"""
import time
import sys

sys.path.append("/Users/mac/PycharmProjects/starmaker-qa/automation_3/main")
sys.path.append("/Users/mac/PycharmProjects/starmaker-qa")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python35.zip")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload")
sys.path.append("/Users/mac/PycharmProjects/starmaker-qa/venv/lib/python3.5/site-packages")
sys.path.append("/Users/mac/PycharmProjects/starmaker-qa/venv/lib/python3.5/site-packages/setuptools-41.0.1-py3.7.egg")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/Appium_Python_Client-0.24-py3.5.egg")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium-3.9.0-py3.5.egg")

from automation_3.report.test_data_extraction import get_data


class testSuite:
    # 测试数据调整
    def __init__(self):
        try:
            with open('../main/config.txt', 'r', encoding='utf-8') as f:
            # with open('/config.txt', 'r', encoding='utf-8') as f:
                config = eval(f.read())

            # 测试版本
            self.ver = config["version"]
            # 包信息
            self.package = config["package"]
            # 设备信息
            self.platformVersion = config["platformVersion"]
            self.device = config["device"]
            self.deviceName = config["deviceName"]
        except:
            # 测试版本
            self.ver = "9.9.9"
            # 包信息
            self.package = "Product"
            # 设备信息
            self.platformVersion = "8.1.0"
            self.device = "SM_G610F"
            self.deviceName = "on7xelte"

        # 取数据次数（最低5，因为结算时会减去最高和最低）
        self.num = 5
        # 单次数据运行时间
        self.run_time = 2
        # 录制歌曲数量
        self.song_num = 1

    # 测试数据处理
    def log_result(self, modular):
        result = get_data(self.ver, modular)
        if result:
            print("%s模块数据已记录成功" % modular)
        time.sleep(10)

    def liveSuite(self):
        from automation_3.live.performance_broadcaster import PerformanceBroadcaster
        modular = "live"
        num = 0
        while num < self.num:
            num += 1
            print("\n\n当前运行 %s模块 第%s次" % (modular, num))
            try:
                PerformanceBroadcaster().suiteRunner(PerformanceBroadcaster)
            except ValueError:
                num -= 1
                continue
        self.log_result(modular)

    def momentSuite(self):
        from automation_3.moment.performance_popular import PerformanceMoment
        modular = "popular"
        num = 0
        while num < self.num:
            num += 1
            print("\n\n当前运行 %s模块 第%s次" % (modular, num))
            try:
                PerformanceMoment().suiteRunner(PerformanceMoment)
            except ValueError:
                num -= 1
                continue
        self.log_result(modular)

    def recordingSuite(self):
        from automation_3.recording.performance_recording import PerformanceRecording
        modular = "recording"
        num = 0
        while num < self.num:
            num += 1
            print("\n\n当前运行 %s模块 第%s次" % (modular, num))
            try:
                PerformanceRecording().suiteRunner(PerformanceRecording)
            except ValueError:
                num -= 1
                continue
        self.log_result(modular)


if __name__ == '__main__':
    testSuite().liveSuite()
    testSuite().momentSuite()
    testSuite().recordingSuite()
