# coding=utf-8
# ----------
# 个人页
# ----------
from Utils.FindElement import find_element
from CommonView.VData import Profile_VD


# 个人页
class Profile(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findAU = find_element().AU

    # 用户头像
    def Profile_HeadView(self):
        Profile_HeadView_ID = self.findID(Profile_VD.Profile_HeadView_ID)
        return Profile_HeadView_ID

    # 用户昵称
    def Profile_StageName(self):
        Profile_StageName_ID = self.findID(Profile_VD.Profile_StageName_ID)
        return Profile_StageName_ID

    # 用户等级
    def Profile_UserLevel(self):
        Profile_UserLevel_ID = self.findID(Profile_VD.Profile_UserLevel_ID)
        return Profile_UserLevel_ID

    # 用户VIP状态(text=Vip/Get Vip)
    def Profile_VIPLevel(self):
        Profile_VIPLevel_ID = self.findID(Profile_VD.Profile_VIPLevel_ID)
        return Profile_VIPLevel_ID

    # 用户Followers数
    def Profile_FollowersNumber(self):
        Profile_FollowersNumber_ID = self.findID(Profile_VD.Profile_FollowersNumber_ID)
        return Profile_FollowersNumber_ID

    # 用户Following数
    def Profile_FollowingNumber(self):
        Profile_FollowingNumber_ID = self.findID(Profile_VD.Profile_FollowingNumber_ID)
        return Profile_FollowingNumber_ID

    # 用户上榜作品数
    def Profile_RankRecords(self):
        Profile_RankRecords_ID = self.findID(Profile_VD.Profile_RankRecords_ID)
        return Profile_RankRecords_ID

    # 功能栏
    def Profile_FunctionBar(self):
        Profile_FunctionBar_IDS = Profile_VD.Profile_FunctionBar_IDS
        return Profile_FunctionBar_IDS

    # Tab栏
    def Profile_TabBar(self):
        Profile_TabBar_IDS = Profile_VD.Profile_TabBar_IDS
        return Profile_TabBar_IDS

    # ----------
    # Tab——PROFILE
    # ----------

    # 【Personal info】个人信息
    # 个人信息Title(text=Personal info)
    def PersonalInfo_Title(self):
        PersonalInfo_Title_ID = self.findID(Profile_VD.PersonalInfo_Title_ID)
        return PersonalInfo_Title_ID

    # 个人信息内容(text=Bio: Welcome to my stage🎤)
    def PersonalInfo_desc(self):
        PersonalInfo_desc_ID = self.findID(Profile_VD.PersonalInfo_desc_ID)
        return PersonalInfo_desc_ID

    # 【Album】专辑
    # 专辑Title(text=Album)
    def Album_Title(self):
        Album_Title_ID = self.findID(Profile_VD.Album_Title_ID)
        return Album_Title_ID

    # 专辑图片（count -1 = 实际图片数量）
    def Album_Photo(self):
        Album_Photo_Cla = self.findCla(Profile_VD.Album_Photo_ClaS)
        return Album_Photo_Cla

    # 【Top Fans】收到的星光排行
    # 星光榜Title(text=Top Fans)
    def TopFans_Title(self):
        TopFans_Title_ID = self.findID(Profile_VD.TopFans_Title_ID)
        return TopFans_Title_ID

    # 星光值（text=16）
    def Starlight(self):
        Starlight_ID = self.findID(Profile_VD.Starlight_ID)
        return Starlight_ID

    # TopFans头像
    def TopFans_FindFirstHeadView(self):
        try:
            self.findID(Profile_VD.TopFans_First_ID)
            return True
        # 否则返回False
        except:
            return False

    def TopFans_FindSecondHeadView(self):
        try:
            self.findID(Profile_VD.TopFans_Second_ID)
            return True
        # 否则返回False
        except:
            return False

    def TopFans_FindThirdHeadView(self):
        try:
            self.findID(Profile_VD.TopFans_Third_ID)
            return True
        # 否则返回False
        except:
            return False

    # 【Contribute】送出的金币统计
    # 送礼榜Title(text=Contribute)
    def Contribute_Title(self):
        Contribute_Title_AU = self.findAU(Profile_VD.Contribute_Title_AU)
        return Contribute_Title_AU

    # 送礼榜金币数
    def Contribute_Gold(self):
        Contribute_Gold_ID = self.findID(Profile_VD.Contribute_Gold_ID)
        return Contribute_Gold_ID

    # 【Store】商城
    # 商城Title(text=Store)
    def Store_Title(self):
        Store_Title_ID = self.findID(Profile_VD.Store_Title_ID)
        return Store_Title_ID
