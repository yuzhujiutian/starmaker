# coding=utf-8
# 维护版本：
# 维护日期：
# 维护人员：
# ----------
# 启动模块
# ----------
from StarMaker.CommonView.VData import StartUp_VD
from StarMaker.Utils import Tools
from StarMaker.Utils.FindElement import find_element


# 启动模块
class StartUp(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findAU = find_element().AU
        self.findClaS = find_element().ClaS
        self.DIYSwipe_Percentage = Tools.Screen().DIYSwipe_Percentage

    # 语言选择页-ClaS(用于校验)
    def ChooseLanguagePage_Check(self):
        ChooseLanguagePage_Check_ClaS = StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS
        return ChooseLanguagePage_Check_ClaS

    # 语言选择页-校验启动成功-顶部Tips文案([0]text=Choose Language)
    def ChooseLanguagePage_CheckStartSuccess_Tips(self):
        ChooseLanguagePage_CheckStartSuccess_Tips_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_CheckStartSuccess_Tips_ClaS, 0)
        return ChooseLanguagePage_CheckStartSuccess_Tips_ClaS

    # 语言选择页-选择语言-选择印地语([1]text=हिन्दी)
    def ChooseLanguagePage_SelectLanguage(self, num):
        ChooseLanguagePage_SelectLanguage_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, num)
        return ChooseLanguagePage_SelectLanguage_ClaS

