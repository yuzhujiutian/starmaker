# coding=utf-8
import time
import unittest
from StarMaker.CommonView.StartUp import StartUp
from StarMaker.CommonView.LogIn import LogIn
from StarMaker.CommonView.Home import Home
from StarMaker.Utils.Tools import Tools
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver
from StarMaker.Utils.ReadXMLData import ReadXMLData


# Facebook登录
class FacebookLogInCase(unittest.TestCase):
    # 存放Skip_Case
    Skips = []

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

    # 判断当前手机打开Facebook登录方式（PS：判断本机是否安装fb）
    def test_Case001_WayJudgmentCase(self):
        # 点击fb登录按钮
        StartUp().FB_LogIn_Btn().click()
        time.sleep(10)
        # 查找H5弹窗是否存在
        if LogIn().FBPopup_TitleFind():
            time.sleep(2)
            Way = "Popup"
        # 查找第三方页面是否存在
        elif LogIn().FBPage_Preselection_TitleFind():
            time.sleep(2)
            Way = "Page"
        else:
            Way = None
        # 断言：Way不为空
        self.assertIsNotNone(Way)

    # 手机未安装APP时，Facebook弹窗登录成功
    def test_Case002_FBPopup_LogInCase(self):
        # 如果Facebook弹窗能找到
        if LogIn().FBPopup_TitleFind():
            time.sleep(2)
            # 输入Facebook帐号
            LogIn().FBPopup_Email().send_keys(
                ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "FBEmail"))
            time.sleep(2)
            # 输入Facebook密码
            LogIn().FBPopup_Password().send_keys(
                ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "FBPasswprd"))
            time.sleep(2)
            # 点击登录按钮
            LogIn().FBPopup_LogIn().click()
            time.sleep(5)
            # 点击继续按钮
            LogIn().FBPopup_Continue_R()
            time.sleep(5)
            expValue = "Share your pictures and view what's shared by others."
            # 记录首页New Feature引导文案
            actValue = Home().HomePage_NewFeature_Tips().text
            # 判断是否新装包首次登录成功——展示New Feature引导
            time.sleep(2)
            self.assertEqual(expValue, actValue)
        # 否则Home().HomePage_MainTabName_Sing().text该Case
        else:
            self.Skips.append("Skip_test_Case002")
            self.skipTest("该设备已安装Facebook客户端，跳过test_Case002")

    # 手机已安装APP是，Facebook第三方登录页面登录成功
    def test_Case003_FBPage_LogInCase(self):
        # 如果Facebook页面能找到
        if LogIn().FBPage_Preselection_TitleFind():
            time.sleep(2)
            # 如果有Facebook预选帐号弹窗（客户端曾今登录）
            if LogIn().FBPage_Pre_FindLoginAnotherAccount():
                # 点击选择其他帐号登录
                LogIn().FBPage_Pre_LoginAnotherAccount().click()
                time.sleep(2)
            # 输入Facebook帐号
            LogIn().FBPage_inputAN().send_keys(
                ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "FBEmail"))
            time.sleep(2)
            # 点击登录
            LogIn().FBPage_LogIn().click()
            time.sleep(2)
            # 输入Facebook密码
            LogIn().FBPage_inputPWD().send_keys(
                ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "FBPasswprd"))
            time.sleep(2)
            # 再次点击登录
            LogIn().FBPage_LogIn().click()
            time.sleep(5)
            expValue = "Share your pictures and view what's shared by others."
            # 记录首页New Feature引导文案
            actValue = Home().HomePage_NewFeature_Tips().text
            # 判断是否新装包首次登录成功——展示New Feature引导
            time.sleep(2)
            self.assertEqual(expValue, actValue)
        # 否则跳过该Case
        else:
            self.Skips.append("Skip_test_Case003")
            self.skipTest("该设备未安装Facebook客户端，跳过test_Case003")

    # 点击FB登录按钮直接登录成功
    def test_Case004_FBLogInBtn_LogInCase(self):
        if len(self.Skips) == 2:
            time.sleep(5)
            expValue = "Share your pictures and view what's shared by others."
            # 记录首页New Feature引导文案
            actValue = Home().HomePage_NewFeature_Tips().text
            # 判断是否新装包首次登录成功——展示New Feature引导
            time.sleep(2)
            self.assertEqual(expValue, actValue)
        else:
            self.skipTest("已登录")


if __name__ == '__main__':
    unittest.main()
