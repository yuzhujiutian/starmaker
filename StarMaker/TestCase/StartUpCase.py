# coding=utf-8
import time
import unittest
from CommonView.StartUp import StartUp
from Utils.Tools import Tools
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

    # 启动成功——介绍验证
    def test_Case001_TipsCase(self):
        expValue = '"sing with 50,000,000+ music lovers"'
        # 获取启动首页Tips文案
        actValue = StartUp().StartUpHome_Tips().text
        time.sleep(2)
        self.assertEqual(expValue, actValue)

    # 启动成功——解释说明验证
    def test_Case002_ExplainCase(self):
        expValue = "You agree to our Terms of Service & Privacy Policy"
        # 获取启动首页解释说明文案
        actValue = StartUp().StartUpHome_Explain().text
        time.sleep(2)
        self.assertEqual(expValue, actValue)

    # 登录方式验证——Email 登录
    def test_Case003_LogInMode_EmailCase(self):
        expValue = True
        # 查找Email登录按钮，如果存在则返回True
        actValue = StartUp().LogInModeCase_Email()
        time.sleep(2)
        self.assertEqual(expValue, actValue)

    # 登录方式验证——Phone 登录
    def test_Case004_LogInMode_PhoneCase(self):
        expValue = True
        # 查找Phone登录按钮，如果存在则返回True
        actValue = StartUp().LogInModeCase_Phone()
        time.sleep(2)
        self.assertEqual(expValue, actValue)

    # 登录方式验证——Google 登录
    def test_Case005_LogInMode_GoogleCase(self):
        expValue = True
        # 查找Google登录按钮，如果存在则返回True
        actValue = StartUp().LogInModeCase_Google()
        time.sleep(2)
        self.assertEqual(expValue, actValue)

    # 登录方式验证——Facebook 登录
    def test_Case006_LogInMode_FacebookCase(self):
        expValue = True
        # 查找Email登录按钮，如果存在则返回True
        actValue = StartUp().LogInModeCase_Facebook()
        time.sleep(2)
        self.assertEqual(expValue, actValue)
