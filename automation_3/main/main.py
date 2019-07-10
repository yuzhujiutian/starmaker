# coding=utf-8
"""
调整测试数据
依次运行对应测试脚本
"""
import time

from automation_3.report.test_data_extraction import get_data


class testSuite:
    # 测试数据调整
    def __init__(self):
        # 测试版本
        self.ver = "7.4.8"
        # 取数据次数（最低5，因为结算时会减去最高和最低）
        self.num = 5
        # 单次数据运行时间
        self.run_time = 10
        # 录制歌曲数量
        self.song_num = 2

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
            except:
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
            except:
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
            except:
                num -= 1
                continue
        self.log_result(modular)


if __name__ == '__main__':
    testSuite().liveSuite()
    testSuite().momentSuite()
    testSuite().recordingSuite()
