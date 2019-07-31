# coding=utf-8
from StarMaker.Utils import Tools
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
gms = "com.google.android"

# ----------
# StartMaker的Moment页面
# ----------
# 首页进入到 Moment[0],Party[1],Sing[2],Message[3],Me[4]
Source_MomentPage_Tab_Moment_IDS = "tab_animation_view"
MomentPage_Tab_Moment_IDS = package + FS(Source_MomentPage_Tab_Moment_IDS)

# Moment界面 发布类型   Sing[0], Album[1], Camera[2], Text[3]
Source_Moment_Tab_MomentPublish_Sing_IDS = "tv_post_recording"
Moment_Tab_MomentPublish_Sing_IDS = package + FS(Source_Moment_Tab_MomentPublish_Sing_IDS)

# Moment 下的Following[0],Popular[1],Billboard[2],Nearby[3]
Source_Moment_Tab_MomentPopular_IDS = "tv_tab_title"
Moment_Tab_MomentPopular_IDS = package + FS(Source_Moment_Tab_MomentPopular_IDS)

# moment下的发布Post
Source_Moment_Tab_MomentPublish_ID = "iv_content_post"
Moment_Tab_MomentPublish_ID = package + FS(Source_Moment_Tab_MomentPublish_ID)

# moment-following下的第一个作品的文字
Source_MomentPublish_Function_SendSucText_ID = "tv_desc"
MomentPublish_Function_SendSucText_ID = package + FS(Source_MomentPublish_Function_SendSucText_ID)

# postText下的send
Source_MomentPublish_Function_Send_ID = "btn_next"
MomentPublish_Function_Send_ID = package + FS(Source_MomentPublish_Function_Send_ID)

# postAlbum下的Next
Source_MomentPublish_Function_AlbumNext_ID = "button_apply"
MomentPublish_Function_AlbumNext_ID = package + FS(Source_MomentPublish_Function_AlbumNext_ID)

# postAlbum下的Album
Source_Moment_MomentPublish_AlbumPage_ID = "selected_album"
Moment_MomentPublish_AlbumPage_ID = package + FS(Source_Moment_MomentPublish_AlbumPage_ID)

# moment下的发布Post返回上一页
Source_Moment_Function_Post_Back_Class = "android.widget.ImageButton"

# Post下返回-Discard
Source_Moment_Function_Post_DiscardElements_ClaS = "android.widget.Button"
Source_Moment_Function_Post_DiscardElements_IDS = "button2"
Moment_Function_Post_DiscardElements_IDS = package + FS(Source_Moment_Function_Post_DiscardElements_IDS)

# moment下发布-Album-选择图片
Source_Moment_MomentPublish_Album_CheckPicture_IDS = "check_view"
Moment_MomentPublish_Album_CheckPicture_IDS = package + FS(Source_Moment_MomentPublish_Album_CheckPicture_IDS)

# 发布页标识（图片，@符号，#号，地点标识）
MomentPublish_Function_CheckImageClaS = "android.widget.ImageView"

# Text-背景图-选择彩色图片
Source_TextPostPage_Function_BackPicture_IDS = "image_icon"
TextPostPage_Function_BackPicture_IDS = package + FS(Source_TextPostPage_Function_BackPicture_IDS)

# Text-彩色图片
Source_TextPostPage_Function_CheckBackPicture_ID = "writing_edit_txt_view"
TextPostPage_Function_CheckBackPicture_ID = package + FS(Source_TextPostPage_Function_CheckBackPicture_ID)

# Moment界面下的发布后的，在Following的加载条
# ----------------
# 发布人的头像
Source_MomentFollowing_Function_LoadAvatar_ID = "iv_cover"
MomentFollowing_Function_LoadAvatar_ID = package + FS(Source_MomentFollowing_Function_LoadAvatar_ID)

# 上传中提示
Source_MomentFollowing_Function_UploadingAvatar_ID = "iv_cover"
MomentFollowing_Function_UploadingAvatar_ID_ID = package + FS(Source_MomentFollowing_Function_UploadingAvatar_ID)

# 进度圈
Source_MomentFollowing_Function_ProgressBar_ID = "iv_cover"
MomentFollowing_Function_ProgressBar_ID = package + FS(Source_MomentFollowing_Function_ProgressBar_ID)



