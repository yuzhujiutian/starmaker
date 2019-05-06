# coding=utf-8
# ----------
# KTV模块
# ----------
from StarMaker.Utils.FindElement import find_element
from StarMaker.CommonView.VData import Parties_VD
from StarMaker.Utils.Tools import Popular_Elements_Disposes


# KTV模块
class Parties(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU
        self.ID_IDS = Popular_Elements_Disposes().ID_IDS

    # ----------
    # KTV大厅
    # ----------
    # 用于校验IDS下TextList
    def KtvPage_Tab_TabList(self):
        KtvPage_Tab_TabList = Parties_VD.KtvPage_Tab_Common_IDS
        return KtvPage_Tab_TabList

    # KTV大厅-Tab-PARTIES
    def KtvPage_Tab_PARTIES(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Parties_VD.KtvPage_Tab_Common_IDS, 0)
        return KtvPage_Tab_SwitchTab_IDS

    # KTV大厅-Tab-LIVE
    def KtvPage_Tab_LIVE(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Parties_VD.KtvPage_Tab_Common_IDS, 1)
        return KtvPage_Tab_SwitchTab_IDS

    # KTV大厅-Tab-DISCOVER
    def KtvPage_Tab_DISCOVER(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Parties_VD.KtvPage_Tab_Common_IDS, 2)
        return KtvPage_Tab_SwitchTab_IDS

    # KTV大厅-Tab-HOT
    def KtvPage_Tab_HOT(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Parties_VD.KtvPage_Tab_Common_IDS, 3)
        return KtvPage_Tab_SwitchTab_IDS

    # KTV大厅-Tab-MULTI-GUEST
    def KtvPage_Tab_MULTIGUEST(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Parties_VD.KtvPage_Tab_Common_IDS, 4)
        return KtvPage_Tab_SwitchTab_IDS

    # KTV大厅-Tab-COLLAB
    def KtvPage_Tab_COLLAB(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Parties_VD.KtvPage_Tab_Common_IDS, 5)
        return KtvPage_Tab_SwitchTab_IDS

    # KTV大厅-Tab-QUEUE
    def KtvPage_Tab_QUEUE(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Parties_VD.KtvPage_Tab_Common_IDS, 6)
        return KtvPage_Tab_SwitchTab_IDS

    # KTV大厅-Tab-FOLLOWING
    def KtvPage_Tab_FOLLOWING(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Parties_VD.KtvPage_Tab_Common_IDS, 7)
        return KtvPage_Tab_SwitchTab_IDS

    # KTV大厅-搜索-搜索房间
    def KtvPage_Search_SearchRoom(self):
        KtvPage_Search_SearchRoom_ID = self.findID(Parties_VD.KtvPage_Search_SearchRoom_ID)
        return KtvPage_Search_SearchRoom_ID

    # KTV大厅-功能入口-My Room
    def KtvPage_FunctionEntry_MyRoom(self):
        KtvPage_FunctionEntry_Common_IDS = self.findIDS(Parties_VD.KtvPage_FunctionEntry_Common_IDS, 0)
        return KtvPage_FunctionEntry_Common_IDS

    # KTV大厅-功能入口-History
    def KtvPage_FunctionEntry_History(self):
        KtvPage_FunctionEntry_Common_IDS = self.findIDS(Parties_VD.KtvPage_FunctionEntry_Common_IDS, 1)
        return KtvPage_FunctionEntry_Common_IDS

    # KTV大厅-功能入口-Ranking
    def KtvPage_FunctionEntry_Ranking(self):
        KtvPage_FunctionEntry_Common_IDS = self.findIDS(Parties_VD.KtvPage_FunctionEntry_Common_IDS, 2)
        return KtvPage_FunctionEntry_Common_IDS

    # ----------
    # KTV大厅-房间卡片
    # ----------
    # KTV大厅-房间卡片-封面图(ID/IDS)
    def KtvPage_RoomCard_Cover(self):
        KtvPage_RoomCard_Cover_ID_IDS = self.ID_IDS(Parties_VD.KtvPage_RoomCard_Cover_ID_IDS)
        return KtvPage_RoomCard_Cover_ID_IDS

    # KTV大厅-房间卡片-守护天使(ID/IDS)
    def KtvPage_RoomCard_Avatar(self):
        KtvPage_RoomCard_Avatar_ID_IDS = self.ID_IDS(Parties_VD.KtvPage_RoomCard_Avatar_ID_IDS)
        return KtvPage_RoomCard_Avatar_ID_IDS

    # KTV大厅-房间卡片-正在演唱歌曲(ID/IDS)
    def KtvPage_RoomCard_SongName(self):
        KtvPage_RoomCard_SongName_ID_IDS = self.ID_IDS(Parties_VD.KtvPage_RoomCard_SongName_ID_IDS)
        return KtvPage_RoomCard_SongName_ID_IDS

    # KTV大厅-房间卡片-在线人数(ID/IDS)
    def KtvPage_RoomCard_LiveNumber(self):
        KtvPage_RoomCard_LiveNumber_ID_IDS = self.ID_IDS(KtvPage_RoomCard_LiveNumber_ID_IDS)
        return KtvPage_RoomCard_LiveNumber_ID_IDS

    # KTV大厅-房间卡片-排麦人数(ID/IDS)
    def KtvPage_RoomCard_LineUp(self):
        KtvPage_RoomCard_LineUp_ID_IDS = self.ID_IDS(Parties_VD.KtvPage_RoomCard_LineUp_ID_IDS)
        return KtvPage_RoomCard_LineUp_ID_IDS

    # KTV大厅-房间卡片-房间等级(ID/IDS)(暂无text属性)
    def KtvPage_RoomCard_RoomLevel(self):
        KtvPage_RoomCard_RoomLevel_ID_IDS = self.ID_IDS(Parties_VD.KtvPage_RoomCard_RoomLevel_ID_IDS)
        return KtvPage_RoomCard_RoomLevel_ID_IDS

    # KTV大厅-房间卡片-房间名(ID/IDS)
    def KtvPage_RoomCard_RoomName(self):
        KtvPage_RoomCard_RoomName_ID_IDS = self.ID_IDS(Parties_VD.KtvPage_RoomCard_RoomName_ID_IDS)
        return KtvPage_RoomCard_RoomName_ID_IDS
