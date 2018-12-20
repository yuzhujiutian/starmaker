# coding=utf-8
import time
import unittest
from CommonView.StartUp import StartUp
from CommonView.LogIn import LogIn
from CommonView.Home import Home
from Utils.Tools import Tools, Screen
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.ReadXMLData import ReadXMLData
from CommonView.Profile import Profile


# Google登录
class GoogleLogInCase(unittest.TestCase):
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

    # Google第三方登陆
    def test_Case001_GoogleLogIn(self):
        # 滑动Choose Language页面到底部
        Screen().DIYSwipe_Percentage(0.5, 0.7, 0.5, 0.4, 500)
        time.sleep(2)
        # 内容语言选择页面点击English
        StartUp().ChooseContentLan_En().click()
        time.sleep(8)
        # 点击APP底部的me页面入口唤起【登录注册】弹窗
        Home().HomeTab_Profile().click()
        # 判断【登录注册】弹窗上是否有G+登录方式的按钮
        if LogIn().LogInModeCase_Google():
            # 点击G+登陆按钮
            LogIn().LogInWindow_Google_Btn().click()
            time.sleep(10)
            # 查找预选帐号弹窗是否存在
            if LogIn().FindGoogle_PreselectionPopup():
                time.sleep(2)
                # 点击添加帐号（需提前关闭手机密码解锁）
                LogIn().Google_AddAccountNumber().click()
                time.sleep(5)
            else:
                pass
            # 输入电子邮箱地址或电话号码
            LogIn().Google_AddLogInPage_InputAN().send_keys(
                ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "GoogleEmail"))
            time.sleep(5)
            # 点击下一步
            LogIn().Google_ANNext().click()
            time.sleep(5)
            # 判定该帐号是否已添加
            if LogIn().Google_AddAN_ErrorText():
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
                    ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "GooglePassword"))
                time.sleep(2)
                # 点击下一步
                LogIn().Google_PWDNext().click()
                time.sleep(2)
                # 点击我同意
                LogIn().Google_ConsentNext().click()
                time.sleep(2)
                # google服务页点击“下箭头”
                LogIn().Google_ServiceDownArrow().click()
                time.sleep(2)
                # google服务页点击“接受”
                LogIn().Google_ServiceAccept().click()
            time.sleep(5)
            # 使用me页面的followers入口的文案作为校验值
            expValue = "Followers"
            # 记录me页面followers入口的文案
            actValue = Profile().Profile_FollowersEnter().text
            # 判断是否新装包G+登录成功——比对me页面的followers入口
            time.sleep(2)
            self.assertEqual(expValue, actValue)
        else:
            self.skipTest("该设备不支持Google登陆方式")


if __name__ == '__main__':
    unittest.main()
