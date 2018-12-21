# coding=utf-8
# ----------
# 首页
# ----------
from Utils.FindElement import find_element
from CommonView.VData import Home_VD


# 首页
class Home(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU

    # ----------
    # 默认首页
    # ----------
    # 首页-Popular-Text([1]/English_text=POPULAR/Hindi_text=लोकप्रिय)
    def HomePage_Popular_Text(self):
        HomePage_Popular_Text_ID = self.findClaS(Home_VD.HomePage_Popular_Text_ClaS,1)
        return HomePage_Popular_Text_ID

    # ----------
    # 首页-MainTab
    # ----------
    # 首页-MainTab-HomeTab
    def HomePage_MainTab_HomeTab(self):
        HomePage_MainTab_HomeTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 0)
        return HomePage_MainTab_HomeTab_ClaS

    # 首页-MainTab-DiscoverTab
    def HomePage_MainTab_DiscoverTab(self):
        HomePage_MainTab_DiscoverTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 1)
        return HomePage_MainTab_DiscoverTab_ClaS

    # 首页-MainTab-PostTab
    def HomePage_MainTab_PostTab(self):
        HomePage_MainTab_PostTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 2)
        return HomePage_MainTab_PostTab_ClaS

    # 首页-MainTab-NotificationTab
    def HomePage_MainTab_NotificationTab(self):
        HomePage_MainTab_NotificationTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 3)
        return HomePage_MainTab_NotificationTab_ClaS

    # 首页-MainTab-ProfileTab
    def HomePage_MainTab_ProfileTab(self):
        HomePage_MainTab_ProfileTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 4)
        return HomePage_MainTab_ProfileTab_ClaS


# ----------------------------------------------------------------------------------------------------------------------
    # ----------
    # 选择发布类型
    # ----------

    # 选择发布类型([0]Album/[1]Camera/[2]Text/[3]Sing/[4]关闭)
    def PostType_Album(self):
        PostType_ClaS = self.findClaS(Home_VD.PostType_ClaS, 0)
        return PostType_ClaS

    def PostType_Camera(self):
        PostType_ClaS = self.findClaS(Home_VD.PostType_ClaS, 1)
        return PostType_ClaS

    def PostType_Text(self):
        PostType_ClaS = self.findClaS(Home_VD.PostType_ClaS, 2)
        return PostType_ClaS

    def PostType_Sing(self):
        PostType_ClaS = self.findClaS(Home_VD.PostType_ClaS, 3)
        return PostType_ClaS

    def PostType_Close(self):
        PostType_ClaS = self.findClaS(Home_VD.PostType_ClaS, 4)
        return PostType_ClaS
