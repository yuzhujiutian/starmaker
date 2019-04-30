# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
gms = "com.google.android"


# ----------
# 作品播放详情页
# ----------
# PlaybackDetails页-播放内容-播放表面
Source_PlaybackDetailsPage_PlayContent_Surface_ID = "video_surface"
PlaybackDetailsPage_PlayContent_Surface_ID = package + FS(Source_PlaybackDetailsPage_PlayContent_Surface_ID)

# PlaybackDetails页-播放内容-暂停
Source_PlaybackDetailsPage_PlayContent_Suspend_ID = "album_laoding_pb"
PlaybackDetailsPage_PlayContent_Suspend_ID = package + FS(Source_PlaybackDetailsPage_PlayContent_Suspend_ID)

# PlaybackDetails页-播放内容-继续
Source_PlaybackDetailsPage_PlayContent_Continue_ID = "play_control_play_pause"
PlaybackDetailsPage_PlayContent_Continue_ID = package + FS(Source_PlaybackDetailsPage_PlayContent_Continue_ID)

# PlaybackDetails页-作者信息-头像(ID_IDS)
Source_PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS = "civ_head_view"
PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS = package + FS(Source_PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS)

# PlaybackDetails页-作者信息-用户名
Source_PlaybackDetailsPage_AuthorInfo_UserName_ID = "user_name_view_tv_name"
PlaybackDetailsPage_AuthorInfo_UserName_ID = package + FS(Source_PlaybackDetailsPage_AuthorInfo_UserName_ID)

# PlaybackDetails页-作品信息-描述
Source_PlaybackDetailsPage_RecordingInfo_Describe_ID = "tv_desc"
PlaybackDetailsPage_RecordingInfo_Describe_ID = package + FS(Source_PlaybackDetailsPage_RecordingInfo_Describe_ID)

# PlaybackDetails页-作品信息-统计信息(需拆分，原文="173 shares · 333 likes · 2.4K plays · A")
Source_PlaybackDetailsPage_RecordingInfo_Statistics_ID = "tv_like_count"
PlaybackDetailsPage_RecordingInfo_Statistics_ID = package + FS(Source_PlaybackDetailsPage_RecordingInfo_Statistics_ID)

# ----------
# 图片/视屏播放详情页
# ----------
# PlaybackDetails页-图片详情页-图片预览
Source_PlaybackDetailsPage_Img_Preview_ID = "imt_preview"
PlaybackDetailsPage_Img_Preview_ID = package + FS(Source_PlaybackDetailsPage_Img_Preview_ID)

# PlaybackDetails页-视屏详情页-视屏预览
Source_PlaybackDetailsPage_Video_Preview_ID = "ttr_video"
PlaybackDetailsPage_Video_Preview_ID = package + FS(Source_PlaybackDetailsPage_Video_Preview_ID)

# PlaybackDetails页-视屏详情页-Repost[0]
Source_PlaybackDetailsPage_Video_Repost_IDS = "tv_tab_title"
PlaybackDetailsPage_Video_Repost_IDS = package + FS(Source_PlaybackDetailsPage_Video_Repost_IDS)

# PlaybackDetails页-视屏详情页-Comment[1]
Source_PlaybackDetailsPage_Video_Comment_IDS = "tv_tab_title"
PlaybackDetailsPage_Video_Comment_IDS = package + FS(Source_PlaybackDetailsPage_Video_Comment_IDS)

