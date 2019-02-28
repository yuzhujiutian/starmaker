# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
# ----------
# Jalebee首页
# ----------
# Jalebee首页底部按钮([0]Home/[1]Party/[2]Message/[3]Me)
Source_Jalebee_MainTab_Common_IDS = "tab_name"
Jalebee_MainTab_Common_IDS = package + FS(Source_Jalebee_MainTab_Common_IDS)

# Jalebee首页内容Tab([0]FOLLOWING/[1]POPULAR)
Source_Jalebee_FeedTab_Common_IDS = "tv_tab_title"
Jalebee_FeedTab_Common_IDS = package + FS(Source_Jalebee_FeedTab_Common_IDS)

# Jalebee首页底部Post按钮
Source_Jalebee_MainTab_Post_ID = "tab_post_container"
Jalebee_MainTab_Post_ID = package + FS(Source_Jalebee_MainTab_Post_ID)

# ----------
# JalebeeFollowing页
# ----------
# JalebeeFollowing页-作品发布时间
Source_JalebeeFollowingPage_ShootPostTime_ID_IDS = "tv_time"
JalebeeFollowingPage_ShootPostTime_ID_IDS = package + FS(Source_JalebeeFollowingPage_ShootPostTime_ID_IDS)

# JalebeeFollowing页-发布-发布进度条
Source_JalebeeFollowingPage_PublishBar_ID = "tweet_publish_bar"
JalebeeFollowingPage_PublishBar_ID = package + FS(Source_JalebeeFollowingPage_PublishBar_ID)

# JalebeeFollowing页-作品Like数
Source_JalebeeFollowingPage_ShootLikeNum_ID_IDS = "tv_like_num"
JalebeeFollowingPage_ShootLikeNum_ID_IDS = package + FS(Source_JalebeeFollowingPage_ShootLikeNum_ID_IDS)

# ----------
# Jalebee-Party页
# ----------
# Jalebee-Party页-Title
Source_JalebeePartyPage_Title_Text_ID = "tv_tab_title"
JalebeePartyPage_Title_Text_ID = package + FS(Source_JalebeePartyPage_Title_Text_ID)

# Jalebee-Party页-MyRoom/History([0]MyRoom="मेरा रूम"/[1]History="इतिहास")
Source_JalebeePartyPage_MyRoom_History_Text_IDS = "txt_title"
JalebeePartyPage_MyRoom_History_Text_IDS = package + FS(Source_JalebeePartyPage_MyRoom_History_Text_IDS)

# Jalebee-Party页-Search
Source_JalebeePartyPage_Search_Btn_ID = "imb_search"
JalebeePartyPage_Search_Btn_ID = package + FS(Source_JalebeePartyPage_Search_Btn_ID)

# ----------
# Jalebee-拍摄页
# ----------
# Jalebee-拍摄页-Start按钮
Source_JalebeeShootingPage_Function_StartBtn_ID = "rbtn_record_capturelib_fragment_capture"
JalebeeShootingPage_Function_StartBtn_ID = package + FS(Source_JalebeeShootingPage_Function_StartBtn_ID)

# Jalebee-拍摄页-选择音乐引导
Source_JalebeeShootingPage_Function_AddMusicGuide_ID = "tv_tip_capturelib_popupwindow_add_bgm_guide"
JalebeeShootingPage_Function_AddMusicGuide_ID = package + FS(Source_JalebeeShootingPage_Function_AddMusicGuide_ID)

# Jalebee-拍摄页-进度条
Source_JalebeeShootingPage_Function_ProgressBar_ID = "spb_progress_capturelib_fragment_capture"
JalebeeShootingPage_Function_ProgressBar_ID = package + FS(Source_JalebeeShootingPage_Function_ProgressBar_ID)

# Jalebee-拍摄页-关闭按钮
Source_JalebeeShootingPage_Function_CloseBtn_ID = "iv_close_capturelib_fragment_capture"
JalebeeShootingPage_Function_CloseBtn_ID = package + FS(Source_JalebeeShootingPage_Function_CloseBtn_ID)

# Jalebee-拍摄页-音乐icon
Source_JalebeeShootingPage_Function_MusicIcon_ID = "iv_choose_music_capturelib_fragment_capture"
JalebeeShootingPage_Function_MusicIcon_ID = package + FS(Source_JalebeeShootingPage_Function_MusicIcon_ID)

# Jalebee-拍摄页-当前选择音乐
Source_JalebeeShootingPage_Function_MusicName_ID = "tv_choose_music_capturelib_fragment_capture"
JalebeeShootingPage_Function_MusicName_ID = package + FS(Source_JalebeeShootingPage_Function_MusicName_ID)

