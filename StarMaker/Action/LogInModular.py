# coding=utf-8
import time
import unittest
from CommonView.LogIn import LogIn
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.ReadXMLData import ReadXMLData
from Utils.Tools import Screen


# 邮箱登录
class LogInModular(unittest.TestCase):
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

    # ----------
    # 登录弹窗
    # ----------
    # 登录弹窗-选择登录方式-选择FB方式
    def test_Case001_LogInPopup_SelectLoginMode_SelectFacebook(self):
        LogIn().LogInPopup_SelectLoginMode_SelectFacebook().click()
        # 断言待补充

    # 登录弹窗-选择登录方式-选择Email方式
    def test_Case002_LogInPopup_SelectLoginMode_SelectEmail(self):
        LogIn().LogInPopup_SelectLoginMode_SelectEmail().click()
        time.sleep(2)
        # 获取Email注册登录选择弹窗Title
        expValue = "Use Email Address"
        actValue = LogIn().LogInPopup_EmailLoginMode_Title().text
        time.sleep(2)
        # 断言：成功弹出Email注册登录选择弹窗
        self.assertEqual(expValue, actValue)

    # 登录弹窗-选择登录方式-选择Phone方式
    def test_Case003_LogInPopup_SelectLoginMode_SelectPhone(self):
        LogIn().LogInPopup_SelectLoginMode_SelectPhone().click()
        # 断言待补充

    # 登录弹窗-选择登录方式-选择G+方式
    def test_Case004_LogInPopup_SelectLoginMode_SelectGoogle(self):
        LogIn().LogInPopup_SelectLoginMode_SelectGoogle().click()
        # 断言待补充

    # ----------
    # 登录弹窗-Email登录方式
    # ----------
    # 登录弹窗-Email登录方式-选择登录
    def test_Case005_LogInPopup_EmailLoginMode_SelectLogIn(self):
        LogIn().LogInPopup_EmailLoginMode_SelectLogIn().click()
        time.sleep(2)
        # 获取Email输入框text
        expValue = "Email"
        actValue = LogIn().EmailLogInPage_InputBox_EmailInput().text
        time.sleep(2)
        # 断言：跳转Email登录页成功
        self.assertEqual(expValue, actValue)

    # 登录弹窗-Email登录方式-选择注册
    def test_Case006_LogInPopup_EmailLoginMode_SelectSignUp(self):
        LogIn().LogInPopup_EmailLoginMode_SelectSignUp().click()
        # 断言待补充

    # 登录弹窗-Email登录方式-选择取消
    def test_Case007_LogInPopup_EmailLoginMode_SelectCancel(self):
        LogIn().LogInPopup_EmailLoginMode_SelectCancel().click()
        # 断言待补充

    # 邮箱登录页-输入框-输入邮箱
    def test_Case008_EmailLogInPage_InputBox_EmailInput(self):
        Email = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Email")
        LogIn().EmailLogInPage_InputBox_EmailInput().send_keys(Email)
        time.sleep(2)
        # 获取Email输入框text
        expValue = Email
        actValue = LogIn().EmailLogInPage_InputBox_EmailInput().text
        time.sleep(2)
        # 断言：输入邮箱正确
        self.assertEqual(expValue, actValue)

    # 邮箱登录页-输入框-明文密码
    def test_Case009_EmailLogInPage_InputBox_InputVisibility(self):
        LogIn().EmailLogInPage_InputBox_InputVisibility().click()
        time.sleep(2)
        # 获取Password输入框password属性
        expValue = "false"
        actValue = LogIn().EmailLogInPage_InputBox_PasswordInput().get_attribute("password")
        time.sleep(2)
        # 断言：密码以明文展示
        self.assertEqual(expValue, actValue)

    # 邮箱登录页-输入框-输入密码
    def test_Case010_EmailLogInPage_InputBox_PasswordInput(self):
        Password = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password")
        LogIn().EmailLogInPage_InputBox_PasswordInput().send_keys(Password)
        time.sleep(2)
        # 获取密码
        if LogIn().EmailLogInPage_InputBox_PasswordInput().get_attribute("password") == "true":
            # 点击明文密码
            LogIn().EmailLogInPage_InputBox_InputVisibility().click()
            time.sleep(2)
        # 获取Email输入框text
        expValue = Password
        actValue = LogIn().EmailLogInPage_InputBox_PasswordInput().text
        time.sleep(2)
        # 断言：输入密码正确
        self.assertEqual(expValue, actValue)

    # 邮箱登录页-登录-确认登录
    def test_Case011_EmailLogInPage_LogIn_Confirm(self):
        LogIn().EmailLogInPage_LogIn_Confirm().click()
        time.sleep(5)
        # 尝试查找邮箱登录页顶部Title
        actValue = LogIn().EmailLogInPage_Title_Text()
        time.sleep(2)
        # 断言：登录成功
        self.assertFalse(actValue)









