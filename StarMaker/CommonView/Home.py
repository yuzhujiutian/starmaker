# coding=utf-8
# ----------
# 首页
# ----------
from Utils.FindElement import find_element
from CommonView.VData import Home_VD
from Utils.Tools import Popular_Elements_Disposes


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
        self.ID_IDS = Popular_Elements_Disposes().ID_IDS
        self.ID_IDS_Count = Popular_Elements_Disposes().ID_IDS_Count

    # ----------
    # 默认首页
    # ----------
    # 首页-Popular-Text([1]/English_text=POPULAR/Hindi_text=लोकप्रिय)
    def HomePage_Popular_Text(self):
        HomePage_Popular_Text_ID = self.findClaS(Home_VD.HomePage_Popular_Text_ClaS, 1)
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

    # ----------
    # 首页-HotTopics
    # ----------
    # 首页-HotTopics-Text(English_text=Hot topics)
    def HomePage_HotTopics_Text(self):
        HomePage_HotTopics_Text_ID = self.findID(Home_VD.HomePage_HotTopics_Text_ID)
        return HomePage_HotTopics_Text_ID

    # 首页-HotTopics-SeeAll(English_text=SEE ALL)
    def HomePage_HotTopics_SeeAll(self):
        HomePage_HotTopics_SeeAll_ID = self.findID(Home_VD.HomePage_HotTopics_SeeAll_ID)
        return HomePage_HotTopics_SeeAll_ID

    # 首页-feed卡片_Follow-返回当前页个数
    def HomePage_FeedCard_FollowCount(self):
        HomePage_FeedCard_FollowCount = self.ID_IDS_Count(Home_VD.HomePage_FeedCard_Follow_ID_IDS)
        return HomePage_FeedCard_FollowCount

    # 首页-feed卡片_Follow(English_text=FOLLOW)(ID/IDS)
    def HomePage_FeedCard_Follow(self):
        HomePage_FeedCard_Follow_ID = self.ID_IDS(Home_VD.HomePage_FeedCard_Follow_ID_IDS)
        return HomePage_FeedCard_Follow_ID

    # 首页-feed卡片_叉号-返回当前页个数
    def HomePage_FeedCard_DislikeCount(self):
        HomePage_FeedCard_DislikeCount = self.ID_IDS_Count(Home_VD.HomePage_FeedCard_Dislike_ID_IDS)
        return HomePage_FeedCard_DislikeCount

    # 首页-feed卡片_叉号(ID/IDS)
    def HomePage_FeedCard_Dislike(self):
        HomePage_FeedCard_Dislike_ID = self.ID_IDS(Home_VD.HomePage_FeedCard_Dislike_ID_IDS)
        return HomePage_FeedCard_Dislike_ID

    # ----------
    # 首页-Dislike弹窗
    # ----------
    # 首页-Dislike弹窗-Unwanted
    def HomePage_DislikePop_Unwanted(self):
        HomePage_DislikePop_Unwanted_ID = self.findID(Home_VD.HomePage_DislikePop_Unwanted_ID)
        return HomePage_DislikePop_Unwanted_ID

    # 首页-Dislike弹窗-Report
    def HomePage_DislikePop_Report(self):
        HomePage_DislikePop_Report_ID = self.findID(Home_VD.HomePage_DislikePop_Report_ID)
        return HomePage_DislikePop_Report_ID

    # 首页-Dislike弹窗-Cancel
    def HomePage_DislikePop_Cancel(self):
        HomePage_DislikePop_Cancel_ID = self.findID(Home_VD.HomePage_DislikePop_Cancel_ID)
        return HomePage_DislikePop_Cancel_ID
