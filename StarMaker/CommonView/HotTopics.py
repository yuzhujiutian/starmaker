# coding=utf-8
# ----------
# HotTopics页
# ----------
from Utils.FindElement import find_element
from CommonView.VData import HotTopics_VD


# HotTopics页
class HotTopics(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU

    # HotTopics页面-Title-Text([0]English_text=Hot Topics)
    def HotTopicsPage_Title_Text(self):
        HotTopicsPage_Title_Text_ClaS = self.findClaS(HotTopics_VD.HotTopicsPage_Title_Text_ClaS, 0)
        return HotTopicsPage_Title_Text_ClaS

    # HotTopics页面-HotTopics_TopicsName
    def HotTopicsPage_HotTopics_TopicsName_Single(self, num):
        HotTopicsPage_HotTopics_TopicsName_IDS = self.findIDS(HotTopics_VD.HotTopicsPage_HotTopics_TopicsName_IDS, num)
        return HotTopicsPage_HotTopics_TopicsName_IDS
