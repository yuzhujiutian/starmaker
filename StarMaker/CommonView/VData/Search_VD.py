# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
gms = "com.google.android"


# ----------
# Search
# ----------
# Search页面-搜索-搜索框
Source_SearchPage_Search_SearchBox_ID = "imb_search"
SearchPage_Search_SearchBox_ID = package + mapping_dict[Source_SearchPage_Search_SearchBox_ID]

# Search页面-搜索-结果类型Tab([0]All/[1]Songs/...]
Source_SearchPage_Search_ResultType_IDS = "tv_tab_title"
SearchPage_Search_ResultType_IDS = package + mapping_dict[Source_SearchPage_Search_ResultType_IDS]

# ----------
# SongsSearch
# ----------
# Search页面-Songs搜索结果-歌曲名([0]第一首歌曲名/..]
Source_SearchPage_SongsSearchResult_SongsName_IDS = "tv_song"
SearchPage_SongsSearchResult_SongsName_IDS = package + mapping_dict[Source_SearchPage_SongsSearchResult_SongsName_IDS]

# Search页面-Songs搜索结果-歌曲点唱([0]第一首歌曲Sing/..]
Source_SearchPage_SongsSearchResult_SongsSingBtn_IDS = "lyt_sing"
SearchPage_SongsSearchResult_SongsSingBtn_IDS = package + \
                                                mapping_dict[Source_SearchPage_SongsSearchResult_SongsSingBtn_IDS]
