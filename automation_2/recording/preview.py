# encoding=utf-8
from automation_2.base.base import BaseAction
from automation_2.common.activity import Activity
from automation_2.login.login import LoginAction


# 封装录制相关的操作
class RecordingPreviewAction(BaseAction):

    # 对话框确认逻辑，
    def post(self):
        postBtn = self.findElementById('btn_post')
        self.singleTap(postBtn)

        # todo: 需要校验postBtn点击已经生效

        loginAction = LoginAction(self)
        loginAction.checkToLogin(preActivity=Activity.RecordingPreview)

    def restart(self):
        closeBtn = self.findElementById('imb_close')
        self.singleTap(closeBtn)

        # todo: 找到restart按钮
        restartBtn = self.findElementsById('text1')[0]
        self.singleTap(restartBtn)

    def quit(self):
        closeBtn = self.findElementById('imb_close')
        self.singleTap(closeBtn)

        # todo: 找到exit按钮
        quitBtn = self.findElementsById('text1')[1]
        self.singleTap(quitBtn)

        # 确认删除文件，退出录制
        self.dialogBtnClick(confirm=True)
