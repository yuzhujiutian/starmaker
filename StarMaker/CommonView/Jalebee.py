# coding=utf-8
# ----------
# Jalebee
# ----------
from StarMaker.Utils.FindElement import find_element
from StarMaker.CommonView.VData import Jalebee_VD
from StarMaker.Utils.Tools import Popular_Elements_Disposes


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

    # 首页-MainTab-Post
    def Jalebee_MainTab_Post(self):
        Jalebee_MainTab_Post_ID = self.findID(Jalebee_VD.Jalebee_MainTab_Post_ID)
        return Jalebee_MainTab_Post_ID

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

    # ----------
    # JalebeeFollowing页
    # ----------
    # JalebeeFollowing页-发布-发布进度条
    def JalebeeFollowingPage_PublishBar(self):
        JalebeeFollowingPage_PublishBar_ID = self.findID(Jalebee_VD.JalebeeFollowingPage_PublishBar_ID)
        return JalebeeFollowingPage_PublishBar_ID

    # JalebeeFollowing页-作品Like按钮
    def JalebeeFollowingPage_ShootLikeBtn(self):
        JalebeeFollowingPage_ShootLikeBtn_ID_IDS = self.ID_IDS(Jalebee_VD.JalebeeFollowingPage_ShootLikeBtn_ID_IDS)
        return JalebeeFollowingPage_ShootLikeBtn_ID_IDS

    # JalebeeFollowing页-作品like数(NoLike_text=लाइक करें)
    def JalebeeFollowingPage_ShootLikeNum(self):
        JalebeeFollowingPage_ShootLikeNum_ID_IDS = self.ID_IDS(Jalebee_VD.JalebeeFollowingPage_ShootLikeNum_ID_IDS)
        return JalebeeFollowingPage_ShootLikeNum_ID_IDS

    # JalebeeFollowing页-作品like数(用于统计)
    def JalebeeFollowingPage_ShootLikeNumS_Count(self):
        JalebeeFollowingPage_ShootLikeNum_ID_IDS = self.ID_IDS_Count(Jalebee_VD.JalebeeFollowingPage_ShootLikeNum_ID_IDS)
        return JalebeeFollowingPage_ShootLikeNum_ID_IDS

    # JalebeeFollowing页-首个作品
    def JalebeeFollowingPage_FirstShoot(self):
        JalebeeFollowingPage_FirstShoot_ID_IDS = self.ID_IDS(Jalebee_VD.JalebeeFollowingPage_FirstShoot_ID_IDS)
        return JalebeeFollowingPage_FirstShoot_ID_IDS

    # ----------
    # Jalebee-Party页
    # ----------
    # Jalebee-Party页-Title
    def JalebeePartyPage_Title_Text(self):
        JalebeePartyPage_Title_Text_ID = self.findID(Jalebee_VD.JalebeePartyPage_Title_Text_ID)
        return JalebeePartyPage_Title_Text_ID

    # Jalebee-Party页-MyRoom("मेरा रूम")
    def JalebeePartyPage_MyRoom_Text(self):
        JalebeePartyPage_MyRoom_History_Text_IDS = self.findIDS(Jalebee_VD.JalebeePartyPage_MyRoom_History_Text_IDS, 0)
        return JalebeePartyPage_MyRoom_History_Text_IDS

    # Jalebee-Party页-History("इतिहास")
    def JalebeePartyPage_History_Text(self):
        JalebeePartyPage_MyRoom_History_Text_IDS = self.findIDS(Jalebee_VD.JalebeePartyPage_MyRoom_History_Text_IDS, 1)
        return JalebeePartyPage_MyRoom_History_Text_IDS

    # Jalebee-Party页-首个房间
    def JalebeePartyPage_KTVRoom_FirstRoom(self):
        JalebeePartyPage_MyRoom_History_Text_IDS = self.findIDS(Jalebee_VD.JalebeePartyPage_MyRoom_History_Text_IDS, 2)
        return JalebeePartyPage_MyRoom_History_Text_IDS

    # Jalebee-Party页-第二个房间
    def JalebeePartyPage_KTVRoom_SecondRoom(self):
        JalebeePartyPage_MyRoom_History_Text_IDS = self.findIDS(Jalebee_VD.JalebeePartyPage_MyRoom_History_Text_IDS, 3)
        return JalebeePartyPage_MyRoom_History_Text_IDS

    # Jalebee-Party页-Search
    def JalebeePartyPage_Search_Btn(self):
        JalebeePartyPage_Search_Btn_ID = self.findID(Jalebee_VD.JalebeePartyPage_Search_Btn_ID)
        return JalebeePartyPage_Search_Btn_ID

    # ----------
    # Jalebee-拍摄页
    # ----------
    # Jalebee-拍摄页-选择音乐引导(首次进入时显示，该元素为单独一个页面，遮挡其他元素)
    def JalebeeShootingPage_Function_AddMusicGuide(self):
        JalebeeShootingPage_Function_AddMusicGuide_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_AddMusicGuide_ID)
        return JalebeeShootingPage_Function_AddMusicGuide_ID

    # Jalebee-拍摄页-Start按钮
    def JalebeeShootingPage_Function_StartBtn(self):
        JalebeeShootingPage_Function_StartBtn_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_StartBtn_ID)
        return JalebeeShootingPage_Function_StartBtn_ID

    # Jalebee-拍摄页-进度条
    def JalebeeShootingPage_Function_ProgressBar(self):
        JalebeeShootingPage_Function_ProgressBar_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_ProgressBar_ID)
        return JalebeeShootingPage_Function_ProgressBar_ID

    # Jalebee-拍摄页-关闭按钮
    def JalebeeShootingPage_Function_CloseBtn(self):
        JalebeeShootingPage_Function_CloseBtn_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_CloseBtn_ID)
        return JalebeeShootingPage_Function_CloseBtn_ID

    # Jalebee-拍摄页-音乐icon
    def JalebeeShootingPage_Function_MusicIcon(self):
        JalebeeShootingPage_Function_MusicIcon_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_MusicIcon_ID)
        return JalebeeShootingPage_Function_MusicIcon_ID

    # Jalebee-拍摄页-当前选择音乐
    def JalebeeShootingPage_Function_MusicName(self):
        JalebeeShootingPage_Function_MusicName_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_MusicName_ID)
        return JalebeeShootingPage_Function_MusicName_ID

    # Jalebee-拍摄页-取消已选择音乐
    def JalebeeShootingPage_Function_DeselectedMusic(self):
        JalebeeShootingPage_Function_DeselectedMusic_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_DeselectedMusic_ID)
        return JalebeeShootingPage_Function_DeselectedMusic_ID

    # Jalebee-拍摄页-手电筒
    def JalebeeShootingPage_Function_Flashlight(self):
        JalebeeShootingPage_Function_Flashlight_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_Flashlight_ID)
        return JalebeeShootingPage_Function_Flashlight_ID

    # Jalebee-拍摄页-切换摄像头
    def JalebeeShootingPage_Function_SwitchingCamera(self):
        JalebeeShootingPage_Function_SwitchingCamera_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_SwitchingCamera_ID)
        return JalebeeShootingPage_Function_SwitchingCamera_ID

    # Jalebee-拍摄页-美颜
    def JalebeeShootingPage_Function_Beauty(self):
        JalebeeShootingPage_Function_Beauty_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_Beauty_ID)
        return JalebeeShootingPage_Function_Beauty_ID

    # Jalebee-拍摄页-滤镜
    def JalebeeShootingPage_Function_Filter(self):
        JalebeeShootingPage_Function_Filter_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_Filter_ID)
        return JalebeeShootingPage_Function_Filter_ID

    # Jalebee-拍摄页-相册
    def JalebeeShootingPage_Function_Album(self):
        JalebeeShootingPage_Function_Album_ID = self.findID(Jalebee_VD.JalebeeShootingPage_Function_Album_ID)
        return JalebeeShootingPage_Function_Album_ID

    # Jalebee-拍摄页-拍摄模式-Photo
    def JalebeeShootingPage_Function_ShootingMode_Photo(self):
        JalebeeShootingPage_Function_ShootingMode_IDS = self.findIDS(Jalebee_VD.JalebeeShootingPage_Function_ShootingMode_IDS, 0)
        return JalebeeShootingPage_Function_ShootingMode_IDS

    # Jalebee-拍摄页-拍摄模式-15S
    def JalebeeShootingPage_Function_ShootingMode_15S(self):
        JalebeeShootingPage_Function_ShootingMode_IDS = self.findIDS(Jalebee_VD.JalebeeShootingPage_Function_ShootingMode_IDS, 1)
        return JalebeeShootingPage_Function_ShootingMode_IDS

    # Jalebee-拍摄页-拍摄模式-60S
    def JalebeeShootingPage_Function_ShootingMode_60S(self):
        JalebeeShootingPage_Function_ShootingMode_IDS = self.findIDS(Jalebee_VD.JalebeeShootingPage_Function_ShootingMode_IDS, 2)
        return JalebeeShootingPage_Function_ShootingMode_IDS

    # ----------
    # Jalebee-音乐选择页
    # ----------
    # Jalebee-音乐选择页-Title
    def JalebeeSelectMusicPage_Title(self):
        JalebeeSelectMusicPage_Title_ID = self.findID(Jalebee_VD.JalebeeSelectMusicPage_Title_ID)
        return JalebeeSelectMusicPage_Title_ID

    # Jalebee-音乐选择页-Close
    def JalebeeSelectMusicPage_Function_Close(self):
        JalebeeSelectMusicPage_Function_Close_ID = self.findID(Jalebee_VD.JalebeeSelectMusicPage_Function_Close_ID)
        return JalebeeSelectMusicPage_Function_Close_ID

    # Jalebee-音乐选择页-Search
    def JalebeeSelectMusicPage_Function_Search(self):
        JalebeeSelectMusicPage_Function_Search_ID = self.findID(Jalebee_VD.JalebeeSelectMusicPage_Function_Search_ID)
        return JalebeeSelectMusicPage_Function_Search_ID

    # Jalebee-音乐选择页-内容Tab-推荐页EXPLORE
    def JalebeeSelectMusicPage_FeedTab_Explore(self):
        JalebeeSelectMusicPage_FeedTab_Common_IDS = self.findIDS(Jalebee_VD.JalebeeSelectMusicPage_FeedTab_Common_IDS, 0)
        return JalebeeSelectMusicPage_FeedTab_Common_IDS

    # Jalebee-音乐选择页-内容Tab-收藏页FAVORITE
    def JalebeeSelectMusicPage_FeedTab_Favorite(self):
        JalebeeSelectMusicPage_FeedTab_Common_IDS = self.findIDS(Jalebee_VD.JalebeeSelectMusicPage_FeedTab_Common_IDS, 1)
        return JalebeeSelectMusicPage_FeedTab_Common_IDS

    # Jalebee-音乐选择页-Category
    def JalebeeSelectMusicPage_Function_Category(self, num=0):
        JalebeeSelectMusicPage_Function_Category_IDS = self.findIDS(Jalebee_VD.JalebeeSelectMusicPage_Function_Category_IDS, num)
        return JalebeeSelectMusicPage_Function_Category_IDS

    # Jalebee-音乐选择页-音乐名
    def JalebeeSelectMusicPage_Function_SongsName(self, num=0):
        JalebeeSelectMusicPage_Function_SongsName_IDS = self.findIDS(Jalebee_VD.JalebeeSelectMusicPage_Function_SongsName_IDS, num)
        return JalebeeSelectMusicPage_Function_SongsName_IDS

    # Jalebee-音乐选择页-收藏
    def JalebeeSelectMusicPage_Function_Favor(self, num=0):
        JalebeeSelectMusicPage_Function_Favor_IDS = self.findIDS(Jalebee_VD.JalebeeSelectMusicPage_Function_Favor_IDS, num)
        return JalebeeSelectMusicPage_Function_Favor_IDS

    # Jalebee-音乐选择页-确认选择
    def JalebeeSelectMusicPage_Function_USE(self):
        JalebeeSelectMusicPage_Function_USE_ID = self.findID(Jalebee_VD.JalebeeSelectMusicPage_Function_USE_ID)
        return JalebeeSelectMusicPage_Function_USE_ID

    # ----------
    # Jalebee-发布预览页
    # ----------
    # Jalebee-发布预览页-进度条
    def JalebeePostPreviewPage_Function_ProgressBar(self):
        JalebeePostPreviewPage_Function_ProgressBar_ID = self.findID(Jalebee_VD.JalebeePostPreviewPage_Function_ProgressBar_ID)
        return JalebeePostPreviewPage_Function_ProgressBar_ID

    # Jalebee-发布预览页-返回
    def JalebeePostPreviewPage_Function_Back(self):
        JalebeePostPreviewPage_Function_Back_ID = self.findID(Jalebee_VD.JalebeePostPreviewPage_Function_Back_ID)
        return JalebeePostPreviewPage_Function_Back_ID

    # Jalebee-发布预览页-Volume
    def JalebeePostPreviewPage_Function_Volume(self):
        JalebeePostPreviewPage_Function_Other_ClaS = self.findClaS(
            Jalebee_VD.JalebeePostPreviewPage_Function_Other_ClaS, 1)
        return JalebeePostPreviewPage_Function_Other_ClaS

    # Jalebee-发布预览页-Cut Music
    def JalebeePostPreviewPage_Function_CutMusic(self):
        JalebeePostPreviewPage_Function_Other_ClaS = self.findClaS(
            Jalebee_VD.JalebeePostPreviewPage_Function_Other_ClaS, 2)
        return JalebeePostPreviewPage_Function_Other_ClaS

    # Jalebee-发布预览页-Select Music
    def JalebeePostPreviewPage_Function_SelectMusic(self):
        JalebeePostPreviewPage_Function_Other_ClaS = self.findClaS(
            Jalebee_VD.JalebeePostPreviewPage_Function_Other_ClaS, 3)
        return JalebeePostPreviewPage_Function_Other_ClaS

    # Jalebee-发布预览页-Cover
    def JalebeePostPreviewPage_Function_Cover(self):
        JalebeePostPreviewPage_Function_Other_ClaS = self.findClaS(
            Jalebee_VD.JalebeePostPreviewPage_Function_Other_ClaS, 4)
        return JalebeePostPreviewPage_Function_Other_ClaS

    # Jalebee-发布预览页-Next
    def JalebeePostPreviewPage_Function_Next(self):
        JalebeePostPreviewPage_Function_Next_ID = self.findID(Jalebee_VD.JalebeePostPreviewPage_Function_Next_ID)
        return JalebeePostPreviewPage_Function_Next_ID

    # ----------
    # Jalebee-发布编辑页
    # ----------
    # Jalebee-发布编辑页-Title(text=पोस्ट करें)
    def JalebeePostEditPage_Title(self):
        JalebeePostEditPage_Title_ID = self.findID(Jalebee_VD.JalebeePostEditPage_Title_ID)
        return JalebeePostEditPage_Title_ID

    # Jalebee-发布编辑页-返回
    def JalebeePostEditPage_Function_Back(self):
        JalebeePostEditPage_Function_Back_Cla = self.findCla(Jalebee_VD.JalebeePostEditPage_Function_Back_Cla)
        return JalebeePostEditPage_Function_Back_Cla

    # Jalebee-发布编辑页-输入文字(text=आपके दिमाग मे क्या है?)
    def JalebeePostEditPage_Function_MindWriting(self):
        JalebeePostEditPage_Function_MindWriting_ID = self.findID(Jalebee_VD.JalebeePostEditPage_Function_MindWriting_ID)
        return JalebeePostEditPage_Function_MindWriting_ID

    # Jalebee-发布编辑页-更换封面
    def JalebeePostEditPage_Function_SetCover(self):
        JalebeePostEditPage_Function_SetCover_ID = self.findID(Jalebee_VD.JalebeePostEditPage_Function_SetCover_ID)
        return JalebeePostEditPage_Function_SetCover_ID

    # Jalebee-发布编辑页-@好友
    def JalebeePostEditPage_Function_RemindFriends(self):
        JalebeePostEditPage_Function_RemindFriends_ID = self.findID(Jalebee_VD.JalebeePostEditPage_Function_RemindFriends_ID)
        return JalebeePostEditPage_Function_RemindFriends_ID

    # Jalebee-发布编辑页-Topic
    def JalebeePostEditPage_Function_Topic(self):
        JalebeePostEditPage_Function_Topic_ID = self.findID(Jalebee_VD.JalebeePostEditPage_Function_Topic_ID)
        return JalebeePostEditPage_Function_Topic_ID

    # Jalebee-发布编辑页-定位
    def JalebeePostEditPage_Function_Location(self):
        JalebeePostEditPage_Function_Location_ID = self.findID(Jalebee_VD.JalebeePostEditPage_Function_Location_ID)
        return JalebeePostEditPage_Function_Location_ID

    # Jalebee-发布编辑页-保存草稿
    def JalebeePostEditPage_Function_Draft(self):
        JalebeePostEditPage_Function_Draft_ID = self.findID(Jalebee_VD.JalebeePostEditPage_Function_Draft_ID)
        return JalebeePostEditPage_Function_Draft_ID

    # Jalebee-发布编辑页-发布
    def JalebeePostEditPage_Function_Post(self):
        JalebeePostEditPage_Function_Post_ID = self.findID(Jalebee_VD.JalebeePostEditPage_Function_Post_ID)
        return JalebeePostEditPage_Function_Post_ID

    # ----------
    # Jalebee-消息页
    # ----------
    # Jalebee-消息页-功能区-System(text=सिस्टम)
    def JalebeeMessagePage_Function_System(self):
        JalebeeMessagePage_FunctionCommon_IDS = self.findIDS(Jalebee_VD.JalebeeMessagePage_FunctionCommon_IDS, 0)
        return JalebeeMessagePage_FunctionCommon_IDS

    # Jalebee-消息页-功能区-Gifts(text=उपहार प्राप्त)
    def JalebeeMessagePage_Function_Gifts(self):
        JalebeeMessagePage_FunctionCommon_IDS = self.findIDS(Jalebee_VD.JalebeeMessagePage_FunctionCommon_IDS, 1)
        return JalebeeMessagePage_FunctionCommon_IDS

    # Jalebee-消息页-功能区-Messages(text=संदेश)
    def JalebeeMessagePage_Function_Messages(self):
        JalebeeMessagePage_FunctionCommon_IDS = self.findIDS(Jalebee_VD.JalebeeMessagePage_FunctionCommon_IDS, 2)
        return JalebeeMessagePage_FunctionCommon_IDS

    # Jalebee-消息页-内容Tab-FOLLOWING
    def JalebeeMessagePage_FeedTab_FOLLOWING(self):
        JalebeeMessagePage_FeedTabCommon_IDS = self.findIDS(Jalebee_VD.JalebeeMessagePage_FeedTabCommon_IDS, 0)
        return JalebeeMessagePage_FeedTabCommon_IDS

    # Jalebee-消息页-内容Tab-YOU
    def JalebeeMessagePage_FeedTab_YOU(self):
        JalebeeMessagePage_FeedTabCommon_IDS = self.findIDS(Jalebee_VD.JalebeeMessagePage_FeedTabCommon_IDS, 1)
        return JalebeeMessagePage_FeedTabCommon_IDS

    # Jalebee-消息页-消息内容
    def JalebeeMessagePage_MessageContent(self):
        JalebeeMessagePage_MessageContent_ID_IDS = self.ID_IDS(Jalebee_VD.JalebeeMessagePage_MessageContent_ID_IDS)
        return JalebeeMessagePage_MessageContent_ID_IDS

    # ----------
    # Jalebee-播放详情页
    # ----------
    # Jalebee-播放详情页-作者名
    def JalebeePlayDetailsPage_AuthorInfo_AuthorName(self):
        JalebeePlayDetailsPage_AuthorInfo_AuthorName_ID = self.findID(Jalebee_VD.JalebeePlayDetailsPage_AuthorInfo_AuthorName_ID)
        return JalebeePlayDetailsPage_AuthorInfo_AuthorName_ID

    # Jalebee-播放详情页-返回
    def JalebeePlayDetailsPage_Function_Back(self):
        JalebeePlayDetailsPage_Function_Back_ID = self.findID(Jalebee_VD.JalebeePlayDetailsPage_Function_Back_ID)
        return JalebeePlayDetailsPage_Function_Back_ID