# Jalebee-拍摄页-取消已选择音乐
Source_JalebeeShootingPage_Function_DeselectedMusic_ID = "iv_delete_music_capturelib_fragment_capture"
JalebeeShootingPage_Function_DeselectedMusic_ID = package + FS(Source_JalebeeShootingPage_Function_DeselectedMusic_ID)

# Jalebee-拍摄页-手电筒
Source_JalebeeShootingPage_Function_Flashlight_ID = "iv_flash_capturelib_fragment_capture"
JalebeeShootingPage_Function_Flashlight_ID = package + FS(Source_JalebeeShootingPage_Function_Flashlight_ID)

# Jalebee-拍摄页-切换摄像头
Source_JalebeeShootingPage_Function_SwitchingCamera_ID = "iv_camera_switchover_capturelib_fragment_capture"
JalebeeShootingPage_Function_SwitchingCamera_ID = package + FS(Source_JalebeeShootingPage_Function_Flashlight_ID)

# Jalebee-拍摄页-美颜
Source_JalebeeShootingPage_Function_Beauty_ID = "iv_beauty_capturelib_fragment_capture"
JalebeeShootingPage_Function_Beauty_ID = package + FS(Source_JalebeeShootingPage_Function_Beauty_ID)

# Jalebee-拍摄页-滤镜
Source_JalebeeShootingPage_Function_Filter_ID = "iv_filter_capturelib_fragment_capture"
JalebeeShootingPage_Function_Filter_ID = package + FS(Source_JalebeeShootingPage_Function_Filter_ID)

# Jalebee-拍摄页-相册
Source_JalebeeShootingPage_Function_Album_ID = "iv_album_capturelib_fragment_capture"
JalebeeShootingPage_Function_Album_ID = package + FS(Source_JalebeeShootingPage_Function_Album_ID)

# Jalebee-拍摄页-拍摄模式([0]Photo/[1](默认)15S/[2]60S)
Source_JalebeeShootingPage_Function_ShootingMode_IDS = "tv_name_capturelib_view_record_mode_display_item"
JalebeeShootingPage_Function_ShootingMode_IDS = package + FS(Source_JalebeeShootingPage_Function_ShootingMode_IDS)

# ----------
# Jalebee-音乐选择页
# ----------
# Jalebee-音乐选择页-Title
Source_JalebeeSelectMusicPage_Title_ID = "txt_title"
JalebeeSelectMusicPage_Title_ID = package + FS(Source_JalebeeSelectMusicPage_Title_ID)

# Jalebee-音乐选择页-Close
Source_JalebeeSelectMusicPage_Function_Close_ID = "imb_close"
JalebeeSelectMusicPage_Function_Close_ID = package + FS(Source_JalebeeSelectMusicPage_Function_Close_ID)

# Jalebee-音乐选择页-Search
Source_JalebeeSelectMusicPage_Function_Search_ID = "lyt_search"
JalebeeSelectMusicPage_Function_Search_ID = package + FS(Source_JalebeeSelectMusicPage_Function_Search_ID)

# Jalebee-音乐选择页-内容Tab([0]推荐页EXPLORE/[1]收藏页FAVORITE)
Source_JalebeeSelectMusicPage_FeedTab_Common_IDS = "tv_tab_title"
JalebeeSelectMusicPage_FeedTab_Common_IDS = package + FS(Source_JalebeeSelectMusicPage_FeedTab_Common_IDS)

# Jalebee-音乐选择页-分类
Source_JalebeeSelectMusicPage_Function_Category_IDS = "label_name"
JalebeeSelectMusicPage_Function_Category_IDS = package + FS(Source_JalebeeSelectMusicPage_Function_Category_IDS)

# Jalebee-音乐选择页-音乐名
Source_JalebeeSelectMusicPage_Function_SongsName_IDS = "tv_song"
JalebeeSelectMusicPage_Function_SongsName_IDS = package + FS(Source_JalebeeSelectMusicPage_Function_SongsName_IDS)

# Jalebee-音乐选择页-收藏
Source_JalebeeSelectMusicPage_Function_Favor_IDS = "iv_favor"
JalebeeSelectMusicPage_Function_Favor_IDS = package + FS(Source_JalebeeSelectMusicPage_Function_Favor_IDS)

