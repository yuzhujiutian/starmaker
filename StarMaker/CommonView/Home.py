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
    # 首页-切换内容Tab-Following
    def HomePage_SwitchTab_FollowingTab(self):
        HomePage_Common_SwitchTab_ClaS = self.findClaS(Home_VD.HomePage_Common_SwitchTab_ClaS, 0)
        return HomePage_Common_SwitchTab_ClaS

    # 首页-切换内容Tab-Popular
    # English_text=POPULAR/Hindi_text=लोकप्रिय
    def HomePage_SwitchTab_PopularTab(self):
        HomePage_Common_SwitchTab_ClaS = self.findClaS(Home_VD.HomePage_Common_SwitchTab_ClaS, 1)
        return HomePage_Common_SwitchTab_ClaS

    # 首页-切换内容Tab-Sing
    def HomePage_SwitchTab_SingTab(self):
        HomePage_Common_SwitchTab_ClaS = self.findClaS(Home_VD.HomePage_Common_SwitchTab_ClaS, 2)
        return  HomePage_Common_SwitchTab_ClaS

    # 首页-通用-搜索框
    def HomePage_Common_Search(self):
        HomePage_Common_Search_ID = self.findID(Home_VD.HomePage_Common_Search_ID)
        return HomePage_Common_Search_ID

    # 首页-通用-Library
    def HomePage_Common_Library(self):
        HomePage_Common_Library_ID = self.findID(Home_VD.HomePage_Common_Library_ID)
        return HomePage_Common_Library_ID

    # 首页-通用-切换内容语言
    def HomePage_Common_ContentLanguage(self):
        HomePage_Common_ContentLanguage_ID = self.findID(Home_VD.HomePage_Common_ContentLanguage_ID)
        return HomePage_Common_ContentLanguage_ID

    # ----------
    # 首页-语言选择弹窗
    # ----------
    # 首页-语言选择弹窗-Tips(English_text=The content displayed will be based on the language you choose.)
    def HomePage_ChooseLanguage_IndiaTips(self):
        HomePage_ChooseLanguage_IndiaTips_ID = self.findID(Home_VD.HomePage_ChooseLanguage_IndiaTips_ID)
        return HomePage_ChooseLanguage_IndiaTips_ID

    # 首页-语言选择弹窗-切换语言([0]हिन्दी(Hindi)/[1]বাংলা(Bengali)/[2]ಕನ್ನಡ(Kannada)/[3]தமிழ்(Tamil)/[4]ગુજરાતી(Gujarati)/
    # [5]ଓଡ଼ିଆ(Odia)/[6]മലയാളം(Malayalam)/[7]मराठी(Marathi)/[8]తెలుగు(Telugu)/[9]ਪੰਜਾਬੀ(Punjabi)/[10]অসমীয়া(Assamese)/
    # [滑动翻页][-4]हरियाणवी(Haryanvi)/[-3]राजस्थानी(Rajasthani)/[-2]भोजपूरी(Bhojpuri)/[-1]English(English))
    def HomePage_ChooseLanguage_IndiaSwitchLanguage(self, num):
        HomePage_ChooseLanguage_IndiaSwitchLanguage_IDS = self.findIDS(Home_VD.HomePage_ChooseLanguage_IndiaSwitchLanguage_IDS, num)
        return HomePage_ChooseLanguage_IndiaSwitchLanguage_IDS

    def HomePage_ChooseLanguage_ByTextSwitchLanguage(self, text):
        HomePage_ChooseLanguage_ByTextSwitchLanguage_AU = self.findAU(text)
        return HomePage_ChooseLanguage_ByTextSwitchLanguage_AU

    # ----------
    # 首页-MainTab
    # ----------
    # 首页-MainTab-Moment
    def HomePage_MainTab_MomentTab(self):
        HomePage_MainTab_MomentTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 0)
        return HomePage_MainTab_MomentTab_ClaS

    # 首页-MainTab-Party
    def HomePage_MainTab_PartyTab(self):
        HomePage_MainTab_PartyTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 1)
        return HomePage_MainTab_PartyTab_ClaS

    # 首页-MainTab-Sing
    def HomePage_MainTab_SingTab(self):
        HomePage_MainTab_SingTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 2)
        return HomePage_MainTab_SingTab_ClaS

    # 首页-MainTab-Message
    def HomePage_MainTab_MessageTab(self):
        HomePage_MainTab_MessageTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 3)
        return HomePage_MainTab_MessageTab_ClaS

    # 首页-MainTab-Me
    def HomePage_MainTab_MeTab(self):
        HomePage_MainTab_MeTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_ClaS, 4)
        return HomePage_MainTab_MeTab_ClaS

    # 首页-MainTabName-Moment
    def HomePage_MainTabName_Moment(self):
        HomePage_MainTab_HomeTab_ClaS = self.findIDS(Home_VD.HomePage_MainTab_TabName_IDS, 0)
        return HomePage_MainTab_HomeTab_ClaS

    # 首页-MainTabName-Party
    def HomePage_MainTabName_Party(self):
        HomePage_MainTab_DiscoverTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_TabName_IDS, 1)
        return HomePage_MainTab_DiscoverTab_ClaS

    # 首页-MainTabName-Sing
    def HomePage_MainTabName_Sing(self):
        HomePage_MainTab_PostTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_TabName_IDS, 2)
        return HomePage_MainTab_PostTab_ClaS

    # 首页-MainTabName-Message
    def HomePage_MainTabName_Message(self):
        HomePage_MainTab_NotificationTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_TabName_IDS, 3)
        return HomePage_MainTab_NotificationTab_ClaS

    # 首页-MainTabName-Me
    def HomePage_MainTabName_Me(self):
        HomePage_MainTab_ProfileTab_ClaS = self.findClaS(Home_VD.HomePage_MainTab_TabName_IDS, 4)
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

    # ----------
    # 首页-feed卡片
    # ----------
    # 首页-feed卡片_头像(ID/IDS)
    def HomePage_FeedCard_HeadView(self):
        HomePage_FeedCard_HeadView_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_HeadView_ID_IDS)
        return HomePage_FeedCard_HeadView_ID_IDS

    # 首页-feed卡片_用户名(ID/IDS)
    def HomePage_FeedCard_UserName(self):
        HomePage_FeedCard_UserName_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_UserName_ID_IDS)
        return HomePage_FeedCard_UserName_ID_IDS

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

    # 首页-feed卡片_描述(ID/IDS)
    def HomePage_FeedCard_Describe(self):
        HomePage_FeedCard_Describe_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_Describe_ID_IDS)
        return HomePage_FeedCard_Describe_ID_IDS

    # 首页-feed卡片_图片(ID/IDS)
    def HomePage_FeedCard_Img(self):
        HomePage_FeedCard_Img_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_Img_ID_IDS)
        return HomePage_FeedCard_Img_ID_IDS

    # 首页-feed卡片_视屏(ID/IDS)
    def HomePage_FeedCard_Video(self):
        HomePage_FeedCard_Video_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_Video_ID_IDS)
        return HomePage_FeedCard_Video_ID_IDS

    # 首页-feed卡片_分享按钮(ID/IDS)
    def HomePage_FeedCard_Share(self):
        HomePage_FeedCard_Share_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_Share_ID_IDS)
        return HomePage_FeedCard_Share_ID_IDS

    # 首页-feed卡片_分享数(ID/IDS)
    def HomePage_FeedCard_ShareCount(self):
        HomePage_FeedCard_ShareCount_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_ShareCount_ID_IDS)
        return HomePage_FeedCard_ShareCount_ID_IDS

    # 首页-feed卡片_评论按钮(ID/IDS)
    def HomePage_FeedCard_Comment(self):
        HomePage_FeedCard_Comment_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_Comment_ID_IDS)
        return HomePage_FeedCard_Comment_ID_IDS

    # 首页-feed卡片_评论数(ID/IDS)
    def HomePage_FeedCard_CommentCount(self):
        HomePage_FeedCard_CommentCount_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_CommentCount_ID_IDS)
        return HomePage_FeedCard_CommentCount_ID_IDS

    # 首页-feed卡片_like按钮(ID/IDS)
    def HomePage_FeedCard_Like(self):
        HomePage_FeedCard_Like_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_Like_ID_IDS)
        return HomePage_FeedCard_Like_ID_IDS

    # 首页-feed卡片_like数(ID/IDS)
    def HomePage_FeedCard_LikeCount(self):
        HomePage_FeedCard_LikeCount_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_LikeCount_ID_IDS)
        return HomePage_FeedCard_LikeCount_ID_IDS

    # 首页-feed卡片_下载按钮(ID/IDS)
    def HomePage_FeedCard_Download(self):
        HomePage_FeedCard_Download_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_Download_ID_IDS)
        return HomePage_FeedCard_Download_ID_IDS

    # 首页-feed卡片_WhatsApp按钮(ID/IDS)
    def HomePage_FeedCard_WhatsApp(self):
        HomePage_FeedCard_WhatsApp_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_WhatsApp_ID_IDS)
        return HomePage_FeedCard_WhatsApp_ID_IDS

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

    # ----------
    # 首页-弹窗
    # ----------
    # 首页-Share弹窗-外框
    def HomePage_SharePop_Frame(self):
        HomePage_SharePop_Frame_ID = self.findID(Home_VD.HomePage_SharePop_Frame_ID)
        return HomePage_SharePop_Frame_ID

    # 首页-WhatsApp弹窗-外框
    def HomePage_WhatsAppPop_Frame(self):
        HomePage_WhatsAppPop_Frame_ID = self.findID(Home_VD.HomePage_WhatsAppPop_Frame_ID)
        return HomePage_WhatsAppPop_Frame_ID
