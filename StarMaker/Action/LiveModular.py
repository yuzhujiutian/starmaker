# coding=utf-8
import time
import unittest
from CommonView.Live import Live
from CommonView.Popup import Popup
from Utils.Tools import Tools
from Utils.Tools import Page_Element_Verification
from Utils.ReadXMLData import ReadXMLData
from Utils.GetAppiumDeriver import GetAppiumDeriver


# 启动模块
class LiveModular(unittest.TestCase):
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
    # Live大厅
    # ----------
    # 检查当前页八个Tab加载正确
    def test_Case4001_LivePage_InspectTab(self):
        # 获取Tab列表
        TextList = ReadXMLData().returnXMLFile("InspectTabList.xml", "InspectTabList", "LiveTabList")
        # 查看当前功能栏是否显示正确
        actValue = Page_Element_Verification().PEV_IDS(Live().LivePage_Tab_TabList(), TextList)
        self.assertTrue(actValue)

    # 切换至HOT
    def test_Case4002_LivePage_SwitchTab_HOT(self):
        Live().LivePage_Tab_HOT().click()
        time.sleep(2)
        # 获取Hot的selected属性
        expValue = "true"
        actValue = Live().LivePage_Tab_HOT().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到Hot
        self.assertEqual(expValue, actValue)

    # 切换至SINGER
    def test_Case4003_LivePage_SwitchTab_SINGER(self):
        Live().LivePage_Tab_SINGER().click()
        time.sleep(2)
        # 获取SINGER的selected属性
        expValue = "true"
        actValue = Live().LivePage_Tab_SINGER().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到SINGER
        self.assertEqual(expValue, actValue)

    # 切换至CHAT
    def test_Case4004_LivePage_SwitchTab_CHAT(self):
        Live().LivePage_Tab_CHAT().click()
        time.sleep(2)
        # 获取CHAT的selected属性
        expValue = "true"
        actValue = Live().LivePage_Tab_CHAT().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到CHAT
        self.assertEqual(expValue, actValue)

    # 切换至TALENT
    def test_Case4005_LivePage_SwitchTab_TALENT(self):
        Live().LivePage_Tab_TALENT().click()
        time.sleep(2)
        # 获取TALENT的selected属性
        expValue = "true"
        actValue = Live().LivePage_Tab_TALENT().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到TALENT
        self.assertEqual(expValue, actValue)

    # 切换至NEARBY
    def test_Case4006_LivePage_SwitchTab_NEARBY(self):
        Live().LivePage_Tab_NEARBY().click()
        time.sleep(2)
        # 获取NEARBY的selected属性
        expValue = "true"
        actValue = Live().LivePage_Tab_NEARBY().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到NEARBY
        self.assertEqual(expValue, actValue)

    # ----------
    # Live大厅-功能入口
    # ----------
    # Live大厅-功能入口-TopStars
    def test_Case4007_LivePage_FunctionEntry_TopStars(self):
        Live().LivePage_FunctionEntry_TopStars().click()
        time.sleep(2)
        # 获取Top榜单页面TopStarsTab的selected属性
        expValue = "true"
        actValue = Live().LivePage_TopListPage_TopStarsTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已跳转到Top榜单页面TopStars
        self.assertEqual(expValue, actValue)

    # Live大厅-功能入口-TopGifters
    def test_Case4008_LivePage_FunctionEntry_TopGifters(self):
        Live().LivePage_FunctionEntry_TopGifters().click()
        time.sleep(2)
        # 获取Top榜单页面TopGiftersTab的selected属性
        expValue = "true"
        actValue = Live().LivePage_TopListPage_TopGiftersTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已跳转到Top榜单页面TopGifters
        self.assertEqual(expValue, actValue)

    # Live大厅-功能入口-StartLive
    def test_Case4009_LivePage_FunctionEntry_StartLive(self):
        Live().LivePage_FunctionEntry_StartLive().click()
        time.sleep(2)
        # 权限弹窗处理，存在则点击允许，否则跳过
        Popup().SingPopup_Jurisdiction_LiveClick()
        # 获取开播页面GoLive的text属性
        expValue = "GO LIVE"
        actValue = Live().StartLivePage_StartLive_GoLive().text
        time.sleep(2)
        # 断言：已跳转到开播页
        self.assertEqual(expValue, actValue)



    # ----------
    # Live大厅-直播间卡片
    # ----------
    # Live大厅-直播间卡片-封面图(ID/IDS)
    def test_Case4010_LivePage_LiveRoomCard_Cover(self):
        Live().LivePage_LiveRoomCard_Cover().click()
        time.sleep(2)
        # 断言待补充

    # Live大厅-直播间卡片-守护天使(ID/IDS)
    def test_Case4011_LivePage_LiveRoomCard_Avatar(self):
        Live().LivePage_LiveRoomCard_Avatar().click()
        time.sleep(2)
        # 断言待补充

    # Live大厅-直播间卡片-Hot值(ID/IDS)
    def test_Case4012_LivePage_LiveRoomCard_HotValue(self):
        expValue = Live().LivePage_LiveRoomCard_HotValue().text
        time.sleep(2)
        # 断言待补充

    # Live大厅-直播间卡片-直播间名(ID/IDS)
    def test_Case4013_LivePage_LiveRoomCard_LiveRoomName(self):
        expValue = Live().LivePage_LiveRoomCard_LiveRoomName().text
        time.sleep(2)
        # 断言待补充

    # Live大厅-直播间卡片-主播名(ID/IDS)
    def test_Case4014_LivePage_LiveRoomCard_AnchorName(self):
        expValue = Live().LivePage_LiveRoomCard_AnchorName().text
        time.sleep(2)
        # 断言待补充

    # Live大厅-直播间卡片-主播等级(ID/IDS)(暂无text属性)
    def test_Case4015_LivePage_LiveRoomCard_AnchorLive(self):
        expValue = Live().LivePage_LiveRoomCard_AnchorLive().text
        time.sleep(2)
        # 断言待补充


