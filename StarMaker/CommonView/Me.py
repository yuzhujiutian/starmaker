# coding=utf-8
# 维护版本：
# 维护日期：
# 维护人员：
# ----------
# Me模块
# ----------
from StarMaker.CommonView.VData import Me_VD
from StarMaker.Utils.FindElement import find_element


class Me(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU

# ----------
    # 首页-Me界面
    # ----------
    # 用于校验是否进入Me界面
    def MePage_Tab_Me(self):
        MePage_Tab_Me_Text = self.findAU("new UiSelector().text(\"Me\")")
        return MePage_Tab_Me_Text

    # 个人页用户个人经验值
    def MePage_Tab_MeExperience(self):
        MePage_Tab_MeExperience_ClaS = self.findClaS(Me_VD.MePage_Tab_MeExperience_Class, 2)
        return MePage_Tab_MeExperience_ClaS

    # My Level页的个人经验值
    def MyLevel_Tab_MeExperience(self):
        MyLevel_Tab_MeExperience_ClaS = self.findClaS(Me_VD.MePage_Tab_MeExperience_Class, 1)
        return MyLevel_Tab_MeExperience_ClaS

    # 个人页用户VIP标识
    def MyLevel_Tab_VIPIdentification(self):
        MyLevel_Tab_VIPIdentification_ClaS = self.findClaS(Me_VD.MePage_Tab_MeExperience_Class, 3)
        return MyLevel_Tab_VIPIdentification_ClaS

    # My Level页的返回按钮
    def MeExperience_MyLevel_backButton(self):
        MyLevel_Tab_VIPIdentification_ClaS = self.findCla(Me_VD.Source_Mylevel_BackButton_Class)
        return MyLevel_Tab_VIPIdentification_ClaS