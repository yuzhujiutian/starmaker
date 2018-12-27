# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
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
Source_HomePage_FeedCard_Img_ID_IDS = "img_cover"
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
# 首页-底部五个Tab
# ----------
# 首页-底部五个Tab([0]feed流/[1]互娱页/[2]点唱页/[3]消息页/[4]个人页)
HomePage_MainTab_ClaS = "android.support.v7.app.ActionBar$Tab"
