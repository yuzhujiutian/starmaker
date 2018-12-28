# coding=utf-8
import time
import unittest
from CommonView.Parties import Parties
from Utils.Tools import Tools
from Utils.Tools import Screen
from Utils.Tools import Page_Element_Verification
from Utils.ReadXMLData import ReadXMLData
from Utils.GetAppiumDeriver import GetAppiumDeriver


# 启动模块
class PartiesModular(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)

    def setUp(self):
        pass

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # 切换至PartiesTab
    def test_Case3001_KtvPage_SwitchTab_PARTIES(self):
        Parties().KtvPage_Tab_PARTIES().click()
        time.sleep(2)
        # 获取PartiesTab的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_PARTIES().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PartiesTab
        self.assertEqual(expValue, actValue)

    # 检查当前页八个Tab加载正确
    def test_Case3002_KtvPage_InspectTab(self):
        # 获取Tab列表
        TextList = ReadXMLData().returnXMLFile("KtvText.xml", "KtvText", "Tab_TextList1")
        # 查看当前功能栏是否显示正确
        actValue = Page_Element_Verification().PEV_IDS(Parties().KtvPage_Tab_TabList(), TextList)
        self.assertTrue(actValue)

    # ----------
    # KTV大厅
    # ----------
    # KTV大厅-Tab-PARTIES
    def KtvPage_Tab_PARTIES(self):
        pass

    # KTV大厅-Tab-LIVE
    def KtvPage_Tab_LIVE(self):
        pass

    # KTV大厅-Tab-DISCOVER
    def KtvPage_Tab_DISCOVER(self):
        pass

    # KTV大厅-Tab-HOT
    def KtvPage_Tab_HOT(self):
        pass

    # KTV大厅-Tab-MULTI-GUEST
    def KtvPage_Tab_MULTIGUEST(self):
        pass

    # KTV大厅-Tab-COLLAB
    def KtvPage_Tab_COLLAB(self):
        pass

    # KTV大厅-Tab-QUEUE
    def KtvPage_Tab_QUEUE(self):
        pass

    # KTV大厅-Tab-FOLLOWING
    def KtvPage_Tab_FOLLOWING(self):
        pass

    # KTV大厅-搜索-搜索房间
    def KtvPage_Search_SearchRoom(self):
        pass

    # KTV大厅-功能入口-My Room
    def KtvPage_FunctionEntry_MyRoom(self):
        pass

    # KTV大厅-功能入口-History
    def KtvPage_FunctionEntry_History(self):
        pass

    # KTV大厅-功能入口-Ranking
    def KtvPage_FunctionEntry_Ranking(self):
        pass

    # ----------
    # KTV大厅-房间卡片
    # ----------
    # KTV大厅-房间卡片-封面图(ID/IDS)
    def KtvPage_RoomCard_Cover(self):
        pass

    # KTV大厅-房间卡片-守护天使(ID/IDS)
    def KtvPage_RoomCard_Avatar(self):
        pass

    # KTV大厅-房间卡片-正在演唱歌曲(ID/IDS)
    def KtvPage_RoomCard_SongName(self):
        pass

    # KTV大厅-房间卡片-在线人数(ID/IDS)
    def KtvPage_RoomCard_LiveNumber(self):
        pass

    # KTV大厅-房间卡片-排麦人数(ID/IDS)
    def KtvPage_RoomCard_LineUp(self):
        pass

    # KTV大厅-房间卡片-房间等级(ID/IDS)(暂无text属性)
    def KtvPage_RoomCard_RoomLevel(self):
        pass

    # KTV大厅-房间卡片-房间名(ID/IDS)
    def KtvPage_RoomCard_RoomName(self):
        pass
