# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
gms = "com.google.android"


# ----------
# 作品播放详情页
# ----------
# PlaybackDetails页-播放内容-播放表面
Source_PlaybackDetailsPage_PlayContent_Surface_ID = "video_surface"
PlaybackDetailsPage_PlayContent_Surface_ID = package + mapping_dict[Source_PlaybackDetailsPage_PlayContent_Surface_ID]

# PlaybackDetails页-播放内容-暂停
Source_PlaybackDetailsPage_PlayContent_Suspend_ID = "album_laoding_pb"
PlaybackDetailsPage_PlayContent_Suspend_ID = package + mapping_dict[Source_PlaybackDetailsPage_PlayContent_Suspend_ID]

# PlaybackDetails页-播放内容-继续
Source_PlaybackDetailsPage_PlayContent_Continue_ID = "play_control_play_pause"
PlaybackDetailsPage_PlayContent_Continue_ID = package + mapping_dict[Source_PlaybackDetailsPage_PlayContent_Continue_ID]

# PlaybackDetails页-作者信息-头像(ID_IDS]
Source_PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS = "civ_head_view"
PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS = package + \
                                                 mapping_dict[Source_PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS]

# PlaybackDetails页-作者信息-用户名
Source_PlaybackDetailsPage_AuthorInfo_UserName_ID = "user_name_view_tv_name"
PlaybackDetailsPage_AuthorInfo_UserName_ID = package + mapping_dict[Source_PlaybackDetailsPage_AuthorInfo_UserName_ID]

# PlaybackDetails页-作品信息-描述
Source_PlaybackDetailsPage_RecordingInfo_Describe_ID = "tv_desc"
PlaybackDetailsPage_RecordingInfo_Describe_ID = package + \
                                                mapping_dict[Source_PlaybackDetailsPage_RecordingInfo_Describe_ID]

# PlaybackDetails页-作品信息-统计信息(需拆分，原文="173 shares · 333 likes · 2.4K plays · A"]
Source_PlaybackDetailsPage_RecordingInfo_Statistics_ID = "tv_like_count"
PlaybackDetailsPage_RecordingInfo_Statistics_ID = package + \
                                                  mapping_dict[Source_PlaybackDetailsPage_RecordingInfo_Statistics_ID]

# ----------
# 图片/视屏播放详情页
# ----------
# PlaybackDetails页-图片详情页-图片预览
Source_PlaybackDetailsPage_Img_Preview_ID = "imt_preview"
PlaybackDetailsPage_Img_Preview_ID = package + mapping_dict[Source_PlaybackDetailsPage_Img_Preview_ID]

# PlaybackDetails页-视屏详情页-视屏预览
Source_PlaybackDetailsPage_Video_Preview_ID = "ttr_video"
PlaybackDetailsPage_Video_Preview_ID = package + mapping_dict[Source_PlaybackDetailsPage_Video_Preview_ID]

# PlaybackDetails页-视屏详情页-Repost[0]
Source_PlaybackDetailsPage_Video_Repost_IDS = "tv_tab_title"
PlaybackDetailsPage_Video_Repost_IDS = package + mapping_dict[Source_PlaybackDetailsPage_Video_Repost_IDS]

# PlaybackDetails页-视屏详情页-Like
Source_PlaybackDetailsPage_Video_Like_ID = "lyt_like"
PlaybackDetailsPage_Video_Like_ID = package + mapping_dict[Source_PlaybackDetailsPage_Video_Like_ID]

# PlaybackDetails页-视屏详情页-Comment
# Source_PlaybackDetailsPage_Video_Comment_ID = "tv_detail_bottom_detail_comment "
# PlaybackDetailsPage_Video_Comment_ID = package + mapping_dict[Source_PlaybackDetailsPage_Video_Comment_ID]

# PlaybackDetails页-视屏详情页-Share
Source_PlaybackDetailsPage_Video_Share_ID = "lyt_repost"
PlaybackDetailsPage_Video_Share_ID = package + mapping_dict[Source_PlaybackDetailsPage_Video_Share_ID]

# PlaybackDetails页-视屏详情页-Gift
Source_PlaybackDetailsPage_Video_Gift_ID = "lyt_gift"
PlaybackDetailsPage_Video_Gift_ID = package + mapping_dict[Source_PlaybackDetailsPage_Video_Gift_ID]

# PlaybackDetails页-视屏详情页--Comment输入框
Source_PlaybackDetailsPage_Video_CommentSendBox_ID = "edit_text"
PlaybackDetailsPage_Video_CommentSendBox_ID = package + mapping_dict[Source_PlaybackDetailsPage_Video_CommentSendBox_ID]

# PlaybackDetails页-视屏详情页--Comment发布按钮
Source_PlaybackDetailsPage_Video_CommentSendBtn_ID = "iv_send"
PlaybackDetailsPage_Video_CommentSendBtn_ID = package + mapping_dict[Source_PlaybackDetailsPage_Video_CommentSendBtn_ID]

# PlaybackDetails页-视屏详情页--礼物价值text
Source_PlaybackDetailsPage_Video_GiftValue_IDS = "gift_balance"
PlaybackDetailsPage_Video_GiftValue_IDS = package + mapping_dict[Source_PlaybackDetailsPage_Video_GiftValue_IDS]

# PlaybackDetails页-视屏详情页--Combo按钮
Source_PlaybackDetailsPage_Video_ComboBtn_ID = "icon_circle"
PlaybackDetailsPage_Video_ComboBtn_ID = package + mapping_dict[Source_PlaybackDetailsPage_Video_ComboBtn_ID]

# PlaybackDetails页-视屏详情页--礼物面板Send按钮
Source_PlaybackDetailsPage_Video_GiftDetailSendBtn_ID = "btn_send_gift"
PlaybackDetailsPage_Video_GiftDetailSendBtn_ID = package + \
                                                 mapping_dict[Source_PlaybackDetailsPage_Video_GiftDetailSendBtn_ID]

# 礼物-送礼-银币不足弹窗文案(银币="Insufficient Silvers! Finish the Tasks to get more Silvers./金币="Not enough storage"]
Gift_SendGift_InsufficientFunds_ID = "android:id/message"

# 礼物-送礼-银币不足弹窗-取消按钮
Gift_SendGift_InsufficientSilvers_Cancel_ID = "android:id/button2"
