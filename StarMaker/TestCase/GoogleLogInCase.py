# coding=utf-8
import time
import unittest
from CommonView.StartUp import StartUp
from CommonView.LogIn import LogIn
from CommonView.Home import Home
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.ReadXMLData import ReadXMLData


# Google登录
class GoogleLogInCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # Google第三方登陆
    def test_Case001_GoogleLogIn(self):
        if StartUp().LogInModeCase_Google():
            # 点击G+登陆按钮
            StartUp().Google_LogIn_Btn().click()
            time.sleep(10)
            # 查找预选帐号弹窗是否存在
            if LogIn().FindGoogle_PreselectionPopup():
                time.sleep(1)
                # 点击添加帐号（需提前关闭手机密码解锁）
                LogIn().Google_AddAccountNumber().click()
                time.sleep(5)
            else:
                pass
            # 输入电子邮箱地址或电话号码
            LogIn().Google_AddLogInPage_InputAN().send_keys(
                ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "GoogleEmail"))
            time.sleep(1)
            # 点击下一步
            LogIn().Google_ANNext().click()
            time.sleep(1)
            # 判定该帐号是否已添加
            if LogIn().Google_AddAN_ErrorText().text == "此帐号已在您的设备上":
                # 返回至预选弹窗
                self.driver.back()
                time.sleep(5)
                # 查找该帐号在预选弹窗中位置，并点击
                LogIn().Google_GivenAN().click()
            # 如果可以添加
            else:
                # 输入密码
                LogIn().Google_AddLogInPage_InputPWD().send_keys(
                    ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "GooglePasswprd"))
                time.sleep(1)
                # 点击下一步
                LogIn().Google_PWDNext().click()
                time.sleep(3)
                # 点击我同意
                LogIn().Google_ConsentNext().click()
            time.sleep(5)
            expValue = "Share your pictures and view what's shared by others."
            # 记录首页New Feature引导文案
            actValue = Home().HomePage_NewFeature_Tips().text
            # 判断是否新装包首次登录成功——展示New Feature引导
            time.sleep(1)
            self.assertEqual(expValue, actValue)
        else:
            self.skipTest("该设备不支持Google登陆方式")


if __name__ == '__main__':
    unittest.main()
