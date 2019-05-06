# coding=utf-8
from StarMaker.Utils import Tools
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
# ----------
# 个人页
# ----------
# 个人页-Title
Source_ProfilePage_Title_ID = "txt_title"
ProfilePage_Title_ID = package + FS(Source_ProfilePage_Title_ID)

# 个人页-FindFriends
Source_ProfilePage_FindFriends_ID = "imb_friends"
ProfilePage_FindFriends_ID = package + FS(Source_ProfilePage_FindFriends_ID)

# 个人页-Setting
Source_ProfilePage_Setting_ID = "imb_settings"
ProfilePage_Setting_ID = package + FS(Source_ProfilePage_Setting_ID)

# ----------
# 个人页-个人信息
# ----------
# 个人页-个人信息-背景图
# Source_ProfilePage_UserInfo_Background1_ID = "album_front_img"
# ProfilePage_UserInfo_Background1_ID = package + FS(Source_ProfilePage_UserInfo_Background1_ID)
# Source_ProfilePage_UserInfo_Background2_ID = "album_back_img"
# ProfilePage_UserInfo_Background2_ID = package + FS(Source_ProfilePage_UserInfo_Background2_ID)
Source_ProfilePage_UserInfo_Background_ID = "album_mask_iv"
ProfilePage_UserInfo_Background_ID = package + FS(Source_ProfilePage_UserInfo_Background_ID)


# 个人页-个人信息-用户头像(同Moments头像同ID)
Source_ProfilePage_UserInfo_HeadView_ID_IDS = "civ_head_view"
ProfilePage_UserInfo_HeadView_ID_IDS = package + FS(Source_ProfilePage_UserInfo_HeadView_ID_IDS)

# 个人页-个人信息-用户昵称(同Moments昵称同ID)
Source_ProfilePage_UserInfo_StageName_ID_IDS = "user_name_view_tv_name"
ProfilePage_UserInfo_StageName_ID_IDS = package + FS(Source_ProfilePage_UserInfo_StageName_ID_IDS)

# 用户等级
Source_ProfilePage_UserInfo_UserLevel_ID = "user_name_view_tv_level"
ProfilePage_UserInfo_UserLevel_ID = package + FS(Source_ProfilePage_UserInfo_UserLevel_ID)

# 用户VIP状态(text=Vip/Get Vip)
Source_ProfilePage_UserInfo_VIPLevel_ID = "user_name_view_tv_vip_level"
ProfilePag_UserInfo_VIPLevel_ID = package + FS(Source_ProfilePage_UserInfo_VIPLevel_ID)

# 用户Followers数
Source_ProfilePage_UserInfo_FollowersNumber_ID = "txt_followers"
ProfilePage_UserInfo_FollowersNumber_ID = package + FS(Source_ProfilePage_UserInfo_FollowersNumber_ID)

# 用户Following数
Source_ProfilePage_UserInfo_FollowingNumber_ID = "txt_following"
ProfilePage_UserInfo_FollowingNumber_ID = package + FS(Source_ProfilePage_UserInfo_FollowingNumber_ID)

# # 用户上榜作品数
# Source_ProfilePage_UserInfo_RankRecords_ID = "txt_ranks"
# ProfilePage_UserInfo_RankRecords_ID = package + FS(Source_ProfilePage_UserInfo_RankRecords_ID)

# 功能栏(Check)
Source_ProfilePage_CheckList_FunctionBar_IDS = "tv_new_entrance_profile"
ProfilePage_CheckList_FunctionBar_IDS = package + FS(Source_ProfilePage_CheckList_FunctionBar_IDS)

# Tab栏 Tab([0]PROFILE/[1]MOMENTS)
Source_ProfilePage_CheckList_TabBar_IDS = "tv_tab_title"
ProfilePage_CheckList_TabBar_IDS = package + FS(Source_ProfilePage_CheckList_TabBar_IDS)

# ----------
# Tab——PROFILE
# ----------
# 【Personal info】个人信息
# 个人信息Text(text=Personal info)
Source_ProfilePage_ProfileTab_PersonalInfo_Text_ID = "personal_info"
ProfilePage_ProfileTab_PersonalInfo_Text_ID = package + FS(Source_ProfilePage_ProfileTab_PersonalInfo_Text_ID)

# 个人信息内容(text=Bio: Welcome to my stage#55356;#57252;)
Source_ProfilePage_ProfileTab_PersonalInfo_Desc_ID = "personal_info_desc"
ProfilePage_ProfileTab_PersonalInfo_Desc_ID = package + FS(Source_ProfilePage_ProfileTab_PersonalInfo_Desc_ID)

# 【Album】专辑
# 专辑Text(text=Album)
Source_ProfilePage_ProfileTab_Album_Text_ID = "tv_album_title"
ProfilePage_ProfileTab_Album_Text_ID = package + FS(Source_ProfilePage_ProfileTab_Album_Text_ID)

# 专辑图片（count = 实际图片数量）
Source_ProfilePage_ProfileTab_Album_Photos_ID_IDS = "iv_profile_tab_detail_personal"
ProfilePage_ProfileTab_Album_Photos_ID_IDS = package + FS(Source_ProfilePage_ProfileTab_Album_Photos_ID_IDS)

# 【Top Fans】收到的星光排行
# 星光榜Text(text=Top Fans)
Source_ProfilePage_ProfileTab_TopFans_Text_ID = "tv_top_fan"
ProfilePage_ProfileTab_TopFans_Text_ID = package + FS(Source_ProfilePage_ProfileTab_TopFans_Text_ID)

