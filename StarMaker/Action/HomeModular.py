# coding=utf-8
import time
import unittest
from CommonView.Home import Home
from CommonView.LogIn import LogIn
from CommonView.HotTopics import HotTopics
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.Tools import ToastTips_Processing


# 默认首页
class HomeModular(unittest.TestCase):
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
    # 首页-MainTab
    # ----------
    # 首页-切换到HomeTab
    def test_Case001_HomePage_SwitchTab_SelectHomeTab(self):
        Home().HomePage_MainTab_HomeTab().click()
        time.sleep(2)
        # 获取HomeTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_HomeTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到HomeTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到DiscoverTab
    def test_Case002_HomePage_SwitchTab_SelectDiscoverTab(self):
        Home().HomePage_MainTab_DiscoverTab().click()
        time.sleep(2)
        # 获取DiscoverTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_DiscoverTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到DiscoverTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到PostTab
    def test_Case003_HomePage_SwitchTab_SelectPostTab(self):
        Home().HomePage_MainTab_PostTab().click()
        time.sleep(2)
        # 获取PostTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_PostTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PostTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到NotificationTab
    def test_Case004_HomePage_SwitchTab_SelectNotificationTab(self):
        Home().HomePage_MainTab_NotificationTab().click()
        time.sleep(2)
        # 获取NotificationTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_NotificationTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到NotificationTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到ProfileTab
    def test_Case005_HomePage_SwitchTab_SelectProfileTab(self):
        Home().HomePage_MainTab_ProfileTab().click()
        time.sleep(2)
        # 获取ProfileTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_ProfileTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到ProfileTab
        self.assertEqual(expValue, actValue)

    # ----------
    # 首页-游客点击MainTab
    # ----------
    # 首页-游客点击ProfileTab-调起登录弹窗
    def test_Case006_HomePage_Tourist_ProfileTabInlet(self):
        Home().HomePage_MainTab_ProfileTab().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in before checking your profile."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # 首页-游客点击Post-调起登录弹窗
    def test_Case007_HomePage_Tourist_PostTabInlet(self):
        Home().HomePage_MainTab_PostTab().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in to make a post."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # 首页-游客点击Notification-调起登录弹窗
    def test_Case008_HomePage_Tourist_NotificationTabInlet(self):
        Home().HomePage_MainTab_NotificationTab().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in before checking the latest news."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # ----------
    # 首页-Hot topics
    # ----------
    # 首页Hot topics正常显示
    def test_Case009_HomePage_HotTopics_Existence(self):
        # 获取Hot topics的text
        expValue = "Hot topics"
        actValue = Home().HomePage_HotTopics_Text().text
        time.sleep(2)
        # 断言：首页Hot topics正常显示
        self.assertEqual(expValue, actValue)

    # 首页点击Hot topics的See All
    def test_Case010_HomePage_HotTopics_SeeAll(self):
        Home().HomePage_HotTopics_SeeAll().click()
        time.sleep(2)
        # 获取Hot topics页面的title
        expValue = "Hot Topics"
        actValue = HotTopics().HotTopicsPage_Title_Text().text
        time.sleep(2)
        # 断言：已跳转到Hot Topics页面
        self.driver.back()
        self.assertEqual(expValue, actValue)

    # ----------
    # 首页卡片
    # ----------

    # 首页卡片-Follow成功(点击第一个)
    def test_Case011_HomePage_FeedCard_Follow(self):
        Follow_Count_1 = Home().HomePage_FeedCard_FollowCount()
        time.sleep(2)
        if Follow_Count_1 == 1:
            Home().HomePage_FeedCard_Follow().click()
            time.sleep(2)
            # 检查Follow按钮是否存在
            actValue = Home().HomePage_FeedCard_Follow()
            time.sleep(2)
            # 断言：Follow成功
            self.assertFalse(actValue)
        else:
            Home().HomePage_FeedCard_Follow().click()
            time.sleep(2)
            # 检查当前页Follow按钮个数是否-1
            Follow_Count_2 = Home().HomePage_FeedCard_FollowCount()
            expValue = 1
            actValue = Follow_Count_2 - Follow_Count_1
            # 断言：Follow成功
            self.assertEqual(expValue, actValue)

    # 首页卡片，点击叉号调起dislike对话框(点击第一个)
    def test_Case012_HomePage_FeedCard_Dislike(self):
        Home().HomePage_FeedCard_Dislike().click()
        time.sleep(2)
        # 获取dislike对话框的CancelText
        expValue = "Cancel"
        actValue = Home().HomePage_DislikePop_Cancel().text
        time.sleep(2)
        # 断言：已调起dislike对话框
        self.assertEqual(expValue, actValue)

    # 首页卡片，Unwanted
    def test_Case013_HomePage_FeedCard_Unwanted(self):
        Home().HomePage_DislikePop_Unwanted().click()
        time.sleep(2)
        # 循环查找toast提示
        expValue = "You will see fewer similar posts."
        actValue = ToastTips_Processing().ToastTips_TextXpath_IsDisplayed(expValue)
        time.sleep(2)
        # 断言：Unwanted成功
        self.assertTrue(actValue)
