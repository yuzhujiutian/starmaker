# coding=utf-8
import os
import time

from PerformanceEvaluationTest._main_ import main
from PerformanceEvaluationTest.task import Task


class StartAppTask(Task):
    def __init__(self, name):
        super().__init__(name)

    def execute(self):
        self.d.app_start("com.starmakerinteractive.starmaker")
        time_start = time.time()
        a = 0
        while a < 10:
            os.system("adb shell input swipe 360 1024 360 256")
            time.sleep(2)
            time_end = time.time()
            a = time_end - time_start


if __name__ == '__main__':
    main(StartAppTask("StartApp"))
