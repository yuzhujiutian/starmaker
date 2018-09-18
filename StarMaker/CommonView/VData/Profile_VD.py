# coding=utf-8
from Utils import Tools
package = Tools.Tools().package()
FindSource = Tools.Tools().FindSource
# ----------
# 个人页
# ----------

# 用户头像
Source_Profile_HeadView_ID = "civ_head_view"
Profile_HeadView_ID = package + FindSource(Source_Profile_HeadView_ID)

# 用户昵称
Source_Profile_StageName_ID = "user_name_view_tv_name"
Profile_StageName_ID = package + FindSource(Source_Profile_StageName_ID)

# 用户等级
Source_Profile_UserLevel_ID = "user_name_view_tv_level"
Profile_UserLevel_ID = package + FindSource(Source_Profile_UserLevel_ID)

# 用户VIP状态(text=Vip/Get Vip)
Source_Profile_VIPLevel_ID = "user_name_view_tv_vip_level"
Profile_VIPLevel_ID = package + FindSource(Source_Profile_VIPLevel_ID)

# 用户Followers数
Source_Profile_FollowersNumber_ID = "txt_followers"
Profile_FollowersNumber_ID = package + FindSource(Source_Profile_FollowersNumber_ID)

# 用户Following数
Source_Profile_FollowingNumber_ID = "txt_following"
Profile_FollowingNumber_ID = package + FindSource(Source_Profile_FollowingNumber_ID)

# 用户上榜作品数
Source_Profile_RankRecords_ID = "txt_ranks"
Profile_RankRecords_ID = package + FindSource(Source_Profile_RankRecords_ID)

