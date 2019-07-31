# coding=utf-8
from StarMaker.Utils import Tools
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
gms = "com.google.android"


# ----------
# Live大厅
# ----------
# Live大厅-Tab-切换Tab
# ([0]PARTIES/[1]LIVE/[2]DISCOVER/[3]HOT/[4]SINGER/[5]CHAT/[6]TALENT/[7]NEARBY)
Source_LivePage_Tab_Common_IDS = "tv_tab_title"
LivePage_Tab_Common_IDS = package + FS(Source_LivePage_Tab_Common_IDS)

# Live大厅-功能入口-TopStars
Source_LivePage_FunctionEntry_TopStars_ID = "llyt_live_hall_home_item_top_stars"
LivePage_FunctionEntry_TopStars_ID = package + FS(Source_LivePage_FunctionEntry_TopStars_ID)

# Live大厅-功能入口-TopGifters
Source_LivePage_FunctionEntry_TopGifters_ID = "llyt_live_hall_home_item_top_gifters"
LivePage_FunctionEntry_TopGifters_ID = package + FS(Source_LivePage_FunctionEntry_TopGifters_ID)

# Live大厅-功能入口-StartLive
Source_LivePage_FunctionEntry_StartLive_ID = "btn_start_live"
LivePage_FunctionEntry_StartLive_ID = package + FS(Source_LivePage_FunctionEntry_StartLive_ID)

# Live大厅-([0]TopStars/[1]TopGifters)
Source_LivePage_TopListPage_Common_IDS = "tv_tab_title"
LivePage_TopListPage_Common_IDS = package + FS(Source_LivePage_TopListPage_Common_IDS)

# ----------
# Live大厅-直播间卡片
# ----------
# Live大厅-直播间卡片-封面图(ID/IDS)
Source_LivePage_LiveRoomCard_Cover_ID_IDS = "iv_img_cover"
LivePage_LiveRoomCard_Cover_ID_IDS = package + FS(Source_LivePage_LiveRoomCard_Cover_ID_IDS)

# Live大厅-直播间卡片-Hot值(ID/IDS)
Source_LivePage_LiveRoomCard_HotValue_ID_IDS = "tv_hot_num_tv"
LivePage_LiveRoomCard_HotValue_ID_IDS = package + FS(Source_LivePage_LiveRoomCard_HotValue_ID_IDS)

# Live大厅-直播间卡片-直播间名(ID/IDS)
Source_LivePage_LiveRoomCard_LiveRoomName_ID_IDS = "tv_live_hall_item_title"
LivePage_LiveRoomCard_LiveRoomName_ID_IDS = package + FS(Source_LivePage_LiveRoomCard_LiveRoomName_ID_IDS)

# Live大厅-直播间卡片-主播名(ID/IDS)
Source_LivePage_LiveRoomCard_AnchorName_ID_IDS = "tv_host_name"
LivePage_LiveRoomCard_AnchorName_ID_IDS = package + FS(Source_LivePage_LiveRoomCard_AnchorName_ID_IDS)

# Live大厅-直播间卡片-主播等级(ID/IDS)(暂无text属性)
Source_LivePage_LiveRoomCard_AnchorLive_ID_IDS = "iv_host_level"
LivePage_LiveRoomCard_AnchorLive_ID_IDS = package + FS(Source_LivePage_LiveRoomCard_AnchorLive_ID_IDS)

# Live大厅-直播间卡片-守护天使(ID/IDS)
Source_LivePage_LiveRoomCard_Avatar_ID_IDS = "civ_head_view"
LivePage_LiveRoomCard_Avatar_ID_IDS = package + FS(Source_LivePage_LiveRoomCard_Avatar_ID_IDS)

# ----------
# Live开播页
# ----------
# Live开播页-GoLive按钮
Source_StartLivePage_StartLive_GoLive_ID = "txv_start_live_content"
StartLivePage_StartLive_GoLive_ID = package + FS(Source_StartLivePage_StartLive_GoLive_ID)
