# coding=utf-8
import time


class Task(object):
    def __init__(self, name):
        print("进入Task类")
        self.name = name
        self.period = None
        self.d = None
        self.device = None
        self.applicationid = None
        self.version_name = None
        self.pid = None
        self.interval = None
        self.output = None
        self.info_list = set([])

    # 此处编写测试用例
    def execute(self):
        print("execute!!!")

    def add_info(self, info):
        print("进入add_info方法")
        self.info_list.add(info)
        info.task = self

    def set_device(self, d):
        print("进入set_device方法")
        self.d = d


class RandomTask(Task):

    def __init__(self, name):
        print("进入RandomTask类")
        super().__init__(name)
        self.duration = 0.0

    def execute(self):
        print("进入RandomTask.execute方法")
        time.sleep(self.duration)
