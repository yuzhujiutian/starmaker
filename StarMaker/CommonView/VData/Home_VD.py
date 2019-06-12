# coding=utf-8
from StarMaker.Utils import Tools
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
# ----------
# 首页
# ----------
# 首页-feed流tab-切换tab([0]FOLLOWING/[1]POPULAR/[2]SING)
HomePage_Common_SwitchTab_ClaS = "android.widget.TextView"

# 首页-通用-搜索框
Source_HomePage_Common_Search_ID = "imb_search"
HomePage_Common_Search_ID = package + FS(Source_HomePage_Common_Search_ID)

# 首页-通用-Library
Source_HomePage_Common_Library_ID = "imb_sing"
HomePage_Common_Library_ID = package + FS(Source_HomePage_Common_Library_ID)

# 首页-通用-语言
Source_HomePage_Common_ContentLanguage_ID = "iv_content_language"
HomePage_Common_ContentLanguage_ID = package + FS(Source_HomePage_Common_ContentLanguage_ID)

# ----------
# 首页-语言选择弹窗
# ----------
# 首页-语言选择弹窗-Tips(English_text=The content displayed will be based on the language you choose.)
Source_HomePage_ChooseLanguage_IndiaTips_ID = "change_tips"
HomePage_ChooseLanguage_IndiaTips_ID = package + FS(Source_HomePage_ChooseLanguage_IndiaTips_ID)

# 首页-语言选择弹窗-切换语言([0]हिन्दी(Hindi)/[1]বাংলা(Bengali)/[2]ಕನ್ನಡ(Kannada)/[3]தமிழ்(Tamil)/[4]ગુજરાતી(Gujarati)/
# [5]ଓଡ଼ିଆ(Odia)/[6]മലയാളം(Malayalam)/[7]मराठी(Marathi)/[8]తెలుగు(Telugu)/[9]ਪੰਜਾਬੀ(Punjabi)/[10]অসমীয়া(Assamese)/
# [滑动翻页][-4]हरियाणवी(Haryanvi)/[-3]राजस्थानी(Rajasthani)/[-2]भोजपूरी(Bhojpuri)/[-1]English(English))
Source_HomePage_ChooseLanguage_IndiaSwitchLanguage_IDS = "select_language_item_tv"
HomePage_ChooseLanguage_IndiaSwitchLanguage_IDS = package + FS(Source_HomePage_ChooseLanguage_IndiaSwitchLanguage_IDS)

# ----------
# 首页-HotTopics
# ----------
# 首页-HotTopics-Text(English_text=Hot topics)
Source_HomePage_HotTopics_Text_ID = "txt_trend_recommend_title"
HomePage_HotTopics_Text_ID = package + FS(Source_HomePage_HotTopics_Text_ID)

# 首页-HotTopics-SeeAll(English_text=SEE ALL)
Source_HomePage_HotTopics_SeeAll_ID = "txt_trend_recommend_action"
HomePage_HotTopics_SeeAll_ID = package + FS(Source_HomePage_HotTopics_SeeAll_ID)

# ----------
# 首页-feed卡片
# ----------
# 首页-feed卡片-删除卡片(ID/IDS)
Source_HomePage_FeedCard_Delete_ID_IDS = "close_for_you"
HomePage_FeedCard_Delete_ID_IDS = package + FS(Source_HomePage_FeedCard_Delete_ID_IDS)

# 首页-feed卡片_头像(ID/IDS)
Source_HomePage_FeedCard_HeadView_ID_IDS = "civ_head_view"
HomePage_FeedCard_HeadView_ID_IDS = package + FS(Source_HomePage_FeedCard_HeadView_ID_IDS)

# 首页-feed卡片_用户名(ID/IDS)
Source_HomePage_FeedCard_UserName_ID_IDS = "user_name_view_tv_name"
HomePage_FeedCard_UserName_ID_IDS = package + FS(Source_HomePage_FeedCard_UserName_ID_IDS)

# 首页-feed卡片_Follow(English_text=FOLLOW)(ID/IDS)
Source_HomePage_FeedCard_Follow_ID_IDS = "v_follow"
HomePage_FeedCard_Follow_ID_IDS = package + FS(Source_HomePage_FeedCard_Follow_ID_IDS)

# 首页-feed卡片_叉号(ID/IDS)
Source_HomePage_FeedCard_Dislike_ID_IDS = "close_tweet"
HomePage_FeedCard_Dislike_ID_IDS = package + FS(Source_HomePage_FeedCard_Dislike_ID_IDS)

# 首页-feed卡片_描述(ID/IDS)
Source_HomePage_FeedCard_Describe_ID_IDS = "tv_desc"
HomePage_FeedCard_Describe_ID_IDS = package + FS(Source_HomePage_FeedCard_Describe_ID_IDS)