# Jalebee-音乐选择页-确认选择
Source_JalebeeSelectMusicPage_Function_USE_ID = "tv_sing"
JalebeeSelectMusicPage_Function_USE_ID = package + FS(Source_JalebeeSelectMusicPage_Function_USE_ID)

# ----------
# Jalebee-发布预览页
# ----------
# Jalebee-发布预览页-进度条
Source_JalebeePostPreviewPage_Function_ProgressBar_ID = "spb_progress_capturelib_fragment_edit"
JalebeePostPreviewPage_Function_ProgressBar_ID = package + FS(Source_JalebeePostPreviewPage_Function_ProgressBar_ID)

# Jalebee-发布预览页-返回
Source_JalebeePostPreviewPage_Function_Back_ID = "iv_back_capturelib_fragment_edit"
JalebeePostPreviewPage_Function_Back_ID = package + FS(Source_JalebeePostPreviewPage_Function_Back_ID)

# 其他功能([0]Back/[1]Volume/[2]Cut Music/[3]Select Music/[4]Cover)
JalebeePostPreviewPage_Function_Other_ClaS = "android.widget.ImageView"

# Jalebee-发布预览页-Next
Source_JalebeePostPreviewPage_Function_Next_ID = "tv_next_capturelib_fragment_edit"
JalebeePostPreviewPage_Function_Next_ID = package + FS(Source_JalebeePostPreviewPage_Function_Next_ID)

# ----------
# Jalebee-发布编辑页
# ----------
# Jalebee-发布编辑页-Title
Source_JalebeePostEditPage_Title_ID = "tv_title"
JalebeePostEditPage_Title_ID = package + FS(Source_JalebeePostEditPage_Title_ID)

# Jalebee-发布编辑页-返回
JalebeePostEditPage_Function_Back_Cla = "android.widget.ImageButton"

# Jalebee-发布编辑页-输入文字(默认文案：)
Source_JalebeePostEditPage_Function_MindWriting_ID = "writing_edit_view"
JalebeePostEditPage_Function_MindWriting_ID = package + FS(Source_JalebeePostEditPage_Function_MindWriting_ID)

# Jalebee-发布编辑页-更换封面
Source_JalebeePostEditPage_Function_SetCover_ID = "iv_video"
JalebeePostEditPage_Function_SetCover_ID = package + FS(Source_JalebeePostEditPage_Function_SetCover_ID)

# Jalebee-发布编辑页-@好友
Source_JalebeePostEditPage_Function_RemindFriends_ID = "ll_at_user"
JalebeePostEditPage_Function_RemindFriends_ID = package + FS(Source_JalebeePostEditPage_Function_RemindFriends_ID)

# Jalebee-发布编辑页-Topic
Source_JalebeePostEditPage_Function_Topic_ID = "topic_parent"
JalebeePostEditPage_Function_Topic_ID = package + FS(Source_JalebeePostEditPage_Function_Topic_ID)

# Jalebee-发布编辑页-定位
Source_JalebeePostEditPage_Function_Location_ID = "location_parent"
JalebeePostEditPage_Function_Location_ID = package + FS(Source_JalebeePostEditPage_Function_Location_ID)

# Jalebee-发布编辑页-保存草稿
Source_JalebeePostEditPage_Function_Draft_ID = "tv_draft"
JalebeePostEditPage_Function_Draft_ID = package + FS(Source_JalebeePostEditPage_Function_Draft_ID)

# Jalebee-发布编辑页-发布
Source_JalebeePostEditPage_Function_Post_ID = "tv_post"
JalebeePostEditPage_Function_Post_ID = package + FS(Source_JalebeePostEditPage_Function_Post_ID)

# ----------
# Jalebee-消息页
# ----------
# Jalebee-消息页-功能区通用IDS([0]System/[1]Gifts/[2]Messages)
Source_JalebeeMessagePage_FunctionCommon_IDS = "badge_text"
JalebeeMessagePage_FunctionCommon_IDS = package + FS(Source_JalebeeMessagePage_FunctionCommon_IDS)

# Jalebee-消息页-内容Tab通用IDS([0]FOLLOWING/[1]YOU)
Source_JalebeeMessagePage_FeedTabCommon_IDS = "tv_tab_title"
JalebeeMessagePage_FeedTabCommon_IDS = package + FS(Source_JalebeeMessagePage_FeedTabCommon_IDS)

# Jalebee-消息页-消息内容
Source_JalebeeMessagePage_MessageContent_ID_IDS = "item_message_content"
JalebeeMessagePage_MessageContent_ID_IDS = package + FS(Source_JalebeeMessagePage_MessageContent_ID_IDS)