# 星光值（text=16）
Source_ProfilePage_ProfileTab_TopFans_Starlight_ID = "tv_receive_stars"
ProfilePage_ProfileTab_TopFans_Starlight_ID = package + FS(Source_ProfilePage_ProfileTab_TopFans_Starlight_ID)

# TopFans头像
Source_ProfilePage_ProfileTab_TopFans_First_ID = "iv_top_fans_first"
ProfilePage_ProfileTab_TopFans_First_ID = package + FS(Source_ProfilePage_ProfileTab_TopFans_First_ID)

Source_ProfilePage_ProfileTab_TopFans_Second_ID = "iv_top_fans_second"
ProfilePage_ProfileTab_TopFans_Second_ID = package + FS(Source_ProfilePage_ProfileTab_TopFans_Second_ID)

Source_ProfilePage_ProfileTab_TopFans_Third_ID = "iv_top_fans_third"
ProfilePage_ProfileTab_TopFans_Third_ID = package + FS(Source_ProfilePage_ProfileTab_TopFans_Third_ID)

# 【Contribute】送出的金币统计
# 送礼榜Text(text=Contribute)
ProfilePage_ProfileTab_Contribute_Text_AU = "new UiSelector().text(\"योगदान दें\")"

# 送礼榜金币数
Source_ProfilePage_ProfileTab_Contribute_Gold_ID = "tv_contribute"
ProfilePage_ProfileTab_Contribute_Gold_ID = package + FS(Source_ProfilePage_ProfileTab_Contribute_Gold_ID)

# 【Store】商城
# 商城Text(text=Store)
Source_ProfilePage_ProfileTab_Store_Text_ID = "tv_stores"
ProfilePage_ProfileTab_Store_Text_ID = package + FS(Source_ProfilePage_ProfileTab_Store_Text_ID)

# ----------
# Tab——Moments
# ----------
# 作品统计(text=Total Moments(9))
Source_ProfilePage_MomentsTab_CountNum_ID = "txt_count"
ProfilePage_MomentsTab_CountNum_ID = package + FS(Source_ProfilePage_MomentsTab_CountNum_ID)

# 私密标签（text=Private）
Source_ProfilePage_MomentsTab_ShootInfo_Private_ID_IDS = "tx_status"
ProfilePage_MomentsTab_ShootInfo_Private_ID_IDS = package + FS(Source_ProfilePage_MomentsTab_ShootInfo_Private_ID_IDS)

# 发布时间
Source_ProfilePage_MomentsTab_ShootInfo_PostTime_ID_IDS = "tv_time"
ProfilePage_MomentsTab_ShootInfo_PostTime_ID_IDS = package + FS(Source_ProfilePage_MomentsTab_ShootInfo_PostTime_ID_IDS)

# More按钮
Source_ProfilePage_MomentsTab_ShootInfo_More_ID_IDS = "img_trend_more"
ProfilePage_MomentsTab_ShootInfo_More_ID_IDS = package + FS(Source_ProfilePage_MomentsTab_ShootInfo_More_ID_IDS)

# Like
Source_ProfilePage_MomentsTab_ShootInfo_Like_ID_IDS = "tv_like_num"
ProfilePage_MomentsTab_ShootInfo_Like_ID_IDS = package + FS(Source_ProfilePage_MomentsTab_ShootInfo_Like_ID_IDS)

# Comment
Source_ProfilePage_MomentsTab_ShootInfo_Comment_ID_IDS = "tv_comment_num"
ProfilePage_MomentsTab_ShootInfo_Comment_ID_IDS = package + FS(Source_ProfilePage_MomentsTab_ShootInfo_Comment_ID_IDS)

# Share
Source_ProfilePage_MomentsTab_ShootInfo_Share_ID_IDS = "tv_share_num"
ProfilePage_MomentsTab_ShootInfo_Share_ID_IDS = package + FS(Source_ProfilePage_MomentsTab_ShootInfo_Share_ID_IDS)

# ----------
# Tab——Moments——More
# ----------
# FunctionCommon([-1]copyLink/[-2]Save/[-3]Delete)
Source_ProfilePage_MomentsTab_More_FunctionCommon_IDS = "item_rl"
ProfilePage_MomentsTab_More_FunctionCommon_IDS = package + FS(Source_ProfilePage_MomentsTab_More_FunctionCommon_IDS)

# 确认删除按钮
Source_ProfilePage_MomentsTab_ShootInfo_More_Delete_Confirm_ID = "md_buttonDefaultPositive"
ProfilePage_MomentsTab_ShootInfo_More_Delete_Confirm_ID = package + FS(Source_ProfilePage_MomentsTab_ShootInfo_More_Delete_Confirm_ID)

# # ----------
# # Tab——POST
# # ----------
# # Posts Count(text=12 Posts)
# Source_PostsCount_ID = "count"
# PostsCount_ID = package + FS(Source_PostsCount_ID)
#
# # Posts 作品名称([1]第一个作品名/[2]第二个作品名)
# Source_PostsName_IDS = "com.starmakerinteractive.starmaker:id/txt_title"
# PostsName_IDS = package + FS(Source_PostsName_IDS)
#
# # Posts Repost
# Source_RepostBtn_ID = "txt_repost"
# RepostBtn_ID = package + FS(Source_RepostBtn_ID)
#
# # Posts Comment
# Source_CommentBtn_ID = "txt_comment"
# CommentBtn_ID = package + FS(Source_CommentBtn_ID)
#
# # Posts Share
# Source_ShareBtn_ID = "tv_share"
# ShareBtn_ID = package + FS(Source_ShareBtn_ID)
#
# # Share——Copy Link(倒数第二个)
# Source_CopyLink_ClaS = "tv_share"
# CopyLink_ClaS = package + FS(Source_CopyLink_ClaS)


