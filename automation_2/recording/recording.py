# encoding=utf-8
from automation_2.base.base import BaseAction


# 封装录制相关的操作
class RecordingAction(BaseAction):
    ID_Record_Btn = 'record_btn'

    def startRecording(self):
        el = self.findElementById(RecordingAction.ID_Record_Btn)
        el.click()

    def stopRecording(self):
        finishBtn = None

        while finishBtn is None:
            # 确定finish按钮出现
            finishBtn = self.findElementById('finish_tv')

            if finishBtn:
                finishBtn.click()
                break

            try:
                # 停止录制
                el = self.findElementById(RecordingAction.ID_Record_Btn)
                el.click()
            except Exception as e:
                print e

            self.actionSleep(1)

    # 切换摄像头
    def switchCamera(self):
        el = self.findElementById('media_type_chb')
        el.click()

        self.actionSleep(1)

    # 清理各种引导
    def clearGuide(self):
        # 耳机提示框
        el = self.findElementById('recording_headset_dialog_i_know_btn')
        if el:
            el.click()

        self.actionSleep(1)

        # 引导提示
        el = self.findElementById('tv_pitch_guide_tip')
        if el:
            el.click()

    # 检查权限弹窗
    def checkPermission(self):
        grantOkBtn = self.findElementById('permissionOkTv')

        if grantOkBtn:
            grantOkBtn.click()

            while 1:
                permitBtn = self.findElementById('com.android.packageinstaller:id/permission_allow_button')
                if permitBtn:
                    permitBtn.click()
                else:
                    break

                permitBtn = self.findElementById('com.android.packageinstaller:id/permission_allow_button')
                if permitBtn:
                    permitBtn.click()
                else:
                    break

                permitBtn = self.findElementById('com.android.packageinstaller:id/permission_allow_button')
                if permitBtn:
                    permitBtn.click()
                else:
                    break

                break

    def a(self):
        pass
