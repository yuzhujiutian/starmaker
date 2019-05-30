# coding=utf-8
# ----------
# Search页
# ----------
from StarMaker.CommonView.VData import Search_VD
from StarMaker.Utils.FindElement import find_element


# 个人页
class Search(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findAU = find_element().AU

    # ----------
    # Search
    # ----------
    # Search页面-搜索-搜索框
    def SearchPage_Search_SearchBox(self):
        SearchPage_Search_SearchBox_ID = self.findID(Search_VD.SearchPage_Search_SearchBox_ID)
        return SearchPage_Search_SearchBox_ID

    # Search页面-搜索-结果类型Tab-Songs([0]All/[1]Songs/...)
    def SearchPage_Search_SongsType(self):
        SearchPage_Search_ResultType_IDS = self.findIDS(Search_VD.SearchPage_Search_ResultType_IDS, 1)
        return SearchPage_Search_ResultType_IDS

    # ----------
    # SongsSearch
    # ----------
    # Search页面-Songs搜索结果-第一首歌曲名
    def SearchPage_SongsSearchResult_FirstSongName(self):
        SearchPage_SongsSearchResult_SongsName_IDS = self.findIDS(Search_VD.SearchPage_SongsSearchResult_SongsName_IDS, 0)
        return SearchPage_SongsSearchResult_SongsName_IDS

    # Search页面-Songs搜索结果-歌曲点唱
    def SearchPage_SongsSearchResult_FirstSongSingBtn(self):
        SearchPage_SongsSearchResult_SongsSingBtn_IDS = self.findIDS(Search_VD.SearchPage_SongsSearchResult_SongsSingBtn_IDS, 0)
        return SearchPage_SongsSearchResult_SongsSingBtn_IDS
