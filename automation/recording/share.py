#encoding=utf-8

from base.base import BaseAction
from common.activity import Activity

def RecordingShareAction(BaseAction):

    def done(self):
        doneBtn = self.findElementById('tv_done')
        self.singleTap(doneBtn)