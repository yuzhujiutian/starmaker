# coding=utf-8
# ----------
# 首页
# ----------
from StarMaker.CommonView.VData import Home_VD
from StarMaker.Utils.FindElement import find_element
from StarMaker.Utils.Tools import Popular_Elements_Disposes


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
        HomePage_MainTab_MomentTab_IDS = self.findIDS(Home_VD.HomePage_MainTab_IDS, 0)
        return HomePage_MainTab_MomentTab_IDS

    # 首页-MainTab-Party
    def HomePage_MainTab_PartyTab(self):
        HomePage_MainTab_PartyTab_IDS = self.findIDS(Home_VD.HomePage_MainTab_IDS, 1)
        return HomePage_MainTab_PartyTab_IDS

    # 首页-MainTab-Sing
    def HomePage_MainTab_SingTab(self):
        HomePage_MainTab_SingTab_IDS = self.findIDS(Home_VD.HomePage_MainTab_IDS, 2)
        return HomePage_MainTab_SingTab_IDS

    # 首页-MainTab-Message
    def HomePage_MainTab_MessageTab(self):
        HomePage_MainTab_MessageTab_IDS = self.findIDS(Home_VD.HomePage_MainTab_IDS, 3)
        return HomePage_MainTab_MessageTab_IDS

    # 首页-MainTab-Me
    def HomePage_MainTab_MeTab(self):
        HomePage_MainTab_MeTab_IDS = self.findIDS(Home_VD.HomePage_MainTab_IDS, 4)
        return HomePage_MainTab_MeTab_IDS

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
    # 首页-feed卡片-删除卡片(ID/IDS)
    def HomePage_FeedCard_Delete(self):
        HomePage_FeedCard_Delete_ID_IDS = self.ID_IDS(Home_VD.HomePage_FeedCard_Delete_ID_IDS)
        return HomePage_FeedCard_Delete_ID_IDS

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

    # 首页-feed卡片_图片(IDS)
    def HomePage_FeedCard_DIY_Img(self, cnt):
        HomePage_FeedCard_Img_ID_IDS = self.findIDS(Home_VD.HomePage_FeedCard_Img_ID_IDS, cnt)
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

    # ----------
    # Sing页面
    # ----------
    # Sing页-切换内容SingTab-界面元素
    # SIng页-sing
    def SingPage_Function_CheckSingTitle(self):
        SingPage_Function_CheckSingTitle_ID = self.findID(Home_VD.SingPage_Function_CheckSingTitle_ID)
        return SingPage_Function_CheckSingTitle_ID

    # Sing页面-搜索框
    def SingPage_Common_Search(self):
        SingPage_Common_Search_ID = self.findID(Home_VD.SingPage_Common_Search_ID)
        return SingPage_Common_Search_ID

    # Sing页面-播放器图标
    def SingPage_Common_Player(self):
        SingPage_Common_Player_ID = self.findID(Home_VD.SingPage_Common_Player_ID)
        return SingPage_Common_Player_ID

    # Sing页面-Banner
    def SingPage_Common_Banner(self):
        SingPage_Common_Banner_ClaS = self.findClaS(Home_VD.Source_SingPage_Common_Banner_ClaS, 0)
        return SingPage_Common_Banner_ClaS

    # Sing页面-中上方四个Tab([0]Free Style)
    def SingPage_TabName_FreeStyle(self):
        SingPage_TabName_FreeStyle_IDS = self.findIDS(Home_VD.SingPage_TabName_IDS, 0)
        return SingPage_TabName_FreeStyle_IDS

    # Sing页面-中上方四个Tab([1]Collab)
    def SingPage_TabName_Collab(self):
        SingPage_TabName_Collab_IDS = self.findIDS(Home_VD.SingPage_TabName_IDS, 1)
        return SingPage_TabName_Collab_IDS

    # Sing页面-中上方四个Tab([2]Daily Task)
    def SingPage_TabName_DailyTask(self):
        SingPage_TabName_DailyTask_IDS = self.findIDS(Home_VD.SingPage_TabName_IDS, 2)
        return SingPage_TabName_DailyTask_IDS

    # Sing页面-中上方四个Tab([3]My Songs)
    def SingPage_TabName_MySongs(self):
        SingPage_TabName_MySongs_IDS = self.findIDS(Home_VD.SingPage_TabName_IDS, 3)
        return SingPage_TabName_MySongs_IDS

    # Sing页面-Take the Mic
    def SingPage_Function_TakeTheMic(self):
        SingPage_Function_TakeTheMic_ID = self.findID(Home_VD.SingPage_TakeTheMic_ID)
        return SingPage_Function_TakeTheMic_ID

    # Sing页面-Vocal Talents
    def SingPage_Function_VocalTalents(self):
        SingPage_Function_VocalTalents_ID = self.findID(Home_VD.SingPage_VocalTalents_ID)
        return SingPage_Function_VocalTalents_ID

    # Sing页面-Sing Party
    def SingPage_Function_SingParty(self):
        SingPage_Function_SingParty_ID = self.findID(Home_VD.SingPage_SingParty_ID)
        return SingPage_Function_SingParty_ID

    # Sing页面-中下方四个Tab([0]Recommend)
    def SingPage_SingHeat_Recommend(self):
        SingPage_Function_SingHeat_IDS = self.findIDS(Home_VD.SingPage_SingHeat_IDS, 0)
        return SingPage_Function_SingHeat_IDS

    # Sing页面-中下方四个Tab([1]Hot)
    def SingPage_SingHeat_Hot(self):
        SingPage_SingHeat_Hot_IDS = self.findIDS(Home_VD.SingPage_SingHeat_IDS, 1)
        return SingPage_SingHeat_Hot_IDS

    # Sing页面-中下方四个Tab([2]Trending)
    def SingPage_SingHeat_Trending(self):
        SingPage_SingHeat_Trending_IDS = self.findIDS(Home_VD.SingPage_SingHeat_IDS, 2)
        return SingPage_SingHeat_Trending_IDS

    # Sing页面-中下方四个Tab([3]New)
    def SingPage_SingHeat_New(self):
        SingPage_SingHeat_New_IDS = self.findIDS(Home_VD.SingPage_SingHeat_IDS, 3)
        return SingPage_SingHeat_New_IDS

    # Sing页面-任一Tab下-第一首歌曲名
    def SingPage_CommonTab_FirstSongName(self):
        SingPage_CommonTab_FirstSongName_ID_IDS = self.ID_IDS(Home_VD.SingPage_CommonTab_FirstSongName)
        return SingPage_CommonTab_FirstSongName_ID_IDS

    # Sing页面-Recommend下的歌曲点击SING
    def SingPage_SingRecommend_SelectSing(self):
        SingPage_SingRecommend_SelectSing_IDS = self.findIDS(Home_VD.SingPage_SingRecommend_SelectSing_IDS, 0)
        return SingPage_SingRecommend_SelectSing_IDS

    # Sing页面-选择歌曲-歌曲类型Tab([0]Solo)
    def SingPage_SingRecommend_SingType_Solo(self):
        SingPage_SingRecommend_SingType_Solo_IDS = self.findIDS(Home_VD.SingPage_SingRecommend_SingType_IDS, 0)
        return SingPage_SingRecommend_SingType_Solo_IDS

    # Sing页面-选择歌曲-歌曲类型Tab([1]Join Collab)
    def SingPage_SingRecommend_SingType_JoinCollab(self):
        SingPage_SingRecommend_SingType_JoinCollab_IDS = self.findIDS(Home_VD.SingPage_SingRecommend_SingType_IDS, 1)
        return SingPage_SingRecommend_SingType_JoinCollab_IDS

    # Sing页面-选择歌曲-歌曲类型Tab([2]Start Collab)
    def SingPage_SingRecommend_SingType_StartCollab(self):
        SingPage_SingRecommend_SingType_StartCollab_IDS = self.findIDS(Home_VD.SingPage_SingRecommend_SingType_IDS, 2)
        return SingPage_SingRecommend_SingType_StartCollab_IDS

    # Sing页面-选择歌曲-歌曲类型Tab([3]Chorus)
    def SingPage_SingRecommend_SingType_Chorus(self):
        try:
            if self.findIDS(Home_VD.SingPage_SingRecommend_SingType_IDS, 3):
                return
        except:
            return False

    # ----------
    # 安全警告
    # ----------
    #允许访问  Allow
    def SingSolo_SafetyWarning_Allow(self):
        SingSolo_SafetyWarning_Allow_ClaS = self.findClaS(Home_VD.Source_SingSolo_SafetyWarning_ClaS, 0)
        return SingSolo_SafetyWarning_Allow_ClaS
    def SingSolo_SafetyWarning_TextAllow(self):
        SingSolo_SafetyWarning_TextAllow_Text = self.findAU("new UiSelector().text(\"Change the song's pitch to match your voice!\")")
        return SingSolo_SafetyWarning_TextAllow_Text


    #拒绝访问 rejection
    def SingSolo_SafetyWarning_Rejection(self):
        SingSolo_SafetyWarning_Rejection_ClaS = self.findClaS(Home_VD.Source_SingSolo_SafetyWarning_ClaS, 1)
        return SingSolo_SafetyWarning_Rejection_ClaS





    # ----------
    # Sing-Solo页面
    # ----------
    # Solo-引导信息
    def SingSolo_TipsIcon_Check(self):
        SingSolo_TipsIcon_Check_ID = self.findID(Home_VD.SingSolo_SingGuide_ID)
        return SingSolo_TipsIcon_Check_ID

    # Solo-引导信息“I KNOW” SingSolo_TipsInfo_ID
    def SingSolo_TipsIcon_CheckInfo(self):
        SingSolo_TipsIcon_CheckInfo_ID = self.findID(Home_VD.SingSolo_SingGuideConfirm_ID)
        return SingSolo_TipsIcon_CheckInfo_ID
    # Solo-工具引导信息
    def SingSolo_Tool_CheckGuide(self):
        SingSolo_Tool_CheckGuide_Text = self.findAU("new UiSelector().text(\"Change the song's pitch to match your voice!\")")
        return SingSolo_Tool_CheckGuide_Text

    # Sing页面-选择歌曲-Solo-歌曲Pitch
    def SingSolo_Function_CheckPitch_ID(self):
        SingSolo_CheckPitch_ID = self.findID(Home_VD.SingSolo_CheckPitch_ID)
        return SingSolo_CheckPitch_ID

    # Sing页面-选择歌曲-Solo-歌曲Volume
    def SingSolo_Function_ChecVolume(self):
        SingSolo_ChecVolume_ID = self.findID(Home_VD.SingSolo_ChecVolume_ID)
        return SingSolo_ChecVolume_ID

    # Sing页面-选择歌曲-Solo-歌曲Start
    def SingSolo_Function_ChecStart(self):
        SingSolo_Function_ChecStart_ID = self.findID(Home_VD.SingSolo_CheckStart_ID)
        return SingSolo_Function_ChecStart_ID

    # Sing页面-选择歌曲-Solo-歌曲Guide
    def SingSolo_Function_ChecGuide(self):
        SingSolo_Function_ChecGuide_ID = self.findID(Home_VD.SingSolo_CheckGuide_ID)
        return SingSolo_Function_ChecGuide_ID

    # Sing页面-选择歌曲-Solo-歌曲Effect
    def SingSolo_Function_CheckEffect(self):
        SingSolo_Function_CheckEffect_ID = self.findID(Home_VD.SingSolo_CheckEffect_ID)
        return SingSolo_Function_CheckEffect_ID

    # Sing页面-选择歌曲-Solo-歌曲名称
    def SingSolo_Function_SingName(self):
        SingSolo_Function_SingName_ID = self.findID(Home_VD.SingSolo_SingName_ID)
        return SingSolo_Function_SingName_ID

    # Sing页面-选择歌曲-Solo-音频和视频唱歌
    def SingSolo_Function_AudioVideo(self):
        SingSolo_Function_AudioVideo_ID = self.findID(Home_VD.SingSolo_AudioVideo_ID)
        return SingSolo_Function_AudioVideo_ID

    # Sing页面-选择歌曲-Solo-返回上一页
    def SingSolo_Function_BackPage(self):
        SingSolo_Function_BackPage_ID = self.findID(Home_VD.SingSolo_BackPage_ID)
        return SingSolo_Function_BackPage_ID

    # Sing页面-选择歌曲-Solo-播放歌曲-歌曲打分
    def SingSolo_SingRecordScore_CheckElement(self):
        SingSolo_SingRecordScore_CheckElement_ID = self.findID(Home_VD.SingSolo_SingRecordScore_ID)
        return SingSolo_SingRecordScore_CheckElement_ID

    # Sing页面-选择歌曲-Solo-播放歌曲-歌曲打分头像
    def SingSolo_SingRecordScoreImage_CheckElement(self):
        SingSolo_SingRecordScoreImage_CheckElement_ID = self.findID(Home_VD.SingSolo_SingRecordScoreImage_ID)
        return SingSolo_SingRecordScoreImage_CheckElement_ID

    # Sing页面-选择歌曲-Solo-播放歌曲-歌曲音准器（上面的抖动条）
    def SingSolo_SongTone_CheckElement(self):
        SingSolo_SongTone_CheckElement_ID = self.findID(Home_VD.SingSolo_SongTone_ID)
        return SingSolo_SongTone_CheckElement_ID


    # ----------
    # Sing-Solo页面-Pitch
    # ----------
    # Pitch界面的-pitch

    def SongTone_PitchPage_PitchTitle(self):
        SongTone_PitchPage_PitchTitle_ID = self.findID(Home_VD.SongTone_PitchPage_PitchTitle_ID)
        return SongTone_PitchPage_PitchTitle_ID

    # Pitch界面的-Close
    def SongTone_PitchPage_PitchClose(self):
        SongTone_PitchPage_PitchClose_ID = self.findID(Home_VD.SongTone_PitchPage_PitchClose_ID)
        return SongTone_PitchPage_PitchClose_ID

    # Pitch界面的-"-"(低调节)
    def SongTone_PitchPage_PitchLower(self):
        SongTone_PitchPage_PitchLower_ID = self.findID(Home_VD.SongTone_PitchPage_PitchLower_ID)
        return SongTone_PitchPage_PitchLower_ID

    # Pitch界面的-“+”（高调节）
    def SongTone_PitchPage_PitchRaise(self):
        SongTone_PitchPage_PitchRaise_ID = self.findID(Home_VD.SongTone_PitchPage_PitchRaise_ID)
        return SongTone_PitchPage_PitchRaise_ID

    # Pitch界面的-“----”（调节条）
    def SongTone_PitchPage_PitchProgressBar(self):
        SongTone_PitchPage_PitchProgressBar_ID = self.findID(Home_VD.SongTone_PitchPage_PitchProgressBar_ID)
        return SongTone_PitchPage_PitchProgressBar_ID

    # Pitch界面的-分数（调节分数）
    def SongTone_PitchPage_PitchContent(self):
        SongTone_PitchPage_PitchContent_ID = self.findID(Home_VD.SongTone_PitchPage_PitchContent_ID)
        return SongTone_PitchPage_PitchContent_ID

    # Pitch界面的-具体分数
    def SongTone_PitchPage_PitchSpecificContent(self):
        SingSolo_Tool_CheckGuide_Text = self.findAU("new UiSelector().text(\"2\")")
        return SingSolo_Tool_CheckGuide_Text

    # ----------
    # Sing-Solo页面-VOLUME
    # ----------
    # Pitch界面的-Voice
    def SongTone_VolumePage_VolumeAdjust(self):
        SongTone_VolumePage_VolumeAdjust_ID = self.findID(Home_VD.SongTone_VolumePage_VolumeAdjust_ID)
        return SongTone_VolumePage_VolumeAdjust_ID

    # Pitch界面的-Voice
    def SongTone_VolumePage_MusicAdjust(self):
        SongTone_VolumePage_MusicAdjust_ID = self.findID(Home_VD.SongTone_VolumePage_MusicAdjust_ID)
        return SongTone_VolumePage_MusicAdjust_ID
    # ----------
    # Sing-Solo页面-Effect
    # ----------
    # Effect界面的-Effect的场景效果-NONE
    def SongTone_EffectPage_NoneEffect(self):
        SongTone_EffectPage_SceneEffect_IDS = self.findIDS(Home_VD.SongTone_EffectPage_SceneEffect_IDS, 0)
        return SongTone_EffectPage_SceneEffect_IDS

    # Effect界面的-Effect的场景效果-CUSTOM
    def SongTone_EffectPage_CustomEffect(self):
        SongTone_EffectPage_CustomEffect_IDS = self.findIDS(Home_VD.SongTone_EffectPage_SceneEffect_IDS, 1)
        return SongTone_EffectPage_CustomEffect_IDS

    # Effect界面的-Effect的场景效果-HALL
    def SongTone_EffectPage_HallEffect(self):
        SongTone_EffectPage_HallEffect_IDS = self.findIDS(Home_VD.SongTone_EffectPage_SceneEffect_IDS, 2)
        return SongTone_EffectPage_HallEffect_IDS

    # Effect界面的-Effect的场景效果-PARTY
    def SongTone_EffectPage_PartyEffect(self):
        SongTone_EffectPage_PartyEffect_IDS = self.findIDS(Home_VD.SongTone_EffectPage_SceneEffect_IDS, 3)
        return SongTone_EffectPage_PartyEffect_IDS

    # Effect界面的-Effect的场景效果-DISTANT
    def SongTone_EffectPage_DistantEffect(self):
        SongTone_EffectPage_DistantEffect_IDS = self.findIDS(Home_VD.SongTone_EffectPage_SceneEffect_IDS, 4)
        return SongTone_EffectPage_DistantEffect_IDS