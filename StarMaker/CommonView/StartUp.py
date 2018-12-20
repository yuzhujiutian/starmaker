# coding=utf-8
# ----------
# 启动模块
# ----------
from Utils import Tools
from Utils.FindElement import find_element
from CommonView.VData import StartUp_VD
from CommonView.VData import LogIn_VD


# 启动模块
class StartUp(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findAU = find_element().AU
        self.findClaS = find_element().ClaS
        self.DIYSwipe_Percentage = Tools.Screen().DIYSwipe_Percentage

    # 语言选择页-校验启动成功-顶部Tips文案([0]text=Choose Language)
    def ChooseLanguagePage_CheckStartSuccess_Tips(self):
        ChooseLanguagePage_CheckStartSuccess_Tips_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_CheckStartSuccess_Tips_ClaS,0)
        return ChooseLanguagePage_CheckStartSuccess_Tips_ClaS

    # 语言选择页-选择语言-选择印地语([1]text=हिन्दी)
    def ChooseLanguagePage_SelectLanguage_SelectHindi(self):
        ChooseLanguagePage_SelectLanguage_SelectHindi_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS,1)
        return ChooseLanguagePage_SelectLanguage_SelectHindi_ClaS

    # 语言选择页-选择语言-选择英语([15]text=English)
    def ChooseLanguagePage_SelectLanguage_SelectEnglish(self):
        ChooseLanguagePage_SelectLanguage_SelectEnglish_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS,15)
        return ChooseLanguagePage_SelectLanguage_SelectEnglish_ClaS
