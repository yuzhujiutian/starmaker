# coding=utf-8
from StarMaker.Utils import Tools
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
# ----------
# 弹窗汇总
# ----------

# 通用——关闭弹窗
Source_Popup_ImgClose_ID = "img_close"
Popup_ImgClose_ID = package + FS(Source_Popup_ImgClose_ID)

# 通用——iv关闭弹窗
Source_Popup_IvClose_ID = "iv_close"
Popup_IvClose_ID = package + FS(Source_Popup_IvClose_ID)

# ----------
# 1>首页弹窗
# ----------
# JoinCollab引导，如果存在则点击关闭
Source_Popup_MadeForYou_ID = "tv_guide_title"
Popup_MadeForYou_ID = package + FS(Source_Popup_MadeForYou_ID)

# ①登录后首页 New Feature 引导（text=Only for your taste. Hope you love them./NEXT）
Popup_NewFeature_AU = "new UiSelector().text(\"Only for your taste. Hope you love them.\")"
Popup_NEXT = "new UiSelector().text(\"NEXT\")"
# ②登录后首页 New Feature Added 引导（text=New feature added. Tap to post your stories./NEXT）
Popup_NewFeatureAdded_AU = "new UiSelector().text(\"New feature added. Tap to post your stories.\")"
# ③登录后首页 Sing 引导（text=Sing is moved here. Tap to show your voice./NEXT）
Popup_NewFeatureSing_AU = "new UiSelector().text(\"Sing is moved here. Tap to show your voice.\")"
# ④登录后首页 PostOther 引导（text=Post Photo,Gif and Video here/DONE）
Popup_NewFeaturePostOther_AU = "new UiSelector().text(\"Post Photo,Gif and Video here\")"
Popup_DONE = "new UiSelector().text(\"DONE\")"

# 首页位置信息权限弹窗(text=要允许StarMaker获取此设备的位置信息吗？)
Popup_PermissionMessage_ID = "com.android.packageinstaller:id/permission_message"
Popup_PermissionMessage_Allow_ID = "com.android.packageinstaller:id/permission_allow_button"

# ②③登录后首页 Ranking/Parties 引导 文案（text="Ranking and Hashtag are moved here"/Parties are moved here）
Source_Popup_GuideText_ID = "content_tv"
Popup_Guide_Text_ID = package + FS(Source_Popup_GuideText_ID)

# ②③登录后首页 Ranking/Parties 引导 NEXT按钮/DONE按钮
Source_Popup_Guide_Next_ID = "next_tv"
Popup_Guide_Next_ID = package + FS(Source_Popup_Guide_Next_ID)

# 签到按钮，如果存在，需点击通用close按钮
Source_Popup_CheckIn_ID = "btn_check_in"
Popup_CheckIn_ID = package + FS(Source_Popup_CheckIn_ID)

# ----------
# 2>Profile页弹窗
# ----------

# 验证邮箱弹窗，如果存在，需点击通用close按钮
Source_Popup_VerifyEmail_Verify_ID = "tv_email_verify"
Popup_VerifyEmail_Verify_ID = package + FS(Source_Popup_VerifyEmail_Verify_ID)

# ----------
# 3>点唱页页弹窗
# ----------

# 发布图片引导(text=Click to post a photo)/发布图片+文字引导(text=Post texts with background photo.)
Source_Popup_PostGuide_ID = "text"
Popup_PostGuide_ID = package + FS(Source_Popup_PostGuide_ID)

# ----------
# 4>录制准备页
# ----------

# 权限申请(text=Ok, Let's do it.)
Source_Popup_Jurisdiction_ID = "permissionOkTv"
Popup_Jurisdiction_ID = package + FS(Source_Popup_Jurisdiction_ID)

# 总是允许
Popup_PermissionAllow_ID = "com.android.packageinstaller:id/permission_allow_button"

# 插入耳机引导(text=I KNOW)
Source_Popup_HeadphonesRecommended_ID = "recording_headset_dialog_i_know_btn"
Popup_HeadphonesRecommended_ID = package + FS(Source_Popup_HeadphonesRecommended_ID)

# 音效引导(text=Change the song's pitch to match \n your voice!)
Source_Popup_PitchGuide_ID = "tv_pitch_guide_tip"
Popup_PitchGuide_ID = package + FS(Source_Popup_PitchGuide_ID)

# ----------
# 5>KTV/Live
# ----------
# KTV排麦引导(text=Select a song, queue up and sing to gain your popularity!)
Popup_KTVPage_QueueUp_AU = "new UiSelector().text(\"Select a song, queue up and sing to gain your popularity!\")"

# Live滑动引导(text=Scroll up or down to change the live room)
Source_Popup_LivePage_Slide_ID = "tv_tips"
Popup_LivePage_Slide_ID = package + FS(Source_Popup_LivePage_Slide_ID)

# Live悬浮窗引导 拒绝按钮(text=REFUSE)
Source_Popup_LivePage_MinimizeOption_RefuseBtn_ID = "md_buttonDefaultNegative"
Popup_LivePage_MinimizeOption_RefuseBtn_ID = package + FS(Source_Popup_LivePage_MinimizeOption_RefuseBtn_ID)

# KTV悬浮窗引导 拒绝按钮(text=REFUSE)
Source_Popup_KTVPage_MinimizeOption_RefuseBtn_ID = "bt_left"
Popup_KTVPage_MinimizeOption_RefuseBtn_ID = package + FS(Source_Popup_KTVPage_MinimizeOption_RefuseBtn_ID)