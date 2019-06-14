# encoding=utf-8
import time

from automation.base.base import BaseAction


# 封装录制相关的操作
class RecordingEditInfoAction(BaseAction):

    # 设置作品描述
    def setDesc(self, desc=None):
        el = self.findElementById('writing_edit_view')
        if desc is None:
            el.set_text('this is recording description: ' + str(time.time()))
        else:
            el.set_text(desc)

    # 发表作品
    def send(self):
        el = self.findElementById('btn_next')
        self.singleTap(el)
