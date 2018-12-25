# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
# ----------
# 首页
# ----------

# 首页-Popular-Text([2]English_text=POPULAR)
HomePage_Popular_Text_ClaS = "android.widget.TextView"

# 首页-HotTopics-Text(English_text=Hot topics)
Source_HomePage_HotTopics_Text_ID = "txt_trend_recommend_title"
HomePage_HotTopics_Text_ID = package + FS(Source_HomePage_HotTopics_Text_ID)

# 首页-HotTopics-SeeAll(English_text=SEE ALL)
Source_HomePage_HotTopics_SeeAll_ID = "txt_trend_recommend_action"
HomePage_HotTopics_SeeAll_ID = package + FS(Source_HomePage_HotTopics_SeeAll_ID)

# 首页-feed卡片_Follow(English_text=FOLLOW)(ID/IDS)
Source_HomePage_FeedCard_Follow_ID_IDS = "v_follow"
HomePage_FeedCard_Follow_ID_IDS = package + FS(Source_HomePage_FeedCard_Follow_ID_IDS)

# 首页-feed卡片_叉号(ID/IDS)
Source_HomePage_FeedCard_Dislike_ID_IDS = "close_tweet"
HomePage_FeedCard_Dislike_ID_IDS = package + FS(Source_HomePage_FeedCard_Dislike_ID_IDS)

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





