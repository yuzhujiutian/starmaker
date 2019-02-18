# coding=utf-8
import time
import unittest
import warnings
from CommonView.StartUp import StartUp
from CommonView.LogIn import LogIn
from CommonView.Popup import Popup
from CommonView.Jalebee import Jalebee
from Utils.Tools import Tools
from Utils.Tools import Page_Element_Verification
from Utils.ReadXMLData import ReadXMLData
from Utils.GetAppiumDeriver import GetAppiumDeriver


# Jalebee
class JalebeeAutoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
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
        print("语言选择页显示正常")

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
        # 获取底部PostTab
        PostTab = Jalebee().Jalebee_MainTab_Post()
        time.sleep(2)
        # 断言
        self.assertTrue(actValue and PostTab)
        print("首页底部主Tab显示正常")

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
        print("首页内容Tab显示正常")

    # 首页——默认展示首页
    def test_Case004_HomePage_CheckDefaultPage(self):
        # 预期结果
        expValue = "true"
        # 获取首页Home-Tab按钮属性为选中状态
        actValue = Jalebee().JalebeeHomePage_MainTab_Home().get_attribute("selected")
        time.sleep(2)
        # 断言：默认展示首页
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("进入APP默认展示首页正常")

    # 首页——切换到Party页面
    def test_Case005_HomePage_SwitchPartyPage(self):
        # 点击Party按钮
        Jalebee().JalebeeHomePage_MainTab_Party().click()
        # 预期结果
        expValue = "true"
        # 获取Party-Tab按钮属性为选中状态
        actValue = Jalebee().JalebeeHomePage_MainTab_Party().get_attribute("selected")
        time.sleep(2)
        # 断言：成功切换至Party页
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("切换Party页面正常")

    # Party页面——Title显示正确
    def test_Case006_PartyPage_CheckTitle(self):
        # 预期结果
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PartyPage_Title")
        # 获取Party页Title
        actValue = Jalebee().JalebeePartyPage_Title_Text().text
        time.sleep(2)
        # 断言：默认展示首页
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("Party页面Title显示正常")

    # Party页面——MyRoom显示正确("मेरा रूम")
    def test_Case007_PartyPage_CheckMrRoom(self):
        # 预期结果
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PartyPage_MyRoom")
        # 获取Party页MyRoom
        actValue = Jalebee().JalebeePartyPage_MyRoom_Text().text
        time.sleep(2)
        # 断言：MyRoom显示正确
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("Party页面MyRoom显示正常")

    # Party页面——History显示正确("इतिहास")
    def test_Case008_PartyPage_CheckHistory(self):
        # 预期结果
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PartyPage_History")
        # 获取Party页History
        actValue = Jalebee().JalebeePartyPage_History_Text().text
        time.sleep(2)
        # 断言：History显示正确
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("Party页面History显示正常")

    # Party页面——房间显示正常
    def test_Case009_PartyPage_CheckKTVRoom(self):
        # 获取Party页前两个KTVRoom
        FirstRoom = Jalebee().JalebeePartyPage_KTVRoom_FirstRoom().text
        SecondRoom = Jalebee().JalebeePartyPage_KTVRoom_SecondRoom().text
        time.sleep(2)
        # 断言：KTV大厅有数据
        self.assertTrue(FirstRoom and SecondRoom)
        time.sleep(2)
        print("KTV大厅房间数据正常")

    # Party页面——搜索按钮显示正常
    def test_Case010_PartyPage_CheckSearchBtn(self):
        # 获取搜索按钮
        Search_Btn = Jalebee().Source_JalebeePartyPage_Search_Btn()
        time.sleep(2)
        # 断言：搜索按钮正常显示
        self.assertTrue(Search_Btn)
        time.sleep(2)
        print("KTV大厅搜索按钮正常")

    # 游客——点击Post_Tab显示登录窗口
    def test_Case011_Tourist_ClickPostTab_ShowLoginWindow(self):
        # 点击Post_Tab
        Jalebee().Jalebee_MainTab_Post().click()
        time.sleep(2)
        # 预期结果
        PostTab_Welcome = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PostTab_Welcome")
        # 获取登录窗口欢迎语
        LogInWindow_Welcome = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：成功弹出登录窗口
        self.assertEqual(PostTab_Welcome, LogInWindow_Welcome)
        time.sleep(2)
        print("游客点击Post成功弹出登录窗口，欢迎语显示正确")

    # 登录弹窗——登录方式显示正常
    def test_Case012_LogInWindow_CheckLogInMode(self):
        # 获取各个登录方式
        FacebookLogIn = LogIn().LogInPopup_SelectLoginMode_SelectFacebook()
        EmailLogIn = LogIn().LogInPopup_SelectLoginMode_SelectEmail()
        PhoneLogIn = LogIn().LogInPopup_SelectLoginMode_SelectPhone()
        GoogleLogIn = LogIn().LogInPopup_SelectLoginMode_SelectGoogle()
        time.sleep(2)
        # 断言：四种登录方式显示正常
        self.assertTrue(FacebookLogIn and EmailLogIn and PhoneLogIn and GoogleLogIn)
        time.sleep(2)
        print("四种登录方式入口显示正常")

    # 选择Email登录方式——Tips显示正常
    def test_Case013_LogInWindow_SelectEmailLogIn(self):
        # 点击Email LogIn按钮
        LogIn().LogInPopup_SelectLoginMode_SelectEmail().click()
        time.sleep(2)
        # 获取Email注册登录选择弹窗Title
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "EmailLoginMode_Title")
        actValue = LogIn().LogInPopup_EmailLoginMode_Title().text
        time.sleep(2)
        # 断言：成功弹出Email注册登录选择弹窗
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("Email登录注册选择弹窗 Tips显示正常")

    # Email登录注册选择页——登录入口显示正常
    def test_Case014_EmailLogInSignUpSelectionPage_CheckLogInEntry(self):
        # 获取Email注册登录选择弹窗登录入口文案
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "LogInEntry")
        actValue = LogIn().LogInPopup_EmailLoginMode_SelectLogIn().text
        time.sleep(2)
        # 断言：登录入口显示正常
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("Email登录注册选择弹窗 登录入口显示正常")

    # Email登录注册选择页——注册入口显示正常
    def test_Case015_EmailLogInSignUpSelectionPage_CheckSignUpEntry(self):
        # 获取Email注册登录选择弹窗注册入口文案
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "SignUpEntry")
        actValue = LogIn().LogInPopup_EmailLoginMode_SelectSignUp().text
        time.sleep(2)
        # 断言：注册入口显示正常
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("Email登录注册选择弹窗 注册入口显示正常")

    # Email登录注册选择页——其他元素显示正常
    def test_Case016_EmailLogInSignUpSelectionPage_CheckOther(self):
        # 获取Email注册登录选择弹窗其他元素
        Close_Btn = LogIn().LogInPopup_EmailLoginMode_SelectClose()
        Cancel_Btn = LogIn().LogInPopup_EmailLoginMode_SelectCancel()
        time.sleep(2)
        # 断言：关闭和取消按钮显示正常
        self.assertTrue(Close_Btn and Cancel_Btn)
        time.sleep(2)
        print("Email登录注册选择弹窗 关闭和取消按钮显示正常")

    # Email登录注册选择页——邮箱登录
    def test_Case017_EmailLogInPage_InputBox_EmailInput(self):
        # 点击登录按钮
        LogIn().LogInPopup_EmailLoginMode_SelectLogIn().click()
        time.sleep(2)
        # 获取测试账号邮箱
        Email = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Email")
        # 输入账号
        LogIn().EmailLogInPage_InputBox_EmailInput().send_keys(Email)
        time.sleep(2)
        # 获取Email输入框text
        expValue = Email
        actValue = LogIn().EmailLogInPage_InputBox_EmailInput().text
        time.sleep(2)
        # 断言：输入邮箱正确
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("输入登录邮箱正常")

    # 邮箱登录页-输入框-明文密码
    def test_Case18_EmailLogInPage_InputBox_InputVisibility(self):
        # 点击明文密码按钮
        LogIn().EmailLogInPage_InputBox_InputVisibility().click()
        time.sleep(2)
        # 获取Password输入框password属性
        expValue = "false"
        actValue = LogIn().EmailLogInPage_InputBox_PasswordInput().get_attribute("password")
        time.sleep(2)
        # 断言：密码以明文展示
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("明文密码功能正常")

    # 邮箱登录页-输入框-输入密码
    def test_Case19_EmailLogInPage_InputBox_PasswordInput(self):
        # 获取测试账号密码
        Password = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Password")
        # 输入密码
        LogIn().EmailLogInPage_InputBox_PasswordInput().send_keys(Password)
        time.sleep(2)
        # 获取密码
        if LogIn().EmailLogInPage_InputBox_PasswordInput().get_attribute("password") == "true":
            # 点击明文密码
            LogIn().EmailLogInPage_InputBox_InputVisibility().click()
            time.sleep(2)
        # 获取Password输入框text
        expValue = Password
        actValue = LogIn().EmailLogInPage_InputBox_PasswordInput().text
        time.sleep(2)
        # 断言：输入密码正确
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("输入登录密码正常")

    # 邮箱登录页-登录-确认登录
    def test_Case20_EmailLogInPage_LogIn_Confirm(self):
        # 点击确认登录按钮
        LogIn().EmailLogInPage_LogIn_Confirm().click()
        time.sleep(5)
        # 尝试查找邮箱登录页顶部Title
        actValue = LogIn().EmailLogInPage_Title_Text()
        time.sleep(2)
        # 断言：登录成功
        self.assertFalse(actValue)
        time.sleep(2)
        print("登录成功")

    # 处理权限弹窗-进入拍摄页面
    def test_Case21_Jurisdiction_LiveClick(self):
        # 获取权限申请文案
        Hindi_Recording_Jurisdiction = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "Hindi_Recording_Jurisdiction")
        # 处理权限申请弹窗
        Popup().SingPopup_Jurisdiction_LiveClick(text=Hindi_Recording_Jurisdiction)
        time.sleep(10)
        # 获取添加音乐引导文案
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "Guide_AddMusic")
        actValue = Jalebee().JalebeeShotPage_Guide_AddMusic().text
        # 断言：成功进入拍摄页
        self.assertEqual(expValue, actValue)
        time.sleep(2)
        print("登录成功后直接进入拍摄页面")

