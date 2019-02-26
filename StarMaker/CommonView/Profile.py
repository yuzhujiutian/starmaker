# coding=utf-8
# ----------
# 个人页
# ----------
from Utils.FindElement import find_element
from Utils.Tools import Popular_Elements_Disposes
from CommonView.VData import Profile_VD


# 个人页
class Profile(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findAU = find_element().AU
        self.ID_IDS = Popular_Elements_Disposes().ID_IDS

    # ----------
    # 个人页
    # ----------
    # 个人页-Title
    def ProfilePage_Title(self):
        ProfilePage_Title_ID = self.findID(Profile_VD.ProfilePage_Title_ID)
        return ProfilePage_Title_ID

    # ----------
    # 个人页-个人信息
    # ----------
    # 个人页-个人信息-背景图
    def ProfilePage_UserInfo_Background(self):
        ProfilePage_UserInfo_Background_ID = self.findID(Profile_VD.ProfilePage_UserInfo_Background_ID)
        return ProfilePage_UserInfo_Background_ID

    # 个人页-个人信息-用户头像(同Moments头像同ID)
    def ProfilePage_UserInfo_HeadView(self):
        ProfilePage_UserInfo_HeadView_ID_IDS = self.ID_IDS(Profile_VD.ProfilePage_UserInfo_HeadView_ID_IDS)
        return ProfilePage_UserInfo_HeadView_ID_IDS

    # 个人页-个人信息-用户昵称(同Moments昵称同ID)
    def ProfilePage_UserInfo_StageName(self):
        ProfilePage_UserInfo_StageName_ID_IDS = self.findID(Profile_VD.ProfilePage_UserInfo_StageName_ID_IDS)
        return ProfilePage_UserInfo_StageName_ID_IDS

    # 用户等级
    def ProfilePage_UserInfo_UserLevel(self):
        ProfilePage_UserInfo_UserLevel_ID = self.findID(Profile_VD.ProfilePage_UserInfo_UserLevel_ID)
        return ProfilePage_UserInfo_UserLevel_ID

    # 用户VIP状态(text=Vip/Get Vip)
    def ProfilePag_UserInfo_VIPLevel(self):
        ProfilePag_UserInfo_VIPLevel_ID = self.findID(Profile_VD.ProfilePag_UserInfo_VIPLevel_ID)
        return ProfilePag_UserInfo_VIPLevel_ID

    # 用户Followers数
    def ProfilePage_UserInfo_FollowersNumber(self):
        ProfilePage_UserInfo_FollowersNumber_ID = self.findID(Profile_VD.ProfilePage_UserInfo_FollowersNumber_ID)
        return ProfilePage_UserInfo_FollowersNumber_ID

    # 用户Following数
    def ProfilePage_UserInfo_FollowingNumber(self):
        ProfilePage_UserInfo_FollowingNumber_ID = self.findID(Profile_VD.ProfilePage_UserInfo_FollowingNumber_ID)
        return ProfilePage_UserInfo_FollowingNumber_ID

    # 功能栏(用于校验)
    def ProfilePage_CheckList_FunctionBar(self):
        ProfilePage_CheckList_FunctionBar_IDS = Profile_VD.ProfilePage_CheckList_FunctionBar_IDS
        return ProfilePage_CheckList_FunctionBar_IDS

    # Tab栏(用于校验)([0]PROFILE/[1]MOMENTS)
    def ProfilePage_CheckList_TabBar(self):
        ProfilePage_CheckList_TabBar_IDS = Profile_VD.ProfilePage_CheckList_TabBar_IDS
        return ProfilePage_CheckList_TabBar_IDS

    # Profile-Tab
    def ProfilePage_Tab_ProfileTab(self):
        ProfilePage_Tab_ProfileTab_IDS = self.findIDS(Profile_VD.ProfilePage_CheckList_TabBar_IDS, 0)
        return ProfilePage_Tab_ProfileTab_IDS

    # Moments-Tab
    def ProfilePage_Tab_MomentsTab(self):
        ProfilePage_Tab_MomentsTab_IDS = self.findIDS(Profile_VD.ProfilePage_CheckList_TabBar_IDS, 1)
        return ProfilePage_Tab_MomentsTab_IDS

    # ----------
    # Tab——PROFILE
    # ----------
    # 【Personal info】个人信息
    # 个人信息Title(text=Personal info)
    def ProfilePage_ProfileTab_PersonalInfo_Text(self):
        ProfilePage_ProfileTab_PersonalInfo_Text_ID = self.findID(Profile_VD.ProfilePage_ProfileTab_PersonalInfo_Text_ID)
        return ProfilePage_ProfileTab_PersonalInfo_Text_ID

    # 个人信息内容
    def ProfilePage_ProfileTab_PersonalInfo_Desc(self):
        ProfilePage_ProfileTab_PersonalInfo_Desc_ID = self.findID(Profile_VD.ProfilePage_ProfileTab_PersonalInfo_Desc_ID)
        return ProfilePage_ProfileTab_PersonalInfo_Desc_ID

    # 【Album】专辑
    # 专辑Title(text=Album)
    def ProfilePage_ProfileTab_Album_Text(self):
        ProfilePage_ProfileTab_Album_Text_ID = self.findID(Profile_VD.ProfilePage_ProfileTab_Album_Text_ID)
        return ProfilePage_ProfileTab_Album_Text_ID

    # 专辑图片（count = 实际图片数量）
    def ProfilePage_ProfileTab_Album_Photos(self):
        ProfilePage_ProfileTab_Album_Photos_ID_IDS = self.ID_IDS(Profile_VD.ProfilePage_ProfileTab_Album_Photos_ID_IDS)
        return ProfilePage_ProfileTab_Album_Photos_ID_IDS

    # 专辑图片统计
    def ProfilePage_ProfileTab_Album_PhotosCount(self):
        ProfilePage_ProfileTab_Album_Photos_IDS = Profile_VD.ProfilePage_ProfileTab_Album_Photos_ID_IDS
        return ProfilePage_ProfileTab_Album_Photos_IDS

    # 【Top Fans】收到的星光排行
    # 星光榜Title(text=Top Fans)
    def ProfilePage_ProfileTab_TopFans_Text(self):
        ProfilePage_ProfileTab_TopFans_Text_ID = self.findID(Profile_VD.ProfilePage_ProfileTab_TopFans_Text_ID)
        return ProfilePage_ProfileTab_TopFans_Text_ID

    # 星光值（text=16）
    def ProfilePage_ProfileTab_TopFans_Starlight(self):
        ProfilePage_ProfileTab_TopFans_Starlight_ID = self.findID(Profile_VD.ProfilePage_ProfileTab_TopFans_Starlight_ID)
        return ProfilePage_ProfileTab_TopFans_Starlight_ID

    # TopFans头像
    def ProfilePage_ProfileTab_TopFans_FindFirstHeadView(self):
        try:
            self.findID(Profile_VD.ProfilePage_ProfileTab_TopFans_First_ID)
            return True
        # 否则返回False
        except:
            return False

    def ProfilePage_ProfileTab_TopFans_FindSecondHeadView(self):
        try:
            self.findID(Profile_VD.ProfilePage_ProfileTab_TopFans_Second_ID)
            return True
        # 否则返回False
        except:
            return False

    def ProfilePage_ProfileTab_TopFans_FindThirdHeadView(self):
        try:
            self.findID(Profile_VD.ProfilePage_ProfileTab_TopFans_Third_ID)
            return True
        # 否则返回False
        except:
            return False

    # 【Contribute】送出的金币统计
    # 送礼榜Title(text=Contribute)
    def ProfilePage_ProfileTab_Contribute_Text(self):
        ProfilePage_ProfileTab_Contribute_Text_AU = self.findAU(Profile_VD.ProfilePage_ProfileTab_Contribute_Text_AU)
        return ProfilePage_ProfileTab_Contribute_Text_AU

    # 送礼榜金币数
    def ProfilePage_ProfileTab_Contribute_Gold(self):
        ProfilePage_ProfileTab_Contribute_Gold_ID = self.findID(Profile_VD.ProfilePage_ProfileTab_Contribute_Gold_ID)
        return ProfilePage_ProfileTab_Contribute_Gold_ID

    # 【Store】商城
    # 商城Title(text=Store)
    def ProfilePage_ProfileTab_Store_Text(self):
        ProfilePage_ProfileTab_Store_Text_ID = self.findID(Profile_VD.ProfilePage_ProfileTab_Store_Text_ID)
        return ProfilePage_ProfileTab_Store_Text_ID

    # ----------
    # Tab——Moments
    # ----------
    # 作品统计(text=Total Moments(9))
    def ProfilePage_MomentsTab_CountNum(self):
        ProfilePage_MomentsTab_CountNum_ID = self.findID(Profile_VD.ProfilePage_MomentsTab_CountNum_ID)
        return ProfilePage_MomentsTab_CountNum_ID

    # 私密标签（text=Private）
    def ProfilePage_MomentsTab_ShootInfo_Private(self):
        ProfilePage_MomentsTab_ShootInfo_Private_ID_IDS = self.ID_IDS(Profile_VD.ProfilePage_MomentsTab_ShootInfo_Private_ID_IDS)
        return ProfilePage_MomentsTab_ShootInfo_Private_ID_IDS

    # 发布时间
    def ProfilePage_MomentsTab_ShootInfo_PostTime(self):
        ProfilePage_MomentsTab_ShootInfo_PostTime_ID_IDS = self.ID_IDS(Profile_VD.ProfilePage_MomentsTab_ShootInfo_PostTime_ID_IDS)
        return ProfilePage_MomentsTab_ShootInfo_PostTime_ID_IDS

    # More按钮
    def ProfilePage_MomentsTab_ShootInfo_More(self):
        ProfilePage_MomentsTab_ShootInfo_More_ID_IDS = self.ID_IDS(Profile_VD.ProfilePage_MomentsTab_ShootInfo_More_ID_IDS)
        return ProfilePage_MomentsTab_ShootInfo_More_ID_IDS

    # Like
    def ProfilePage_MomentsTab_ShootInfo_Like(self):
        ProfilePage_MomentsTab_ShootInfo_Like_ID_IDS = self.ID_IDS(Profile_VD.ProfilePage_MomentsTab_ShootInfo_Like_ID_IDS)
        return ProfilePage_MomentsTab_ShootInfo_Like_ID_IDS

    # Comment
    def ProfilePage_MomentsTab_ShootInfo_Comment(self):
        ProfilePage_MomentsTab_ShootInfo_Comment_ID_IDS = self.ID_IDS(Profile_VD.ProfilePage_MomentsTab_ShootInfo_Comment_ID_IDS)
        return ProfilePage_MomentsTab_ShootInfo_Comment_ID_IDS

    # Share
    def ProfilePage_MomentsTab_ShootInfo_Share(self):
        ProfilePage_MomentsTab_ShootInfo_Share_ID_IDS = self.ID_IDS(Profile_VD.ProfilePage_MomentsTab_ShootInfo_Share_ID_IDS)
        return ProfilePage_MomentsTab_ShootInfo_Share_ID_IDS


    # # ----------
    # # Tab——POST
    # # ----------
    #
    # # Posts Count(text=12 Posts)
    # def PostsCount(self):
    #     PostsCount_ID = self.findID(Profile_VD.PostsCount_ID)
    #     return PostsCount_ID
    #
    # # Posts 作品名称([1]第一个作品名/[2]第二个作品名)
    # def PostsName_First(self):
    #     PostsName_IDS = self.findIDS(Profile_VD.PostsName_IDS, 1)
    #     return PostsName_IDS
    #
    # # Posts Repost
    # def RepostBtn(self):
    #     RepostBtn_ID = self.findID(Profile_VD.RepostBtn_ID)
    #     return RepostBtn_ID
    #
    # # Posts Share
    # def ShareBtn(self):
    #     ShareBtn_ID = self.findID(Profile_VD.ShareBtn_ID)
    #     return ShareBtn_ID
    #
    # # Share——Copy Link(倒数第二个)
    # def CopyLink(self):
    #     CopyLink_ClaS = self.findClaS(Profile_VD.CopyLink_ClaS, -2)
    #     return CopyLink_ClaS
    #
    # def Profile_FollowersEnter(self):
    #     # 找到登录成功之后me页面的followers入口元素
    #     Profile_FollowersEnter_Text = self.findAU("new UiSelector().text(\"Followers\")")
    #     return Profile_FollowersEnter_Text