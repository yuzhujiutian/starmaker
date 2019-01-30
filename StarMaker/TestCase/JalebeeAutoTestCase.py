# coding=utf-8
import re
import time
import unittest
from CommonView.StartUp import StartUp
from CommonView.Jalebee import Jalebee
from CommonView.LogIn import LogIn
from Utils.Tools import Tools
from Utils.Tools import Page_Element_Verification
from Utils.ReadXMLData import ReadXMLData
from Utils.GetAppiumDeriver import GetAppiumDeriver


# Jalebee
class JalebeeAutoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)

    def setUp(self):
        time.sleep(2)

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # 语言选择页——页面元素校验
    def test_Case001_ChooseLanguagePage_CheckElement(self):
        # 预期结果
        TextList = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "ChooseLanguagePage")
        time.sleep(2)
        # 获取该页面所有元素
        actValue = Page_Element_Verification().PEV_ClaS(StartUp().ChooseLanguagePage_Check(), TextList)
        time.sleep(2)
        # 断言
        self.assertTrue(actValue)

    # 语言选择页——选择语言进入首页——校验底部Tab
    def test_Case002_SelectLanguage_CheckHomeMainTab(self):
        # 选择Hindi语进入首页
        StartUp().ChooseLanguagePage_SelectLanguage_SelectHindi().click()
        time.sleep(2)
        # 预期结果
        TextList = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "HomePageMainTab")
        time.sleep(2)
        # 获取该首页底部所有主Tab名
        actValue = Page_Element_Verification().PEV_ClaS(Jalebee().JalebeeHomePage_MainTab_Check(), TextList)
        time.sleep(2)
        # 断言
        self.assertTrue(actValue)

    # 首页——校验内容Tab
    def test_Case003_HomePage_CheckFeedTab(self):
        # 预期结果
        TextList = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "HomePageFeedTab")
        time.sleep(2)
        # 获取该首页顶部所有内容Tab名
        actValue = Page_Element_Verification().PEV_ClaS(Jalebee().JalebeeHomePage_FeedTab_Check(), TextList)
        time.sleep(2)
        # 断言
        self.assertTrue(actValue)

