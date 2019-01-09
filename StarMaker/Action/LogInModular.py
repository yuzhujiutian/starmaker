# coding=utf-8
import time
import unittest
from CommonView.LogIn import LogIn
from CommonView.Home import Home
from CommonView.Parties import Parties
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.ReadXMLData import ReadXMLData


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
    # 调起登录弹窗
    # ----------
    # 首页-游客点击Sing-调起登录弹窗
    def test_Case2101_HomePage_Tourist_PostTabInlet(self):
        Home().HomePage_MainTab_SingTab().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in to make a post."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # 首页-游客点击Message-调起登录弹窗
    def test_Case2102_HomePage_Tourist_NotificationTabInlet(self):
        Home().HomePage_MainTab_MessageTab().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in before checking the latest news."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # 首页-游客点击Me-调起登录弹窗
    def test_Case2103_HomePage_Tourist_ProfileTabInlet(self):
        Home().HomePage_MainTab_MeTab().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in before checking your profile."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # 首页-游客点击feed卡片Share-调起登录弹窗
    def test_Case2104_HomePage_Tourist_FeedCardShareInlet(self):
        Home().HomePage_FeedCard_Share().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in to repost it."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # 首页-游客点击feed卡片Like-调起登录弹窗
    def test_Case2105_HomePage_Tourist_FeedCardLikeInlet(self):
        Home().HomePage_FeedCard_Like().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Please log in to like it."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # KTV大厅-点击任意房间-调起登录弹窗
    def test_Case2106_KTVHall_Tourist_PartiesRoomInlet(self):
        Parties().KtvPage_RoomCard_Cover().click()
        time.sleep(2)
        # 获取登录弹窗的Tips文案
        expValue = "Enjoy all features after log in."
        actValue = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：调起登录弹窗
        self.assertEqual(expValue, actValue)

    # ----------
    # 登录弹窗
    # ----------
    # 登录弹窗-选择登录方式-选择FB方式(已安装FB客户端)
    def test_Case2107_LogInPopup_SelectLoginMode_SelectFacebook(self):
        LogIn().LogInPopup_SelectLoginMode_SelectFacebook().click()
        time.sleep(2)
        # 校验FB登录页登陆点击按钮是否存在
        actValue = LogIn().LogInPopup_FBLoginMode_LogInClickBtn()
        time.sleep(2)
        # 断言：成功跳转至FB登录页
        self.assertTrue(actValue)

    # 登录弹窗-选择登录方式-选择Email方式
    def test_Case2108_LogInPopup_SelectLoginMode_SelectEmail(self):
        LogIn().LogInPopup_SelectLoginMode_SelectEmail().click()
        time.sleep(2)
        # 获取Email注册登录选择弹窗Title
        expValue = "Use Email Address"
        actValue = LogIn().LogInPopup_EmailLoginMode_Title().text
        time.sleep(2)
        # 断言：成功弹出Email注册登录选择弹窗
        self.assertEqual(expValue, actValue)

    # 登录弹窗-选择登录方式-选择Phone方式
    def test_Case2109_LogInPopup_SelectLoginMode_SelectPhone(self):
        LogIn().LogInPopup_SelectLoginMode_SelectPhone().click()
        time.sleep(2)
        # 获取Phone登录页顶部Title
        expValue = "Enter your mobile number"
        actValue = LogIn().PhoneHome_Tips().text
        time.sleep(2)
        # 断言：成功跳转至Phone登录页
        self.assertEqual(expValue, actValue)

    # 登录弹窗-选择登录方式-选择G+方式
    def test_Case2110_LogInPopup_SelectLoginMode_SelectGoogle(self):
        LogIn().LogInPopup_SelectLoginMode_SelectGoogle().click()
        time.sleep(2)
        # 处理预选帐号弹窗
        if LogIn().FindGoogle_PreselectionPopup():
            actValue = True
        else:
            actValue = LogIn().Google_AddLogInPage_Title()
        time.sleep(2)
        # 断言：成功跳转至google登录页
        self.assertTrue(actValue)

    # ----------
    # 登录弹窗-Email登录方式
    # ----------
    # 登录弹窗-Email登录方式-选择登录
    def test_Case2111_LogInPopup_EmailLoginMode_SelectLogIn(self):
        LogIn().LogInPopup_EmailLoginMode_SelectLogIn().click()
        time.sleep(2)
        # 获取Email输入框text
        expValue = "Email"
        actValue = LogIn().EmailLogInPage_InputBox_EmailInput().text
        time.sleep(2)
        # 断言：跳转Email登录页成功
        self.assertEqual(expValue, actValue)

    # 登录弹窗-Email登录方式-选择注册
    def test_Case2112_LogInPopup_EmailLoginMode_SelectSignUp(self):
        LogIn().LogInPopup_EmailLoginMode_SelectSignUp().click()
        # 断言待补充

    # 登录弹窗-Email登录方式-选择取消
    def test_Case2113_LogInPopup_EmailLoginMode_SelectCancel(self):
        LogIn().LogInPopup_EmailLoginMode_SelectCancel().click()
        # 断言待补充

    # ----------
    # 邮箱登录页
    # ----------
    # 邮箱登录页-输入框-输入邮箱
    def test_Case2201_EmailLogInPage_InputBox_EmailInput(self):
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
    def test_Case2202_EmailLogInPage_InputBox_InputVisibility(self):
        LogIn().EmailLogInPage_InputBox_InputVisibility().click()
        time.sleep(2)
        # 获取Password输入框password属性
        expValue = "false"
        actValue = LogIn().EmailLogInPage_InputBox_PasswordInput().get_attribute("password")
        time.sleep(2)
        # 断言：密码以明文展示
        self.assertEqual(expValue, actValue)

    # 邮箱登录页-输入框-输入密码
    def test_Case2203_EmailLogInPage_InputBox_PasswordInput(self):
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
    def test_Case2204_EmailLogInPage_LogIn_Confirm(self):
        LogIn().EmailLogInPage_LogIn_Confirm().click()
        time.sleep(5)
        # 尝试查找邮箱登录页顶部Title
        actValue = LogIn().EmailLogInPage_Title_Text()
        time.sleep(2)
        # 断言：登录成功
        self.assertFalse(actValue)









