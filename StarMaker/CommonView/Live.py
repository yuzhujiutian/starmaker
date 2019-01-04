# coding=utf-8
# ----------
# Live模块
# ----------
from Utils.FindElement import find_element
from CommonView.VData import Live_VD
from Utils.Tools import Popular_Elements_Disposes


# Live模块
class Live(object):
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
    # Live大厅
    # ----------
    # 用于校验IDS下TextList
    def LivePage_Tab_TabList(self):
        KtvPage_Tab_TabList = Live_VD.LivePage_Tab_Common_IDS
        return KtvPage_Tab_TabList

    # Live大厅-Tab-HOT
    def LivePage_Tab_HOT(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Live_VD.LivePage_Tab_Common_IDS, 3)
        return KtvPage_Tab_SwitchTab_IDS

    # Live大厅-Tab-SINGER
    def LivePage_Tab_SINGER(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Live_VD.LivePage_Tab_Common_IDS, 4)
        return KtvPage_Tab_SwitchTab_IDS

    # Live大厅-Tab-CHAT
    def LivePage_Tab_CHAT(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Live_VD.LivePage_Tab_Common_IDS, 5)
        return KtvPage_Tab_SwitchTab_IDS

    # Live大厅-Tab-TALENT
    def LivePage_Tab_TALENT(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Live_VD.LivePage_Tab_Common_IDS, 6)
        return KtvPage_Tab_SwitchTab_IDS

    # Live大厅-Tab-NEARBY
    def LivePage_Tab_NEARBY(self):
        KtvPage_Tab_SwitchTab_IDS = self.findIDS(Live_VD.LivePage_Tab_Common_IDS, 7)
        return KtvPage_Tab_SwitchTab_IDS

    # ----------
    # Live大厅-功能入口
    # ----------
    # Live大厅-功能入口-TopStars
    def LivePage_FunctionEntry_TopStars(self):
        LivePage_FunctionEntry_TopStars_ID = self.findID(Live_VD.LivePage_FunctionEntry_TopStars_ID)
        return LivePage_FunctionEntry_TopStars_ID

    # Live大厅-功能入口-TopGifters
    def LivePage_FunctionEntry_TopGifters(self):
        LivePage_FunctionEntry_TopGifters_ID = self.findID(Live_VD.LivePage_FunctionEntry_TopGifters_ID)
        return LivePage_FunctionEntry_TopGifters_ID

    # Live大厅-功能入口-StartLive
    def LivePage_FunctionEntry_StartLive(self):
        LivePage_FunctionEntry_StartLive_ID = self.findID(Live_VD.LivePage_FunctionEntry_StartLive_ID)
        return LivePage_FunctionEntry_StartLive_ID

    # Live大厅-Top榜单页面-TopStarsTab
    def LivePage_TopListPage_TopStarsTab(self):
        LivePage_TopListPage_Common_IDS = self.findIDS(Live_VD.LivePage_TopListPage_Common_IDS, 0)
        return LivePage_TopListPage_Common_IDS

    # Live大厅-Top榜单页面-TopGifters
    def LivePage_TopListPage_TopGiftersTab(self):
        LivePage_TopListPage_Common_IDS = self.findIDS(Live_VD.LivePage_TopListPage_Common_IDS, 1)
        return LivePage_TopListPage_Common_IDS

    # ----------
    # Live大厅-直播间卡片
    # ----------
    # Live大厅-直播间卡片-封面图(ID/IDS)
    def LivePage_LiveRoomCard_Cover(self):
        LivePage_LiveRoomCard_Cover_ID_IDS = self.ID_IDS(Live_VD.LivePage_LiveRoomCard_Cover_ID_IDS)
        return LivePage_LiveRoomCard_Cover_ID_IDS

    # Live大厅-直播间卡片-Hot值(ID/IDS)
    def LivePage_LiveRoomCard_HotValue(self):
        LivePage_LiveRoomCard_HotValue_ID_IDS = self.ID_IDS(Live_VD.LivePage_LiveRoomCard_HotValue_ID_IDS)
        return LivePage_LiveRoomCard_HotValue_ID_IDS

    # Live大厅-直播间卡片-直播间名(ID/IDS)
    def LivePage_LiveRoomCard_LiveRoomName(self):
        LivePage_LiveRoomCard_LiveRoomName_ID_IDS = self.ID_IDS(Live_VD.LivePage_LiveRoomCard_LiveRoomName_ID_IDS)
        return LivePage_LiveRoomCard_LiveRoomName_ID_IDS

    # Live大厅-直播间卡片-主播名(ID/IDS)
    def LivePage_LiveRoomCard_AnchorName(self):
        LivePage_LiveRoomCard_AnchorName_ID_IDS = self.ID_IDS(Live_VD.LivePage_LiveRoomCard_AnchorName_ID_IDS)
        return LivePage_LiveRoomCard_AnchorName_ID_IDS

    # Live大厅-直播间卡片-主播等级(ID/IDS)(暂无text属性)
    def LivePage_LiveRoomCard_AnchorLive(self):
        LivePage_LiveRoomCard_AnchorLive_ID_IDS = self.ID_IDS(Live_VD.LivePage_LiveRoomCard_AnchorLive_ID_IDS)
        return LivePage_LiveRoomCard_AnchorLive_ID_IDS

    # Live大厅-直播间卡片-守护天使(ID/IDS)
    def LivePage_LiveRoomCard_Avatar(self):
        LivePage_LiveRoomCard_Avatar_ID_IDS = self.ID_IDS(Live_VD.LivePage_LiveRoomCard_Avatar_ID_IDS)
        return LivePage_LiveRoomCard_Avatar_ID_IDS

    # ----------
    # Live开播页
    # ----------
    # Live开播页-GoLive按钮
    def StartLivePage_StartLive_GoLive(self):
        StartLivePage_StartLive_GoLive_ID = self.findID(Live_VD.StartLivePage_StartLive_GoLive_ID)
        return StartLivePage_StartLive_GoLive_ID
