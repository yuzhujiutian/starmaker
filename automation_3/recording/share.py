# encoding=utf-8

from automation_3.base.base import BaseAction


class RecordingShareAction(BaseAction):

    def done(self):
        doneBtn = self.findElementById('tv_done')
        self.singleTap(doneBtn)