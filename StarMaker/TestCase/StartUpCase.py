# coding=utf-8
import time
import unittest
from CommonView.StartUp import StartUp
from CommonView.Home import Home
from Utils.Tools import Tools
from Utils.Tools import Screen
from Utils.GetAppiumDeriver import GetAppiumDeriver


class StarUpCase(unittest.TestCase):
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

    # 启动APP
    def test_Case001_ChooseLanguagePage_CheckStartSuccess_Tips(self):
        expValue = "Choose Language"
        # 获取语言选择页Tips文案
        actValue = StartUp().ChooseLanguagePage_CheckStartSuccess_Tips().text
        time.sleep(2)
        # 断言：页面顶部Tips文案是"Choose Language"
        self.assertEqual(expValue, actValue)

    # 选择印地语进入Popular页
    def test_Case002_ChooseLanguagePage_SelectLanguage_SelectEnglish(self):
        # 选择Hindi语言
        if StartUp().ChooseLanguagePage_SelectLanguage_SelectHindi().text == "हिन्दी":
            StartUp().ChooseLanguagePage_SelectLanguage_SelectHindi().click()
            time.sleep(3)
        else:
            Tools().get_images()
            return ValueError
        expValue = "लोकप्रिय"
        # 获取首页Popular文案(Hindi_text=लोकप्रिय)
        actValue = Home().HomePage_Popular_Text().text
        time.sleep(2)
        # 断言：校验首页Popular文案为印地语
        self.assertEqual(expValue, actValue)

    # 选择英语进入Popular页
    def test_Case003_ChooseLanguagePage_SelectLanguage_SelectEnglish(self):
        # 向上滑动1/2屏幕
        Screen().SWipeUp_Half()
        time.sleep(2)
        # 选择English语言
        if StartUp().ChooseLanguagePage_SelectLanguage_SelectEnglish().text == "English":
            StartUp().ChooseLanguagePage_SelectLanguage_SelectEnglish().click()
            time.sleep(3)
        else:
            Tools().get_images()
            return ValueError
        expValue = "POPULAR"
        # 获取首页Popular文案(English_text=POPULAR)
        actValue = Home().HomePage_Popular_Text().text
        time.sleep(2)
        # 断言：校验首页Popular文案为英语
        self.assertEqual(expValue, actValue)






