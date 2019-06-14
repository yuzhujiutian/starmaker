# encoding=utf-8

from automation.base.base import BaseAction


class RecordingShareAction(BaseAction):

    def done(self):
        doneBtn = self.findElementById('tv_done')
        self.singleTap(doneBtn)