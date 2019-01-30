# coding=utf-8
# ----------
# Jalebee
# ----------
from Utils.FindElement import find_element
from CommonView.VData import Jalebee_VD
from Utils.Tools import Popular_Elements_Disposes


# Jalebee
class Jalebee(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU
        self.ID_IDS = Popular_Elements_Disposes().ID_IDS
        self.ID_IDS_Count = Popular_Elements_Disposes().ID_IDS_Count

    # ----------
    # Jalebee首页
    # ----------
    # 首页-MainTab-通用(用于校验)
    def JalebeeHomePage_MainTab_Check(self):
        JalebeeHomePage_MainTab_Check_IDS = Jalebee_VD.Jalebee_MainTab_Common_IDS
        return JalebeeHomePage_MainTab_Check_IDS

    # 首页-MainTab-Home
    def JalebeeHomePage_MainTab_Home(self):
        JalebeeHomePage_MainTab_Home_IDS = self.findIDS(Jalebee_VD.Jalebee_MainTab_Common_IDS, 0)
        return JalebeeHomePage_MainTab_Home_IDS

    # 首页-MainTab-Party
    def JalebeeHomePage_MainTab_Party(self):
        JalebeeHomePage_MainTab_Party_IDS = self.findIDS(Jalebee_VD.Jalebee_MainTab_Common_IDS, 1)
        return JalebeeHomePage_MainTab_Party_IDS

    # 首页-MainTab-Message
    def JalebeeHomePage_MainTab_Message(self):
        JalebeeHomePage_MainTab_Message_IDS = self.findIDS(Jalebee_VD.Jalebee_MainTab_Common_IDS, 2)
        return JalebeeHomePage_MainTab_Message_IDS

    # 首页-MainTab-Me
    def JalebeeHomePage_MainTab_Me(self):
        JalebeeHomePage_MainTab_Me_IDS = self.findIDS(Jalebee_VD.Jalebee_MainTab_Common_IDS, 3)
        return JalebeeHomePage_MainTab_Me_IDS

    # Jalebee首页内容Tab(用于校验)
    def JalebeeHomePage_FeedTab_Check(self):
        Jalebee_FeedTab_Common_IDS = Jalebee_VD.Jalebee_FeedTab_Common_IDS
        return Jalebee_FeedTab_Common_IDS

    # Jalebee首页内容Tab-FOLLOWING
    def JalebeeHomePage_FeedTab_FOLLOWING(self):
        Jalebee_FeedTab_Common_IDS = self.findIDS(Jalebee_VD.Jalebee_FeedTab_Common_IDS, 0)
        return Jalebee_FeedTab_Common_IDS

    # Jalebee首页内容Tab-POPULAR
    def JalebeeHomePage_FeedTab_POPULAR(self):
        Jalebee_FeedTab_Common_IDS = self.findIDS(Jalebee_VD.Jalebee_FeedTab_Common_IDS, 1)
        return Jalebee_FeedTab_Common_IDS

