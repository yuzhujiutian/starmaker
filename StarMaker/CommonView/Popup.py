# coding=utf-8
# ----------
# 弹窗
# ----------
from Utils import Tools
from CommonView.VData import Popup_VD
from Utils.GetAppiumDeriver import GetAppiumDeriver


# 弹窗处理
class Popup(object):
    def __init__(self):
        self.driver = GetAppiumDeriver().driver
        self.FindElement = Tools.PopupProcessing().Popup_GeneralMethod

    # ----------
    # 1>首页弹窗
    # ----------
    # NewFeature引导，如果存在则点击OK
    def HomePopup_NewFeature_OK_LiveClick(self):
        state = self.FindElement(Cla=[Popup_VD.Popup_NewFeature_Class, 2, "OK"])
        if state:
            self.driver.find_elements_by_class_name(Popup_VD.Popup_NewFeature_Class)[2].click()

    # Ranking 引导，如果存在则点击Next
    def HomePopup_RankingGuide_Next_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_Guide_Next_ID, "NEXT"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_Guide_Next_ID).click()

    # Parties 引导，如果存在泽点击Next
    def HomePopup_PartiesGuide_Next_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_Guide_Next_ID, "NEXT"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_Guide_Next_ID).click()

    # Live 引导，如果存在泽点击Done
    def HomePopup_LiveGuide_Done_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_Guide_Next_ID, "DONE"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_Guide_Next_ID).click()

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
    # 3>点唱页页弹窗
    # ----------

    # 发布图片引导(text=Click to post a photo)
    def HomePopup_PostPhotoGuide_Click_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_PostGuide_ID, "Click to post a photo"])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_PostGuide_ID).click()

    # 发布图片+文字引导(text=Post texts with background photo.)
    def HomePopup_PostTextsPhotoGuide_Click_LiveClick(self):
        state = self.FindElement(ID=[Popup_VD.Popup_PostGuide_ID, "Post texts with background photo."])
        if state:
            self.driver.find_element_by_id(Popup_VD.Popup_PostGuide_ID).click()