# 首页-feed卡片_图片(ID/IDS)
Source_HomePage_FeedCard_Img_ID_IDS = "img_recording_cover"
HomePage_FeedCard_Img_ID_IDS = package + FS(Source_HomePage_FeedCard_Img_ID_IDS)

# 首页-feed卡片_视屏(ID/IDS)
Source_HomePage_FeedCard_Video_ID_IDS = "iv_image"
HomePage_FeedCard_Video_ID_IDS = package + FS(Source_HomePage_FeedCard_Video_ID_IDS)

# 首页-feed卡片_分享按钮(ID/IDS)
Source_HomePage_FeedCard_Share_ID_IDS = "layout_share"
HomePage_FeedCard_Share_ID_IDS = package + FS(Source_HomePage_FeedCard_Share_ID_IDS)

# 首页-feed卡片_分享数(ID/IDS)
Source_HomePage_FeedCard_ShareCount_ID_IDS = "tv_share_num"
HomePage_FeedCard_ShareCount_ID_IDS = package + FS(Source_HomePage_FeedCard_ShareCount_ID_IDS)

# 首页-feed卡片_评论按钮(ID/IDS)
Source_HomePage_FeedCard_Comment_ID_IDS = "layout_comment"
HomePage_FeedCard_Comment_ID_IDS = package + FS(Source_HomePage_FeedCard_Comment_ID_IDS)

# 首页-feed卡片_评论数(ID/IDS)
Source_HomePage_FeedCard_CommentCount_ID_IDS = "tv_comment_num"
HomePage_FeedCard_CommentCount_ID_IDS = package + FS(Source_HomePage_FeedCard_CommentCount_ID_IDS)

# 首页-feed卡片_like按钮(ID/IDS)
Source_HomePage_FeedCard_Like_ID_IDS = "layout_like"
HomePage_FeedCard_Like_ID_IDS = package + FS(Source_HomePage_FeedCard_Like_ID_IDS)

# 首页-feed卡片_like数(ID/IDS)
Source_HomePage_FeedCard_LikeCount_ID_IDS = "tv_like_num"
HomePage_FeedCard_LikeCount_ID_IDS = package + FS(Source_HomePage_FeedCard_LikeCount_ID_IDS)

# 首页-feed卡片_下载按钮(ID/IDS)
Source_HomePage_FeedCard_Download_ID_IDS = "layout_download"
HomePage_FeedCard_Download_ID_IDS = package + FS(Source_HomePage_FeedCard_Download_ID_IDS)

# 首页-feed卡片_WhatsApp按钮(ID/IDS)
Source_HomePage_FeedCard_WhatsApp_ID_IDS = "img_share_whatsapp"
HomePage_FeedCard_WhatsApp_ID_IDS = package + FS(Source_HomePage_FeedCard_WhatsApp_ID_IDS)

# ----------
# 首页-Dislike弹窗
# ----------
# 首页-Dislike弹窗-Unwanted
Source_HomePage_DislikePop_Unwanted_ID = "tv_dislike"
HomePage_DislikePop_Unwanted_ID = package + FS(Source_HomePage_DislikePop_Unwanted_ID)

# 首页-Dislike弹窗-Report
Source_HomePage_DislikePop_Report_ID = "tv_report"
HomePage_DislikePop_Report_ID = package + FS(Source_HomePage_DislikePop_Report_ID)

# 首页-Dislike弹窗-Cancel
Source_HomePage_DislikePop_Cancel_ID = "tv_cancel"
HomePage_DislikePop_Cancel_ID = package + FS(Source_HomePage_DislikePop_Cancel_ID)

# ----------
# 首页-弹窗
# ----------
# 首页-Share弹窗-外框
Source_HomePage_SharePop_Frame_ID = "layout_background"
HomePage_SharePop_Frame_ID = package + FS(Source_HomePage_SharePop_Frame_ID)

# 首页-WhatsApp弹窗-外框
Source_HomePage_WhatsAppPop_Frame_ID = "ly_fragment_share_video_switch_dialog"
HomePage_WhatsAppPop_Frame_ID = package + FS(Source_HomePage_WhatsAppPop_Frame_ID)

# ----------
# 首页-底部五个Tab
# ----------
# 首页-底部五个Tab([0]Moment/[1]Party/[2]Sing/[3]Message/[4]Me)
# HomePage_MainTab_ClaS = "android.support.v7.app.ActionBar$Tab"
Source_HomePage_MainTab_IDS = "tab_animation_view"
HomePage_MainTab_IDS = package + FS(Source_HomePage_MainTab_IDS)

# 首页-底部五个Tab名称([0]Moment/[1]Party/[2]Sing/[3]Message/[4]Me)
Source_HomePage_MainTab_TabName_IDS = "tab_name"
HomePage_MainTab_TabName_IDS = package + FS(Source_HomePage_MainTab_TabName_IDS)

