# coding=utf-8
# ----------
# Search页
# ----------
from StarMaker.Utils.FindElement import find_element
from StarMaker.CommonView.VData import Search_VD


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

