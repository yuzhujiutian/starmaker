# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FindSource = Tools.Tools().FindSource
# ----------
# 弹窗汇总
# ----------

# 通用——关闭弹窗
Source_Popup_ImgClose_ID = "img_close"
Popup_ImgClose_ID = package + FindSource(Source_Popup_ImgClose_ID)

# ----------
# 1>首页弹窗
# ----------

# ①登陆后首页 New Feature 引导（text=Only for your taste. Hope you love them./NEXT）
Popup_NewFeature_AU = "new UiSelector().text(\"Only for your taste. Hope you love them.\")"
Popup_NEXT = "new UiSelector().text(\"NEXT\")"
# ②③登陆后首页 Ranking/Parties 引导 文案（text="Ranking and Hashtag are moved here"/Parties are moved here）
Source_Popup_GuideText_ID = "content_tv"
Popup_Guide_Text_ID = package + FindSource(Source_Popup_GuideText_ID)

# ②③登陆后首页 Ranking/Parties 引导 NEXT按钮/DONE按钮
Source_Popup_Guide_Next_ID = "next_tv"
Popup_Guide_Next_ID = package + FindSource(Source_Popup_Guide_Next_ID)

# 签到按钮，如果存在，需点击通用close按钮
Source_Popup_CheckIn_ID = "btn_check_in"
Popup_CheckIn_ID = package + FindSource(Source_Popup_CheckIn_ID)

# ----------
# 2>Profile页弹窗
# ----------

# 验证邮箱弹窗，如果存在，需点击通用close按钮
Source_Popup_VerifyEmail_Verify_ID = "tv_email_verify"
Popup_VerifyEmail_Verify_ID = package + FindSource(Source_Popup_VerifyEmail_Verify_ID)

# ----------
# 3>点唱页页弹窗
# ----------

# 发布图片引导(text=Click to post a photo)/发布图片+文字引导(text=Post texts with background photo.)
Source_Popup_PostGuide_ID = "text"
Popup_PostGuide_ID = package + FindSource(Source_Popup_PostGuide_ID)

# ----------
# 4>录制准备页
# ----------

# 权限申请(text=Ok, Let's do it.)
Source_Popup_Jurisdiction_ID = "permissionOkTv"
Popup_Jurisdiction_ID = package + FindSource(Source_Popup_Jurisdiction_ID)

# 总是允许
Popup_PermissionAllow_ID = "permission_allow_button"

# 插入耳机引导(text=I KNOW)
Source_Popup_HeadphonesRecommended_ID = "recording_headset_dialog_i_know_btn"
Popup_HeadphonesRecommended_ID = package + FindSource(Source_Popup_HeadphonesRecommended_ID)

# 音效引导(text=Change the song's pitch to match \n your voice!)
Source_Popup_PitchGuide_ID = "tv_pitch_guide_tip"
Popup_PitchGuide_ID = package + FindSource(Source_Popup_PitchGuide_ID)