# ------------
# Sing页面
# ------------
# Sing页面-Sing标识
Source_SingPage_Function_CheckSingTitle_ID = "sing_title"
SingPage_Function_CheckSingTitle_ID = package + FS(Source_SingPage_Function_CheckSingTitle_ID)

# Sing页面-搜索框
Source_SingPage_Common_Search_ID = "txt_search"
SingPage_Common_Search_ID = package + FS(Source_SingPage_Common_Search_ID)

# Singy页面-播放器图标
Source_SingPage_Common_Player_ID = "music_wave_bar"
SingPage_Common_Player_ID = package + FS(Source_SingPage_Common_Player_ID)

# Sing页面-Banner
Source_SingPage_Common_Banner_ClaS = "android.widget.ImageView"

# Sing页面-中上方四个Tab([0]Free Style/[1]Collab/[2]Daily Task/[3]My Songs)
Source_SingPage_TabName_IDS = "rl_item_container"
SingPage_TabName_IDS = package + FS(Source_SingPage_TabName_IDS)

# Sing页面-Take the Mic
Source_SingPage_TakeTheMic_ID = "iv_challenge_label"
SingPage_TakeTheMic_ID = package + FS(Source_SingPage_TakeTheMic_ID)

# Sing页面-Vocal Talents
Source_SingPage_VocalTalents_ID = "iv_talent_label"
SingPage_VocalTalents_ID = package + FS(Source_SingPage_VocalTalents_ID)

# Sing页面-Sing Party
Source_SingPage_SingParty_ID = "iv_party_label"
SingPage_SingParty_ID = package + FS(Source_SingPage_SingParty_ID)

# Sing页面-中下方四个Tab([0]Recommend/[1]Hot/[2]Trending/[3]New)
Source_SingPage_SingHeat_IDS = "tv_tab_title"
SingPage_SingHeat_IDS = package + FS(Source_SingPage_SingHeat_IDS)

# Sing页面-任一Tab下-第一个歌曲封面
Source_SingPage_CommonTab_FirstSongImgCover = "img_cover"
SingPage_CommonTab_FirstSongImgCover = package + FS(Source_SingPage_CommonTab_FirstSongImgCover)

# Sing页面-Recommend下的歌曲点击SING
Source_SingPage_SingRecommend_SelectSing_IDS = "btn_sing"
SingPage_SingRecommend_SelectSing_IDS = package + FS(Source_SingPage_SingRecommend_SelectSing_IDS)

# Sing页面-选择歌曲-歌曲类型Tab([0]Solo/[1]Join Collab/[2]Start Collab/[3]Chorus)
Source_SingPage_SingRecommend_SingType_IDS = "item_play_detail_dialog_text"
SingPage_SingRecommend_SingType_IDS = package + FS(Source_SingPage_SingRecommend_SingType_IDS)


# ----------
# 歌曲Solo内
# ----------
# Sing页面-选择歌曲-Solo-引导信息
Source_SingSolo_SingGuide_ID = "recording_headset_dialog_msg_tv"
SingSolo_SingGuide_ID = package + FS(Source_SingSolo_SingGuide_ID)

# Sing页面-选择歌曲-Solo-引导信息确认
Source_SingSolo_SingGuideConfirm_ID = "recording_headset_dialog_i_know_btn"
SingSolo_SingGuideConfirm_ID = package + FS(Source_SingSolo_SingGuideConfirm_ID)

# Sing页面-选择歌曲-Solo-Pitch引导信息确认
Source_SingSolo_PitchGuide_ID = "tv_pitch_guide_tip"
SingSolo_PitchGuide_ID = package + FS(Source_SingSolo_PitchGuide_ID)

# Sing页面-选择歌曲-Solo-歌曲Pitch
Source_SingSolo_CheckPitch_ID = "record_pitch_btn"
SingSolo_CheckPitch_ID = package + FS(Source_SingSolo_CheckPitch_ID)

# Sing页面-选择歌曲-Solo-歌曲Volume
Source_SingSolo_CheckVolume_ID = "volume_btn"
SingSolo_ChecVolume_ID = package + FS(Source_SingSolo_CheckVolume_ID)

# Sing页面-选择歌曲-Solo-歌曲Start
Source_SingSolo_CheckStart_ID = "record_btn"
SingSolo_CheckStart_ID = package + FS(Source_SingSolo_CheckStart_ID)

# Sing页面-选择歌曲-Solo-歌曲Guide
Source_SingSolo_CheckGuide_ID = "guide_btn"
SingSolo_CheckGuide_ID = package + FS(Source_SingSolo_CheckGuide_ID)

# Sing页面-选择歌曲-Solo-歌曲Effect
Source_SingSolo_CheckEffect_ID = "audio_effect_btn"
SingSolo_CheckEffect_ID = package + FS(Source_SingSolo_CheckEffect_ID)

