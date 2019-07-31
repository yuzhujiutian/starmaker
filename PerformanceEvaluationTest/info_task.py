# coding=utf-8
class InfoTask(object):
    def __init__(self, task):
        print("进入InfoTask类")
        self.task = task

    def start(self):
        print("进入InfoTask.start方法")
        for info in self.task.info_list:
            info.get_start_info()

        if self.task:
            self.task.execute()

        for info in self.task.info_list:
            info.get_end_info()
