# coding=utf-8
import os
import time

from PerformanceEvaluationTest._main_ import main
from PerformanceEvaluationTest.task import Task


class StartAppTask(Task):
    def __init__(self, name):
        print("进入StartAppTask类")
        super().__init__(name)

    # 自定义场景在此处编写
    def execute(self):
        # 启动app
        self.d.app_start("com.starmakerinteractive.starmaker")
        time.sleep(10)
        # 坐标:选择语言English
        os.system("adb shell input tap 520 310")
        time.sleep(10)
        # 坐标:点击关闭首页引导
        os.system("adb shell input tap 360 640")
        time.sleep(2)
        # 坐标:点击Moment
        os.system("adb shell input tap 70 1220")
        time.sleep(8)
        time_start = time.time()
        a = 0
        while a < 60:
            os.system("adb shell input swipe 360 1024 360 256")
            time.sleep(2)
            time_end = time.time()
            a = time_end - time_start


if __name__ == '__main__':
    main(StartAppTask("StartApp"))
