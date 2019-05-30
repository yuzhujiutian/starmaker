# coding=utf-8
# ----------
# 弹窗
# ----------
import time

from StarMaker.CommonView.VData import Popup_VD
from StarMaker.Utils import Tools
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver


# 弹窗处理
class Popup(object):
    def __init__(self):
        self.driver = GetAppiumDeriver().driver
        self.FindElement = Tools.PopupProcessing().Popup_GeneralMethod

    # ----------
    # 1>首页弹窗
    # ----------
    # ①NewFeature引导，如果存在则点击NEXT
    def HomePopup_NewFeature_NEXT_LiveClick(self):
        state = self.FindElement(AU=[Popup_VD.Popup_NewFeature_AU, "Only for your taste. Hope you love them."])
        if state:
            self.driver.find_element_by_android_uiautomator(Popup_VD.Popup_NEXT).click()

    # ②NewFeature Added引导，如果存在则点击NEXT
    def HomePopup_NewFeatureAdded_NEXT_LiveClick(self):
        state = self.FindElement(AU=[Popup_VD.Popup_NewFeatureAdded_AU, "New feature added. Tap to post your stories."])
        if state:
            self.driver.find_element_by_android_uiautomator(Popup_VD.Popup_NEXT).click()

    # ③登录后首页 Sing 引导（text=Sing is moved here. Tap to show your voice./NEXT）
    def HomePopup_NewFeatureSing_NEXT_LiveClick(self):
        state = self.FindElement(AU=[Popup_VD.Popup_NewFeatureSing_AU, "Sing is moved here. Tap to show your voice."])
        if state:
            self.driver.find_element_by_android_uiautomator(Popup_VD.Popup_NEXT).click()

    # ④登录后首页 PostOther 引导（text=Post Photo,Gif and Video here/DONE）
    def HomePopup_NewFeaturePostOther_DONE_LiveClick(self):
        state = self.FindElement(AU=[Popup_VD.Popup_NewFeaturePostOther_AU, "Post Photo,Gif and Video here"])
        if state:
            self.driver.find_element_by_android_uiautomator(Popup_VD.Popup_DONE).click()

    # 位置信息权限弹窗
    def HomePopup_PermissionMessage_Allow_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_PermissionMessage_ID, "要允许StarMaker获取此设备的位置信息吗？"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_PermissionMessage_Allow_ID).click()

    # # Ranking 引导，如果存在则点击Next
    # def HomePopup_RankingGuide_Next_LiveClick(self):
    #     state = self.FindElement(ID=[Popup_VD.Popup_Guide_Next_ID, "NEXT"])
    #     if state:
    #         self.driver.find_element_by_id(Popup_VD.Popup_Guide_Next_ID).click()
    #
    # # Parties 引导，如果存在泽点击Next
    # def HomePopup_PartiesGuide_Next_LiveClick(self):
    #     state = self.FindElement(ID=[Popup_VD.Popup_Guide_Next_ID, "NEXT"])
    #     if state:
    #         self.driver.find_element_by_id(Popup_VD.Popup_Guide_Next_ID).click()
    #
    # # Live 引导，如果存在泽点击Done
    # def HomePopup_LiveGuide_Done_LiveClick(self):
    #     state = self.FindElement(ID=[Popup_VD.Popup_Guide_Next_ID, "DONE"])
    #     if state:
    #         self.driver.find_element_by_id(Popup_VD.Popup_Guide_Next_ID).click()

    # 签到按钮，如果存在，需点击通用close按钮
    def HomePopup_CheckIn_Close_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_CheckIn_ID, "CHECK IN"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_ImgClose_ID).click()

    # ----------
    # 2>Profile页弹窗
    # ----------

    # 验证邮箱弹窗，如果存在，需点击通用close按钮
    def HomePopup_VerifyEmail_Close_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_VerifyEmail_Verify_ID, "VERIFY"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_ImgClose_ID).click()

    # ----------
    # 3>点唱页弹窗
    # ----------

    # 发布图片引导(text=Click to post a photo)
    def SingPopup_PostPhotoGuide_Click_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_PostGuide_ID, "Click to post a photo"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_PostGuide_ID).click()

    # 发布图片+文字引导(text=Post texts with background photo.)
    def SingPopup_PostTextsPhotoGuide_Click_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_PostGuide_ID, "Post texts with background photo."])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_PostGuide_ID).click()

    # ----------
    # 4>录制准备页
    # ----------

    # 权限申请(text=Ok, Let's do it.)
    def SingPopup_Jurisdiction_LiveClick(self, text="Ok, Let's do it."):
        state = self.FindElement(ID=[Popup_VD.Popup_Jurisdiction_ID, text])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_Jurisdiction_ID).click()
            time.sleep(2)
            self.driver.find_element_by_id(Popup_VD.Popup_PermissionAllow_ID).click()
            time.sleep(2)
            self.driver.find_element_by_id(Popup_VD.Popup_PermissionAllow_ID).click()
            time.sleep(2)
            self.driver.find_element_by_id(Popup_VD.Popup_PermissionAllow_ID).click()
            time.sleep(2)

    # 插入耳机引导(text=I KNOW)
    def SingPopup_HeadphonesRecommended_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_HeadphonesRecommended_ID, "I KNOW"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_HeadphonesRecommended_ID).click()

    # 音效引导(text=Change the song's pitch to match \n your voice!)
    def SingPopup_PitchGuide_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_PitchGuide_ID, "Change the song's pitch to match \n your voice!"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_PitchGuide_ID).click()

    # ----------
    # 5>KTV/Live
    # ----------
    # KTV排麦引导(text=Select a song, queue up and sing to gain your popularity!)
    def Popup_KTVPage_QueueUp_LiveClick(self):
        state = self.FindElement(AU=[Popup_VD.Popup_KTVPage_QueueUp_AU, "Select a song, queue up and sing to gain your popularity!"])
        if state:
            self.driver.find_element_by_android_uiautomator(Popup_VD.Popup_KTVPage_QueueUp_AU).click()
            # 处理衍生的另一个弹窗
            self.driver.back()

    # Live滑动引导(text=Scroll up or down to change the live room)
    def Popup_LivePage_Slide_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_LivePage_Slide_ID, "Scroll up or down to change the live room"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_LivePage_Slide_ID).click()
