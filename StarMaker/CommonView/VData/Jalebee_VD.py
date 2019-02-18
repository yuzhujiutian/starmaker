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
Source_JalebeeShotPage_Start_Btn_ID = "rbtn_record_capturelib_fragment_capture"
JalebeeShotPage_Start_Btn_ID = package + FS(Source_JalebeeShotPage_Start_Btn_ID)

# Jalebee-拍摄页-选择音乐引导
Source_JalebeeShotPage_Guide_AddMusic_ID = "tv_tip_capturelib_popupwindow_add_bgm_guide"
JalebeeShotPage_Guide_AddMusic_ID = package + FS(Source_JalebeeShotPage_Guide_AddMusic_ID)
