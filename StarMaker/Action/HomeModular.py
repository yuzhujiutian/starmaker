# coding=utf-8
import time
import unittest
from CommonView.Home import Home
from CommonView.LogIn import LogIn
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver


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
    # 首页-切换Tab-点击底部HomeTab
    def test_Case001_HomePage_SwitchTab_SelectHomeTab(self):
        Home().HomePage_MainTab_HomeTab().click()
        time.sleep(2)
        # 获取HomeTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_HomeTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到HomeTab
        self.assertEqual(expValue, actValue)

    # 首页-切换Tab-点击底部DiscoverTab
    def test_Case002_HomePage_SwitchTab_SelectDiscoverTab(self):
        Home().HomePage_MainTab_DiscoverTab().click()
        time.sleep(2)
        # 获取DiscoverTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_DiscoverTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到DiscoverTab
        self.assertEqual(expValue, actValue)

    # 首页-切换Tab-点击底部PostTab
    def test_Case003_HomePage_SwitchTab_SelectPostTab(self):
        Home().HomePage_MainTab_PostTab().click()
        time.sleep(2)
        # 获取PostTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_PostTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PostTab
        self.assertEqual(expValue, actValue)

    # 首页-切换Tab-点击底部NotificationTab
    def test_Case004_HomePage_SwitchTab_SelectNotificationTab(self):
        Home().HomePage_MainTab_NotificationTab().click()
        time.sleep(2)
        # 获取NotificationTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_NotificationTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到NotificationTab
        self.assertEqual(expValue, actValue)

    # 首页-切换Tab-点击底部ProfileTab
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
    # 首页-游客点击ProfileTab
    def test_Case006_HomePage_Tourist_SelectProfileTab(self):
        Home().HomePage_MainTab_ProfileTab().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in before checking your profile."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)
