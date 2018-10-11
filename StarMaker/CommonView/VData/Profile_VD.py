# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
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

# Followers按钮(text=Followers)
Source_Profile_FollowersBtn_ID = "txt_followers"
Profile_FollowersBtn_ID = package + FindSource(Source_Profile_FollowersBtn_ID)

# 用户Followers数
Source_Profile_FollowersNumber_ID = "txt_followers"
Profile_FollowersNumber_ID = package + FindSource(Source_Profile_FollowersNumber_ID)

# 用户Following数
Source_Profile_FollowingNumber_ID = "txt_following"
Profile_FollowingNumber_ID = package + FindSource(Source_Profile_FollowingNumber_ID)

# 用户上榜作品数
Source_Profile_RankRecords_ID = "txt_ranks"
Profile_RankRecords_ID = package + FindSource(Source_Profile_RankRecords_ID)

# 功能栏
Source_Profile_FunctionBar_IDS = "new_entrance_layout"
Profile_FunctionBar_IDS = package + FindSource(Source_Profile_FunctionBar_IDS)

# Tab栏
Source_Profile_TabBar_IDS = "vtb_pager"
Profile_TabBar_IDS = package + FindSource(Source_Profile_TabBar_IDS)

# ----------
# Tab——PROFILE
# ----------

# 【Personal info】个人信息
# 个人信息Title(text=Personal info)
Source_PersonalInfo_Title_ID = "personal_info"
PersonalInfo_Title_ID = package + FindSource(Source_PersonalInfo_Title_ID)

# 个人信息内容(text=Bio: Welcome to my stage🎤)
Source_PersonalInfo_desc_ID = "personal_info_desc"
PersonalInfo_desc_ID = package + FindSource(Source_PersonalInfo_desc_ID)

# 【Album】专辑
# 专辑Title(text=Album)
Source_Album_Title_ID = "tv_album_title"
Album_Title_ID = package + FindSource(Source_Album_Title_ID)

# 专辑图片（count -1 = 实际图片数量）
Album_Photo_ClaS = "android.widget.ScrollView"

# 【Top Fans】收到的星光排行
# 星光榜Title(text=Top Fans)
Source_TopFans_Title_ID = "tv_top_fan"
TopFans_Title_ID = package + FindSource(Source_TopFans_Title_ID)

# 星光值（text=16）
Source_Starlight_ID = "tv_receive_stars"
Starlight_ID = package + FindSource(Source_Starlight_ID)

# TopFans头像
Source_TopFans_First_ID = "iv_top_fans_first"
TopFans_First_ID = package + FindSource(Source_TopFans_First_ID)

Source_TopFans_Second_ID = "iv_top_fans_second"
TopFans_Second_ID = package + FindSource(Source_TopFans_Second_ID)

Source_TopFans_Third_ID = "iv_top_fans_third"
TopFans_Third_ID = package + FindSource(Source_TopFans_Third_ID)

# 【Contribute】送出的金币统计
# 送礼榜Title(text=Contribute)
Contribute_Title_AU = "new UiSelector().text(\"Contribute\")"

# 送礼榜金币数
Source_Contribute_Gold_ID = "tv_contribute"
Contribute_Gold_ID = package + FindSource(Source_Contribute_Gold_ID)

# 【Store】商城
# 商城Title(text=Store)
Source_Store_Title_ID = "tv_stores"
Store_Title_ID = package + FindSource(Source_Store_Title_ID)

# ----------
# Tab——POST
# ----------

# Posts Count(text=12 Posts)
Source_PostsCount_ID = "count"
PostsCount_ID = package + FindSource(Source_PostsCount_ID)

# Posts 作品名称([1]第一个作品名/[2]第二个作品名)
Source_PostsName_IDS = "com.starmakerinteractive.starmaker:id/txt_title"
PostsName_IDS = package + FindSource(Source_PostsName_IDS)

# Posts Repost
Source_RepostBtn_ID = "txt_repost"
RepostBtn_ID = package + FindSource(Source_RepostBtn_ID)

# Posts Comment
Source_CommentBtn_ID = "txt_comment"
CommentBtn_ID = package + FindSource(Source_CommentBtn_ID)

# Posts Share
Source_ShareBtn_ID = "tv_share"
ShareBtn_ID = package + FindSource(Source_ShareBtn_ID)

# Share——Copy Link(倒数第二个)
Source_CopyLink_Cla = "tv_share"
CopyLink_ClaS = package + FindSource(Source_CopyLink_Cla)


