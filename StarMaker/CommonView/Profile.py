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
