# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
gms = "com.google.android"


# ----------
# KTV大厅
# ----------
# KTV大厅-Tab-切换Tab
# ([0]Solo/[1]LIVE/[2]Multi_Guest/[3]Ranking]
Source_KtvPage_Tab_Common_IDS = "tv_tab_title"
KtvPage_Tab_Common_IDS = package + mapping_dict[Source_KtvPage_Tab_Common_IDS]

# KTV大厅-搜索-搜索房间
Source_KtvPage_Search_SearchRoom_ID = "imb_search"
KtvPage_Search_SearchRoom_ID = package + mapping_dict[Source_KtvPage_Search_SearchRoom_ID]

# KTV大厅-功能入口-通用
# ([0]My Room/[1]History/[2]Ranking]
Source_KtvPage_FunctionEntry_Common_IDS = "txt_title"
KtvPage_FunctionEntry_Common_IDS = package + mapping_dict[Source_KtvPage_FunctionEntry_Common_IDS]

# ----------
# KTV大厅-房间卡片
# ----------
# KTV大厅-房间卡片-封面图(ID/IDS]
Source_KtvPage_RoomCard_Cover_ID_IDS = "room_cover"
KtvPage_RoomCard_Cover_ID_IDS = package + mapping_dict[Source_KtvPage_RoomCard_Cover_ID_IDS]

# KTV大厅-房间卡片-守护天使(ID/IDS]
Source_KtvPage_RoomCard_Avatar_ID_IDS = "img_avatar"
KtvPage_RoomCard_Avatar_ID_IDS = package + mapping_dict[Source_KtvPage_RoomCard_Avatar_ID_IDS]


# KTV大厅-房间卡片-正在演唱歌曲(ID/IDS]
Source_KtvPage_RoomCard_SongName_ID_IDS = "txt_song"
KtvPage_RoomCard_SongName_ID_IDS = package + mapping_dict[Source_KtvPage_RoomCard_SongName_ID_IDS]

# KTV大厅-房间卡片-在线人数(ID/IDS]
Source_KtvPage_RoomCard_LiveNumber_ID_IDS = "txt_count"
KtvPage_RoomCard_LiveNumber_ID_IDS = package + mapping_dict[Source_KtvPage_RoomCard_LiveNumber_ID_IDS]


# KTV大厅-房间卡片-排麦人数(ID/IDS]
Source_KtvPage_RoomCard_LineUp_ID_IDS = "txt_order"
KtvPage_RoomCard_LineUp_ID_IDS = package + mapping_dict[Source_KtvPage_RoomCard_LineUp_ID_IDS]

# KTV大厅-房间卡片-房间等级(ID/IDS](暂无text属性]
Source_KtvPage_RoomCard_RoomLevel_ID_IDS = "img_room_level"
KtvPage_RoomCard_RoomLevel_ID_IDS = package + mapping_dict[Source_KtvPage_RoomCard_RoomLevel_ID_IDS]

# KTV大厅-房间卡片-房间名(ID/IDS]
Source_KtvPage_RoomCard_RoomName_ID_IDS = "txt_title"
KtvPage_RoomCard_RoomName_ID_IDS = package + mapping_dict[Source_KtvPage_RoomCard_RoomName_ID_IDS]

# ----------
# KTV大厅-房间卡片
# ----------
# KTV大厅-房间卡片-封面图(ID/IDS]
Source_LivePage_RoomCard_Cover_ID_IDS = "iv_img_cover"
LivePage_RoomCard_Cover_ID_IDS = package + mapping_dict[Source_LivePage_RoomCard_Cover_ID_IDS]
