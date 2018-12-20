# coding=utf-8
import time
import unittest
from CommonView.StartUp import StartUp
from CommonView.LogIn import LogIn
from CommonView.Home import Home
from CommonView.Profile import Profile
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.ReadXMLData import ReadXMLData
from Utils.Tools import Screen


# 邮箱登录
class EmailLogInCase(unittest.TestCase):
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

    # Email登录输入框功能验证——清空Email
    def test_Case001_InputFunction_ClearingEmailCase(self):
        # 内容语言选择页面点击English
        StartUp().ChooseContentLan_En().click()
        time.sleep(5)
        # 点击APP底部的me页面入口唤起【登录注册】弹窗
        Home().HomeTab_Profile().click()
        # 在【登录注册】弹窗上点击邮箱方式
        LogIn().LogInWindow_Email_Btn().click()
        # 邮箱登录弹窗上点击login按钮
        LogIn().EmailWindow_LogIn_Btn().click()
        time.sleep(2)
        # 输入邮箱
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Email"))
        time.sleep(2)
        # 点击清空Email
        LogIn().Email_Clear_EmailBox_Btn().click()
        time.sleep(2)
        expValue = "Email"
        # 获取账号输入框内容
        actValue = LogIn().Email_Username_Box().text
        # 判断账号输入框为空
        time.sleep(2)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Username_Box().clear()
        LogIn().Email_Password_Box().clear()

    # Email登录输入框功能验证——清空Pwd
    def test_Case002_InputFunction_ClearingPasswordCase(self):
        # 输入密码
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        time.sleep(2)
        # 点击清空Pwd
        LogIn().Email_Clear_PWDBox_Btn().click()
        time.sleep(2)
        expValue = "Password"
        # 获取密码输入框内容
        actValue = LogIn().Email_Password_Box().text
        # 判断密码输入框为空
        time.sleep(2)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Username_Box().clear()
        LogIn().Email_Password_Box().clear()

    # Email登录输入框功能验证——展示明文密码
    def test_Case003_InputFunction_ShowPasswordCase(self):
        # 输入密码
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        time.sleep(2)
        # 点击展示明文密码
        LogIn().Email_ShowPassword_Btn().click()
        time.sleep(2)
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password")
        # 获取密码输入框内容（非明文text：••••••/明文text：000000）
        actValue = LogIn().Email_Password_Box().text
        # 判断是否成功展示明文密码
        time.sleep(2)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Username_Box().clear()
        LogIn().Email_Password_Box().clear()

    # Email登录——未输入账号时忘记密码光标焦到账户输入框
    def test_Case004_ForgotPassword_FocusedCase(self):
        # 点击忘记密码
        LogIn().Email_ForgotPassword_Link().click()
        time.sleep(2)
        expValue = "true"
        # 因未输入密码，光标聚焦到账号输入框
        actValue = LogIn().Email_Username_Box().get_attribute("focused")
        # 判断光标是否成功聚焦
        time.sleep(2)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Username_Box().clear()
        LogIn().Email_Password_Box().clear()

    # Email登录——未输入账号时忘记密码输入框下方提示不能为空：Your email cannot be empty.
    def test_Case005_ForgotPassword_EmailError_EmptyCase(self):
        expValue = "Your email cannot be empty."
        # 获取账号输入框下方Error提示
        actValue = LogIn().Email_Username_Error().text
        time.sleep(2)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Username_Box().clear()
        LogIn().Email_Password_Box().clear()

    # Email登录——账号错误提示：未注册
    def test_Case006_EmailError_NotRegisteredCase(self):
        # 输入未注册账号/密码
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "NotRegisteredEmail"))
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        time.sleep(2)
        # 点击登录按钮
        LogIn().LogIn_Confirm_Btn().click()
        time.sleep(2)
        expValue = "This Email is not registered yet, please Sign Up now."
        # 获取账号输入框下方Error提示
        actValue = LogIn().Email_Username_Error().text
        time.sleep(2)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Username_Box().clear()
        LogIn().Email_Password_Box().clear()

    # # Email登录——Sign Up跳转注册页
    # def test_Case007_EmailError_SignUp_linkCase(self):
    #     # 输入未注册账号/密码
    #     LogIn().Email_Username_Box().send_keys(
    #         ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "NotRegisteredEmail"))
    #     LogIn().Email_Password_Box().send_keys(
    #         ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
    #     time.sleep(2)
    #     # 点击登录按钮
    #     LogIn().LogIn_Confirm_Btn().click()
    #     time.sleep(5)
    #     # 点击SignUp
    #     LogIn().Email_Username_SignUpNow_ACP()
    #     # self.driver.tap([(1030, 650)], 500)
    #     time.sleep(2)
    #     expValue = "输入邮箱"
    #     # 获取注册页Tips值
    #     actValue = SignUp().SignUp_Tips().text
    #     # 验证是否跳转成功
    #     time.sleep(2)
    #     self.assertEqual(expValue, actValue)
    #     # 为Email登录Case 执行tearDown:
    #     # 1.返回
    #     self.driver.back()
    #     time.sleep(10)
    #     # 2.点击邮箱登录按钮
    #     StartUp().Email_LogIn_Btn_R()
    #     time.sleep(2)
    #     # 3.点击登录弹窗中LogIn按钮
    #     LogIn().EmailWindow_LogIn_Btn().click()
    #     time.sleep(2)

    # Email登录——密码错误提示
    def test_Case008_EmailError_PwdIncorrect(self):
        # 输入邮箱
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Email"))
        # 输入错误密码
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "IncorrectPassword"))
        # 点击LogIn
        LogIn().LogIn_Confirm_Btn().click()
        time.sleep(5)
        expValue = "Username or password is incorrect"
        # 获取密码输入框下方Error提示
        actValue = LogIn().Email_Password_Error().text
        # 判断是否提示密码输入错误
        time.sleep(2)
        self.assertEqual(expValue, actValue)
        LogIn().Email_Username_Box().clear()
        LogIn().Email_Password_Box().clear()

    # Email登录——新装包首次登录成功
    def test_Case009_EmailLogIn(self):
        # 输入邮箱
        LogIn().Email_Username_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Email"))
        # 输入密码
        LogIn().Email_Password_Box().send_keys(
            ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password"))
        # 设置预期值为登录成功后me页面的一个元素
        expValue = "Followers"
        # 点击LogIn
        LogIn().LogIn_Confirm_Btn().click()
        time.sleep(5)
        actValue = Profile().Profile_FollowersEnter().text
        time.sleep(2)
        # 判断是否新装包登录成功——比对me页面的followers入口文案
        self.assertEqual(expValue, actValue)

        # self.assertTrue(actValue)
        # time.sleep(2)
        # Popup().HomePopup_NewFeature_NEXT_LiveClick()
        # time.sleep(2)
        # Popup().HomePopup_NewFeatureAdded_NEXT_LiveClick()
        # time.sleep(2)
        # Popup().HomePopup_NewFeatureSing_NEXT_LiveClick()
        # time.sleep(2)
        # Popup().HomePopup_NewFeaturePostOther_DONE_LiveClick()
        # time.sleep(2)
        # Popup().HomePopup_PermissionMessage_Allow_LiveClick()
        # time.sleep(2)


# if __name__ == "__main__":
#     pass