# Sing页面-选择歌曲-Solo-歌曲名称
Source_SingSolo_SingName_ID = "song_name_tv"
SingSolo_SingName_ID = package + FS(Source_SingSolo_SingName_ID)

# Sing页面-选择歌曲-Solo-音频和视频唱歌
Source_SingSolo_AudioVideo_ID = "song_name_tv"
SingSolo_AudioVideo_ID = package + FS(Source_SingSolo_AudioVideo_ID)

# Sing页面-选择歌曲-Solo-返回上一页
Source_SingSolo_BackPage_ID = "back_img"
SingSolo_BackPage_ID = package + FS(Source_SingSolo_AudioVideo_ID)

# Sing页面-选择歌曲-Solo-温馨提示图标
Source_SingSolo_TipsIcon_ID = "rl_title_fragment_record_tip"
SingSolo_TipsIcon_ID = package + FS(Source_SingSolo_TipsIcon_ID)


# Sing页面-选择歌曲-Solo-温馨提示信息
Source_SingSolo_TipInfo_ID = "rl_title_fragment_record_tip"
SingSolo_TipsInfo_ID = package + FS(Source_SingSolo_TipInfo_ID)

# Sing页面-选择歌曲-Solo-播放歌曲-歌曲打分
Source_SingSolo_SingRecordScore_ID = "pb_progress_view_record_score"
SingSolo_SingRecordScore_ID = package + FS(Source_SingSolo_SingRecordScore_ID)

# Sing页面-选择歌曲-Solo-播放歌曲-歌曲打分头像
Source_SingSolo_SingRecordScoreImage_ID = "iv_avatar_view_record_score"
SingSolo_SingRecordScoreImage_ID = package + FS(Source_SingSolo_SingRecordScoreImage_ID)

# Sing页面-选择歌曲-Solo-播放歌曲-歌曲音准器（上面的抖动条）
Source_SingSolo_SongTone_ID = "intonation_view"
SingSolo_SongTone_ID = package + FS(Source_SingSolo_SongTone_ID)

# ----------
# 安全警告
# ----------
# 允许，拒绝
Source_SingSolo_SafetyWarning_ClaS = "android.widget.Button"

# ----------
# Sing-Solo页面-Pitch
# ----------
# Pitch界面的-pitch
Source_SongTone_PitchPage_PitchTitle_ID = "trayTitle"
SongTone_PitchPage_PitchTitle_ID = package + FS(Source_SongTone_PitchPage_PitchTitle_ID)

# Pitch界面的-Close
Source_SongTone_PitchPage_PitchClose_ID = "done_tv"
SongTone_PitchPage_PitchClose_ID = package + FS(Source_SongTone_PitchPage_PitchClose_ID)

# Pitch界面的-"-"(低调节)
Source_SongTone_PitchPage_PitchLower_ID = "img_lower_pitch"
SongTone_PitchPage_PitchLower_ID = package + FS(Source_SongTone_PitchPage_PitchLower_ID)

# Pitch界面的-“+”（高调节）
Source_SongTone_PitchPage_PitchRaise_ID = "img_raise_pitch"
SongTone_PitchPage_PitchRaise_ID = package + FS(Source_SongTone_PitchPage_PitchRaise_ID)

# Pitch界面的-“----”（调节条）
Source_SongTone_PitchPage_PitchProgressBar_ID = "pitchTrayProgressBar"
SongTone_PitchPage_PitchProgressBar_ID = package + FS(Source_SongTone_PitchPage_PitchProgressBar_ID)

# Pitch界面的-分数（调节分数）
Source_SongTone_PitchPage_PitchContent_ID = "tv_pitch_content"
SongTone_PitchPage_PitchContent_ID = package + FS(Source_SongTone_PitchPage_PitchContent_ID)

# ----------
# Sing-Solo页面-VOLUME
# ----------
# VOLUME界面的-Volume-voice
Source_SongTone_VolumePage_VolumeAdjust_ID = "volumeTrayVoiceTv"
SongTone_VolumePage_VolumeAdjust_ID = package + FS(Source_SongTone_VolumePage_VolumeAdjust_ID)

# VOLUME界面的-Volume-Music
Source_SongTone_VolumePage_MusicAdjust_ID = "volumeTrayMusicTv"
SongTone_VolumePage_MusicAdjust_ID = package + FS(Source_SongTone_VolumePage_MusicAdjust_ID)

# ----------
# Sing-Solo页面-Effect
# ----------
# Effect界面的-Effect的场景效果
Source_SongTone_EffectPage_SceneEffect_IDS = "tv_effect_item_effect_tray"
SongTone_EffectPage_SceneEffect_IDS = package + FS(Source_SongTone_EffectPage_SceneEffect_IDS)






