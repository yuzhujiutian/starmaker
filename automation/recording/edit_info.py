#encoding=utf-8

from base.base import BaseAction
from login.login import LoginAction
from common.activity import Activity

import time

'''
封装录制相关的操作
'''
class RecordingEditInfoAction(BaseAction):

    # 设置作品描述
    def setDesc(self, desc=None):
        el = self.findElementById('writing_edit_view')
        if desc == None:
            el.set_text('this is recording description: ' + str(time.time()))
        else:
            el.set_text(desc)

    # 发表作品
    def send(self):
        el = self.findElementById('btn_next')
        self.singleTap(el)