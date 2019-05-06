# coding=utf-8
import time
import unittest
from StarMaker.CommonView.Parties import Parties
from StarMaker.Utils.Tools import Tools
from StarMaker.Utils.Tools import Page_Element_Verification
from StarMaker.Utils.ReadXMLData import ReadXMLData
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver


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

    # ----------
    # 顶部Tab切换
    # ----------
    # 切换至PartiesTab
    def test_Case3001_TopTab_SwitchTab_PARTIES(self):
        Parties().KtvPage_Tab_PARTIES().click()
        time.sleep(2)
        # 获取PartiesTab的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_PARTIES().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PartiesTab
        self.assertEqual(expValue, actValue)

    # 切换至LiveTab
    def test_Case3002_TopTab_SwitchTab_LIVE(self):
        Parties().KtvPage_Tab_LIVE().click()
        time.sleep(2)
        # 获取LiveTab的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_LIVE().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到LiveTab
        self.assertEqual(expValue, actValue)

    # 切换至DiscoverTab
    def test_Case3003_TopTab_SwitchTab_DISCOVER(self):
        Parties().KtvPage_Tab_DISCOVER().click()
        time.sleep(2)
        # 获取DiscoverTab的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_DISCOVER().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到DiscoverTab
        self.assertEqual(expValue, actValue)

    # ----------
    # KTV大厅
    # ----------
    # 检查当前页八个Tab加载正确
    def test_Case3004_KtvPage_InspectTab(self):
        # 获取Tab列表
        TextList = ReadXMLData().returnXMLFile("InspectTabList.xml", "InspectTabList", "KtvTabList")
        # 查看当前功能栏是否显示正确
        actValue = Page_Element_Verification().PEV_IDS(Parties().KtvPage_Tab_TabList(), TextList)
        self.assertTrue(actValue)

    # 切换至Hot
    def test_Case3005_KtvPage_SwitchTab_HOT(self):
        Parties().KtvPage_Tab_HOT().click()
        time.sleep(2)
        # 获取Hot的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_HOT().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到Hot
        self.assertEqual(expValue, actValue)

    # 切换至MULTI-GUEST
    def test_Case3006_KtvPage_SwitchTab_MULTIGUEST(self):
        Parties().KtvPage_Tab_MULTIGUEST().click()
        time.sleep(2)
        # 获取MULTI-GUEST的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_MULTIGUEST().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到MULTI-GUEST
        self.assertEqual(expValue, actValue)

    # 切换至COLLAB
    def test_Case3007_KtvPage_SwitchTab_COLLAB(self):
        Parties().KtvPage_Tab_COLLAB().click()
        time.sleep(2)
        # 获取COLLAB的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_COLLAB().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到COLLAB
        self.assertEqual(expValue, actValue)

    # 切换至QUEUE
    def test_Case3008_KtvPage_SwitchTab_QUEUE(self):
        Parties().KtvPage_Tab_QUEUE().click()
        time.sleep(2)
        # 获取QUEUE的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_QUEUE().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到QUEUE
        self.assertEqual(expValue, actValue)

    # 切换至FOLLOWING
    def test_Case3009_KtvPage_SwitchTab_FOLLOWING(self):
        Parties().KtvPage_Tab_FOLLOWING().click()
        time.sleep(2)
        # 获取FOLLOWING的selected属性
        expValue = "true"
        actValue = Parties().KtvPage_Tab_FOLLOWING().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到FOLLOWING
        self.assertEqual(expValue, actValue)

    # KTV大厅-搜索-搜索房间
    def test_Case3010_KtvPage_Search_SearchRoom(self):
        Parties().KtvPage_Search_SearchRoom().click()
        time.sleep(2)
        # 断言待补充

    # KTV大厅-功能入口-My Room
    def test_Case3011_KtvPage_FunctionEntry_MyRoom(self):
        Parties().KtvPage_FunctionEntry_MyRoom().click()
        time.sleep(2)
        # 断言待补充

    # KTV大厅-功能入口-History
    def test_Case3012_KtvPage_FunctionEntry_History(self):
        Parties().KtvPage_FunctionEntry_History().click()
        time.sleep(2)
        # 断言待补充

    # KTV大厅-功能入口-Ranking
    def test_Case3012_KtvPage_FunctionEntry_Ranking(self):
        Parties().KtvPage_FunctionEntry_Ranking().click()
        time.sleep(2)
        # 断言待补充

    # ----------
    # KTV大厅-房间卡片
    # ----------
    # KTV大厅-房间卡片-封面图
    def test_Case3013_KtvPage_RoomCard_Cover(self):
        Parties().KtvPage_RoomCard_Cover().click()
        time.sleep(2)
        # 断言待补充

    # KTV大厅-房间卡片-守护天使
    def test_Case3014_KtvPage_RoomCard_Avatar(self):
        Parties().KtvPage_RoomCard_Avatar().click()
        time.sleep(2)
        # 断言待补充

    # KTV大厅-房间卡片-正在演唱歌曲
    def test_Case3015_KtvPage_RoomCard_SongName(self):
        expValue = Parties().KtvPage_RoomCard_SongName().text
        time.sleep(2)
        # 断言待补充

    # KTV大厅-房间卡片-在线人数
    def test_Case3016_KtvPage_RoomCard_LiveNumber(self):
        expValue = Parties().KtvPage_RoomCard_LiveNumber().text
        time.sleep(2)
        # 断言待补充

    # KTV大厅-房间卡片-排麦人数
    def test_Case3017_KtvPage_RoomCard_LineUp(self):
        expValue = Parties().KtvPage_RoomCard_LineUp().text
        time.sleep(2)
        # 断言待补充

    # KTV大厅-房间卡片-房间等级(暂无text属性)
    def test_Case3018_KtvPage_RoomCard_RoomLevel(self):
        expValue = Parties().KtvPage_RoomCard_RoomLevel().text
        time.sleep(2)
        # 断言待补充

    # KTV大厅-房间卡片-房间名
    def test_Case3019_KtvPage_RoomCard_RoomName(self):
        expValue = Parties().KtvPage_RoomCard_RoomName().text
        time.sleep(2)
        # 断言待补充
