# coding=utf-8
import re
import time
import unittest
import warnings
from CommonView.StartUp import StartUp
from CommonView.LogIn import LogIn
from CommonView.Popup import Popup
from CommonView.Profile import Profile
from CommonView.Jalebee import Jalebee
from Utils.Tools import Tools
from Utils.Tools import Screen
from Utils.Tools import TestData_Processing
from Utils.Tools import AssertReportManage
from Utils.Tools import Internationalization
from Utils.Tools import Page_Element_Verification
from Utils.ReadXMLData import ReadXMLData
from Utils.GetAppiumDeriver import GetAppiumDeriver
P = AssertReportManage().Pass
E = AssertReportManage().Error


# Jalebee
class JalebeeAutoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = GetAppiumDeriver().driver
        # 处理上次运行留下的测试数据
        TestData_Processing().TestPicture_Processing()
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
        # 断言：
        msg = "语言选择页 语言选项"
        self.assertTrue(actValue, E(msg))
        print(P(msg))

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
        # 断言：
        msg = "首页底部主Tab"
        self.assertTrue(actValue and PostTab, E(msg))
        print(P(msg))

    # 首页——校验内容Tab
    def test_Case003_HomePage_CheckFeedTab(self):
        # 预期结果
        TextList = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "HomePageFeedTab")
        time.sleep(2)
        # 获取该首页顶部所有内容Tab名
        actValue = Page_Element_Verification().PEV_ClaS(Jalebee().JalebeeHomePage_FeedTab_Check(), TextList)
        time.sleep(2)
        # 断言：
        msg = "首页内容Tab"
        self.assertTrue(actValue, E(msg))
        print(P(msg))

    # 首页——默认展示首页
    def test_Case004_HomePage_CheckDefaultPage(self):
        # 预期结果
        expValue = "true"
        # 获取首页Home-Tab按钮属性为选中状态
        actValue = Jalebee().JalebeeHomePage_MainTab_Home().get_attribute("selected")
        time.sleep(2)
        # 断言：
        msg = "进入APP默认展示首页"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 首页——切换到Party页面
    def test_Case005_HomePage_SwitchPartyPage(self):
        # 点击Party按钮
        Jalebee().JalebeeHomePage_MainTab_Party().click()
        # 预期结果
        expValue = "true"
        # 获取Party-Tab按钮属性为选中状态
        actValue = Jalebee().JalebeeHomePage_MainTab_Party().get_attribute("selected")
        time.sleep(2)
        # 断言：
        msg = "点击Party按钮切换Party页面"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # Party页面——Title显示正确
    def test_Case006_PartyPage_CheckTitle(self):
        # 预期结果
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PartyPage_Title")
        # 获取Party页Title
        actValue = Jalebee().JalebeePartyPage_Title_Text().text
        time.sleep(2)
        # 断言：
        msg = "Party页面Title"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # Party页面——MyRoom显示正确(MrRoom="मेरा रूम"/History="इतिहास")
    def test_Case007_PartyPage_CheckMrRoom_CheckHistory(self):
        # 预期结果
        MrRoom_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PartyPage_MyRoom")
        History_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PartyPage_History")
        # 获取Party页MyRoom
        MrRoom_actValue = Jalebee().JalebeePartyPage_MyRoom_Text().text
        time.sleep(2)
        # 获取Party页History
        History_actValue = Jalebee().JalebeePartyPage_History_Text().text
        time.sleep(2)
        # 断言：
        msg1 = "Party页面MyRoom显示"
        msg2 = "Party页面History显示"
        self.assertEqual(MrRoom_expValue, MrRoom_actValue, E(msg1))
        print(P(msg1))
        self.assertEqual(History_expValue, History_actValue, E(msg2))
        print(P(msg2))

    # Party页面——房间显示正常
    def test_Case008_PartyPage_CheckKTVRoom(self):
        # 获取Party页前两个KTVRoom
        FirstRoom = Jalebee().JalebeePartyPage_KTVRoom_FirstRoom().text
        SecondRoom = Jalebee().JalebeePartyPage_KTVRoom_SecondRoom().text
        time.sleep(2)
        # 断言：
        msg = "KTV大厅房间数据"
        self.assertTrue(FirstRoom and SecondRoom, E(msg))
        print(P(msg))

    # Party页面——搜索按钮显示正常
    def test_Case009_PartyPage_CheckSearchBtn(self):
        # 获取搜索按钮
        Search_Btn = Jalebee().JalebeePartyPage_Search_Btn()
        time.sleep(2)
        # 断言：
        msg = "KTV大厅搜索按钮"
        self.assertTrue(Search_Btn, E(msg))
        print(P(msg))

    # 游客——点击Post_Tab显示登录窗口
    def test_Case010_Tourist_ClickPostTab_ShowLoginWindow(self):
        # 点击Post_Tab
        Jalebee().Jalebee_MainTab_Post().click()
        time.sleep(2)
        # 预期结果
        PostTab_Welcome = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PostTab_Welcome")
        # 获取登录窗口欢迎语
        LogInWindow_Welcome = LogIn().LogInPopup_SelectLoginMode_Tips().text
        time.sleep(2)
        # 断言：
        msg = "游客点击Post成功弹出登录窗口，欢迎语显示"
        self.assertEqual(PostTab_Welcome, LogInWindow_Welcome, E(msg))
        print(P(msg))

    # 登录弹窗——登录方式显示正常
    def test_Case011_LogInWindow_CheckLogInMode(self):
        # 点击展开更多登录方式
        LogIn().LogInPopup_SelectLoginMode_MoreWays().click()
        time.sleep(2)
        # 获取各个登录方式
        FacebookLogIn = LogIn().LogInPopup_SelectLoginMode_SelectFacebook()
        EmailLogIn = LogIn().LogInPopup_SelectLoginMode_SelectEmail()
        PhoneLogIn = LogIn().LogInPopup_SelectLoginMode_SelectPhone()
        GoogleLogIn = LogIn().LogInPopup_SelectLoginMode_SelectGoogle()
        time.sleep(2)
        # 断言：
        msg = "四种登录方式入口"
        self.assertTrue(FacebookLogIn and EmailLogIn and PhoneLogIn and GoogleLogIn, E(msg))
        print(P(msg))

    # 选择Email登录方式——Tips显示正常
    def test_Case012_LogInWindow_SelectEmailLogIn(self):
        # 点击Email LogIn按钮
        LogIn().LogInPopup_SelectLoginMode_SelectEmail().click()
        time.sleep(2)
        # 获取Email注册登录选择弹窗Title
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "EmailLoginMode_Title")
        actValue = LogIn().LogInPopup_EmailLoginMode_Title().text
        time.sleep(2)
        # 断言：
        msg = "Email登录注册选择弹窗 Tips"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # Email登录注册选择页——登录入口显示正常
    def test_Case013_EmailLogInSignUpSelectionPage_CheckLogInEntry(self):
        # 获取数据
        LogInEntry_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "LogInEntry")
        SignUpEntry_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "SignUpEntry")
        time.sleep(2)
        # 获取Email注册登录选择弹窗入口文案
        LogInEntry_actValue = LogIn().LogInPopup_EmailLoginMode_SelectLogIn().text
        SignUpEntry_actValue = LogIn().LogInPopup_EmailLoginMode_SelectSignUp().text
        time.sleep(2)
        # 断言：
        msg1 = "Email登录注册选择弹窗 登录入口"
        msg2 = "Email登录注册选择弹窗 注册入口"
        self.assertEqual(LogInEntry_expValue, LogInEntry_actValue, E(msg1))
        print(P(msg1))
        self.assertEqual(SignUpEntry_expValue, SignUpEntry_actValue, E(msg2))
        print(P(msg2))

    # Email登录注册选择页——其他元素显示正常
    def test_Case014_EmailLogInSignUpSelectionPage_CheckOther(self):
        # 获取Email注册登录选择弹窗其他元素
        Close_Btn = LogIn().LogInPopup_EmailLoginMode_SelectClose()
        Cancel_Btn = LogIn().LogInPopup_EmailLoginMode_SelectCancel()
        time.sleep(2)
        # 断言：
        msg = "Email登录注册选择弹窗 关闭和取消按钮"
        self.assertTrue(Close_Btn and Cancel_Btn, E(msg))
        print(P(msg))

    # Email登录注册选择页——邮箱登录
    def test_Case015_EmailLogInPage_InputBox_EmailInput(self):
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
        # 断言：
        msg = "输入邮箱登录帐号"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 邮箱登录页-输入框-明文密码
    def test_Case016_EmailLogInPage_InputBox_InputVisibility(self):
        # 点击明文密码按钮
        LogIn().EmailLogInPage_InputBox_InputVisibility().click()
        time.sleep(2)
        # 获取Password输入框password属性
        expValue = "false"
        actValue = LogIn().EmailLogInPage_InputBox_PasswordInput().get_attribute("password")
        time.sleep(2)
        # 断言：
        msg = "明文密码功能"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 邮箱登录页-输入框-输入密码
    def test_Case017_EmailLogInPage_InputBox_PasswordInput(self):
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
        # 断言：
        msg = "输入登录密码"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 邮箱登录页-登录-确认登录
    def test_Case018_EmailLogInPage_LogIn_Confirm(self):
        # 点击确认登录按钮
        LogIn().EmailLogInPage_LogIn_Confirm().click()
        time.sleep(5)
        # 尝试查找邮箱登录页顶部Title
        actValue = LogIn().EmailLogInPage_Title_Text()
        time.sleep(2)
        # 断言：
        msg = "邮箱登录"
        self.assertFalse(actValue, E(msg))
        print(P(msg))

    # 处理权限弹窗-进入拍摄页面
    def test_Case019_Jurisdiction_LiveClick(self):
        # 获取权限申请文案
        Hindi_Recording_Jurisdiction = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "Hindi_Recording_Jurisdiction")
        # 处理权限申请弹窗
        Popup().SingPopup_Jurisdiction_LiveClick(text=Hindi_Recording_Jurisdiction)
        time.sleep(10)
        # 获取添加音乐引导文案
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "Guide_AddMusic")
        actValue = Jalebee().JalebeeShootingPage_Function_AddMusicGuide().text
        time.sleep(2)
        # 断言：
        msg = "登录成功后直接进入拍摄页面"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 校验拍摄页 页面元素
    def test_Case020_JalebeeShootingPage_CheckElements(self):
        # 处理引导弹窗
        Jalebee().JalebeeShootingPage_Function_AddMusicGuide().click()
        time.sleep(5)
        # -----检查页面各元素-----
        # 进度条
        Progress_Bar = Jalebee().JalebeeShootingPage_Function_ProgressBar()
        # 关闭按钮
        Close_Btn = Jalebee().JalebeeShootingPage_Function_CloseBtn()
        # 音乐icon
        Music_Icon = Jalebee().JalebeeShootingPage_Function_MusicIcon()
        # 当前选择音乐
        Music_Name = Jalebee().JalebeeShootingPage_Function_MusicName()
        # 手电筒
        Flashlight = Jalebee().JalebeeShootingPage_Function_Flashlight()
        # 切换摄像头
        Switching_Camera = Jalebee().JalebeeShootingPage_Function_SwitchingCamera()
        # 美颜
        Beauty = Jalebee().JalebeeShootingPage_Function_Beauty()
        # 滤镜
        Filter = Jalebee().JalebeeShootingPage_Function_Filter()
        # 相册
        Album = Jalebee().JalebeeShootingPage_Function_Album()
        # 拍摄按钮
        Shot_Btn = Jalebee().JalebeeShootingPage_Function_StartBtn()
        # 拍摄模式-Photo
        ShootingMode_Photo = Jalebee().JalebeeShootingPage_Function_ShootingMode_Photo()
        # 拍摄模式-15S
        ShootingMode_15S = Jalebee().JalebeeShootingPage_Function_ShootingMode_15S()
        # 拍摄模式-60S
        ShootingMode_60S = Jalebee().JalebeeShootingPage_Function_ShootingMode_60S()
        time.sleep(2)
        # 断言：
        msg = "拍摄页13个元素正常展示"
        self.assertTrue(
            Progress_Bar and Close_Btn and Music_Icon and Music_Name and Flashlight and Switching_Camera and Beauty and
            Filter and Album and Shot_Btn and ShootingMode_Photo and ShootingMode_15S and ShootingMode_60S, E(msg))
        print(P(msg))

    # 拍摄页-默认选择15S拍摄模式(该元素selected属性异常，待修复)
    @unittest.expectedFailure  # 如果test失败，不计入失败case目录
    def test_Case021_JalebeeShootingPage_ShootingMode_CheckDefaultChoice(self):
        expValue = "false"  # T38816
        # 获取拍摄页15S模式属性为选中状态
        actValue = Jalebee().JalebeeShootingPage_Function_ShootingMode_15S().get_attribute("selected")
        time.sleep(2)
        # 断言：
        msg = "拍摄页默认选择15S拍摄模式(T38816:该元素selected属性异常，待修复)"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 进入音乐选择页-校验Title
    def test_Case022_JalebeeShootingPage_AddMusic_CheckSelectMusicPageTitle(self):
        # 点击当前选择音乐进入切换音乐页面
        Jalebee().JalebeeShootingPage_Function_MusicName().click()
        # 获取Title文案
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee","SelectMusicPage_Title")
        # 获取音乐选择页Title
        actValue = Jalebee().JalebeeSelectMusicPage_Title().text
        time.sleep(2)
        # 断言：
        msg = "成功进入音乐选择页，页面Title显示"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 校验音乐选择页 内容Tab
    def test_Case023_JalebeeSelectMusicPage_CheckFeedTab(self):
        # 获取Explore/FAVORITE文案
        Explore_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "SelectMusicPage_Explore")
        Favorite_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "SelectMusicPage_Favorite")
        time.sleep(2)
        # 获取音乐选择页Title
        Explore_actValue = Jalebee().JalebeeSelectMusicPage_FeedTab_Explore().text
        Favorite_actValue = Jalebee().JalebeeSelectMusicPage_FeedTab_Favorite().text
        time.sleep(2)
        # 断言：
        msg1 = "音乐选择页 Explore_Tab文案显示"
        msg2 = "音乐选择页 Favorite_Tab文案显示"
        self.assertEqual(Explore_expValue, Explore_actValue, E(msg1))
        print(P(msg1))
        self.assertEqual(Favorite_expValue, Favorite_actValue, E(msg2))
        print(P(msg2))

    # 音乐选择页 默认展示推荐页Explore(该元素selected属性异常，待修复)
    @unittest.expectedFailure  # 如果test失败，不计入失败case目录
    def test_Case024_JalebeeSelectMusicPage_FeedTab_CheckDefaultChoice(self):
        expValue = "false"  # T38816
        # 获取Explore_Tab的属性为选中状态
        actValue = Jalebee().JalebeeSelectMusicPage_FeedTab_Explore().get_attribute("selected")
        time.sleep(2)
        # 断言：
        msg = "默认展示推荐页Explore(T38816:该元素selected属性异常，待修复)"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 校验音乐选择页 页面元素
    def test_Case025_JalebeeSelectMusicPage_CheckElements(self):
        # -----检查页面各元素-----
        # 关闭按钮
        CLose_Btn = Jalebee().JalebeeSelectMusicPage_Function_Close()
        # 搜索框
        Search_Box = Jalebee().JalebeeSelectMusicPage_Function_Search()
        # 音乐分类
        Music_Category = Jalebee().JalebeeSelectMusicPage_Function_Category()
        # 音乐名
        MusicName = Jalebee().JalebeeSelectMusicPage_Function_SongsName()
        # 收藏
        Favor = Jalebee().JalebeeSelectMusicPage_Function_Favor()
        time.sleep(2)
        # 断言：
        msg = "音乐选择页5类元素正常展示"
        self.assertTrue(CLose_Btn and Search_Box and Music_Category and MusicName and Favor, E(msg))
        print(P(msg))

    # 选择音乐返回拍摄页
    def test_Case026_JalebeeSelectMusicPage_SelectMusic_BackShootingPage(self):
        # 点击第一个音乐以播放
        Jalebee().JalebeeSelectMusicPage_Function_SongsName().click()
        time.sleep(2)
        # 记录该音乐名称
        MusicName_expValue = Jalebee().JalebeeSelectMusicPage_Function_SongsName().text
        time.sleep(2)
        # 选择该音乐返回拍摄页
        Jalebee().JalebeeSelectMusicPage_Function_USE().click()
        time.sleep(8)
        # 获取拍摄页当前音乐名称
        MusicName_actValue = Jalebee().JalebeeShootingPage_Function_MusicName().text
        time.sleep(2)
        # 断言：
        msg = "选择音乐返回拍摄页，音乐切换成功"
        self.assertEqual(MusicName_expValue, MusicName_actValue, E(msg))
        print(P(msg))

    # 选择音乐后拍摄页显示取消音乐选择按钮
    def test_Case027_JalebeeShootingPage_SelectMusic_ShowDeselectedMusicBtn(self):
        # 查找取消音乐选择按钮
        DeselectedMusicBtn = Jalebee().JalebeeShootingPage_Function_DeselectedMusic()
        time.sleep(2)
        # 断言:
        msg = "选择音乐后拍摄页显示取消音乐选择按钮"
        self.assertTrue(DeselectedMusicBtn, E(msg))
        print(P(msg))

    # 拍摄15S视屏发布
    def test_Case028_JalebeeShootingPage_Shooting15SPost(self):
        time.sleep(2)
        # 点击Start按钮进行拍摄
        Jalebee().JalebeeShootingPage_Function_StartBtn().click()
        time.sleep(20)
        # 查找发布预览页进度条
        actValue = Jalebee().JalebeePostPreviewPage_Function_ProgressBar()
        time.sleep(2)
        # 断言：
        msg = "录制15S后自动跳转至发布预览页"
        self.assertTrue(actValue, E(msg))
        print(P(msg))

    # 发布预览页元素校验
    def test_Case029_JalebeePostPreviewPage_CheckElement(self):
        # -----获取页面元素-----
        # 返回按钮
        Back = Jalebee().JalebeePostPreviewPage_Function_Back()
        # 音效调整
        Volume = Jalebee().JalebeePostPreviewPage_Function_Volume()
        # 音乐剪切
        Cut_Music = Jalebee().JalebeePostPreviewPage_Function_CutMusic()
        # 选择音乐
        Select_Music = Jalebee().JalebeePostPreviewPage_Function_SelectMusic()
        # 选择封面
        Cover = Jalebee().JalebeePostPreviewPage_Function_Cover()
        # 断言：
        msg = "发布预览页元素正常展示"
        self.assertTrue(Back and Volume and Cut_Music and Select_Music and Cover, E(msg))
        print(P(msg))

    # 点击Next进入发布编辑页
    def test_Case030_ClickNext_JumpPostEditPage(self):
        # 点击Next按钮
        Jalebee().JalebeePostPreviewPage_Function_Next().click()
        time.sleep(2)
        # 获取发布编辑页Title文案
        expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PostPreviewPage_Title")
        actValue = Jalebee().JalebeePostEditPage_Title().text
        time.sleep(2)
        # 断言：
        msg = "点击Next进入发布编辑页，页面Title显示文案正确"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 发布编辑页 输入文字框默认文案，光标聚焦校验
    def test_Case031_JalebeePostEditPage_CheckMindWriting(self):
        # 获取发布编辑页MindWriting文案
        expValue1 = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "PostPreviewPage_MindWriting")
        actValue1 = Jalebee().JalebeePostEditPage_Function_MindWriting().text
        time.sleep(2)
        # 获取发布编辑页MindWriting光标聚焦状态
        expValue2 = "true"
        actValue2 = Jalebee().JalebeePostEditPage_Function_MindWriting().get_attribute("focused")
        time.sleep(2)
        # 断言：
        msg1 = "发布编辑页 MindWriting默认文案显示，"
        msg2 = "发布编辑页 MindWriting光标聚焦状态"
        self.assertEqual(expValue1, actValue1, E(msg1))
        print(P(msg1))
        self.assertEqual(expValue2, actValue2, E(msg2))
        print(P(msg2))

    # 发布编辑页 页面元素校验
    def test_Case032_JalebeePostEditPage_CheckElements(self):
        # -----获取页面元素-----
        # 返回
        Back = Jalebee().JalebeePostEditPage_Function_Back()
        # 更换封面
        SetCover = Jalebee().JalebeePostEditPage_Function_SetCover()
        # @好友
        RemindFriends = Jalebee().JalebeePostEditPage_Function_RemindFriends()
        # Topic
        Topic = Jalebee().JalebeePostEditPage_Function_Topic()
        # 定位
        Location = Jalebee().JalebeePostEditPage_Function_Location()
        # 保存草稿
        Draft = Jalebee().JalebeePostEditPage_Function_Draft()
        # 断言：
        msg = "发布编辑页元素正常展示"
        self.assertTrue(Back and SetCover and RemindFriends and Topic and Location and Draft, E(msg))
        print(P(msg))

    # 发布拍摄作品
    def test_Case033_JalebeePostEditPage_PostShoot(self):
        # 点击发布按钮
        Jalebee().JalebeePostEditPage_Function_Post().click()
        time.sleep(5)
        # 循环等待发布完成
        while Jalebee().JalebeeFollowingPage_PublishBar():
            time.sleep(5)
        # 获取Following页作品like数
        expValue = "3"
        actValue = Jalebee().JalebeeFollowingPage_ShootLikeNumS_Count()
        time.sleep(2)
        # 断言：
        msg = "发布拍摄作品，自动跳转到Following页，作品出现在feed首个卡片"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 点击Message按钮，进入消息页面
    def test_Case034_ClickMessageTab_EnterMessagePage(self):
        # 点击底部Message_Tab
        Jalebee().JalebeeHomePage_MainTab_Message().click()
        time.sleep(2)
        # 获取底部Message-Tab按钮属性为选中状态
        expValue = "true"
        actValue = Jalebee().JalebeeHomePage_MainTab_Message().get_attribute("selected")
        time.sleep(2)
        # 断言：
        msg = "成功跳转消息页面"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 校验功能入口
    def test_Case035_JalebeeMessagePage_CheckFunctionEntry(self):
        # 读取功能入口预期文案
        System_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "JalebeeMessagePage_System")
        Gifts_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "JalebeeMessagePage_Gifts")
        Messages_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "JalebeeMessagePage_Messages")
        time.sleep(2)
        # 获取对应元素text
        System_actValue = Jalebee().JalebeeMessagePage_Function_System().text
        Gifts_actValue = Jalebee().JalebeeMessagePage_Function_Gifts().text
        Messages_actValue = Jalebee().JalebeeMessagePage_Function_Messages().text
        time.sleep(2)
        # 断言：
        msg1 = "消息页 系统消息入口正常，"
        msg2 = "消息页 礼物消息入口正常"
        msg3 = "消息页 私信消息入口正常"
        self.assertEqual(System_expValue, System_actValue, E(msg1))
        print(P(msg1))
        self.assertEqual(Gifts_expValue, Gifts_actValue, E(msg2))
        print(P(msg2))
        self.assertEqual(Messages_expValue, Messages_actValue, E(msg3))
        print(P(msg3))

    # 校验消息页Tab
    def test_Case036_JalebeeMessagePage_CheckFeedTab(self):
        # 读取FeedTab预期文案
        FollowingTab_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "JalebeeMessagePage_FollowingTab")
        YouTab_expValue = ReadXMLData().returnXMLFile("Jalebee.xml", "Jalebee", "JalebeeMessagePage_YouTab")
        time.sleep(2)
        # 获取对应元素text
        FollowingTab_actValue = Jalebee().JalebeeMessagePage_FeedTab_FOLLOWING().text
        YouTab_actValue = Jalebee().JalebeeMessagePage_FeedTab_YOU().text
        time.sleep(2)
        # 断言：
        msg1 = "消息页 Following-Tab 正常，"
        msg2 = "消息页 You-Tab 正常"
        self.assertEqual(FollowingTab_expValue, FollowingTab_actValue, E(msg1))
        print(P(msg1))
        self.assertEqual(YouTab_expValue, YouTab_actValue, E(msg2))
        print(P(msg2))

    # 校验消息页消息内容
    def test_Case037_JalebeeMessagePage_CheckNotification(self):
        # 获取Following-Tab下内容
        Jalebee().JalebeeMessagePage_FeedTab_FOLLOWING().click()
        FollowingTab_MessageContent = Jalebee().JalebeeMessagePage_MessageContent()
        time.sleep(2)
        # 获取You-Tab下内容
        Jalebee().JalebeeMessagePage_FeedTab_YOU().click()
        YouTab_MessageCotent = Jalebee().JalebeeMessagePage_MessageContent()
        time.sleep(2)
        # 断言：
        msg = "消息页 消息内容展示"
        self.assertTrue(FollowingTab_MessageContent and YouTab_MessageCotent, E(msg))
        print(P(msg))

    # 点击Me按钮，进入个人页
    def test_Case038_ClickMeTab_EnterProfilePage(self):
        # 点击Me按钮
        Jalebee().JalebeeHomePage_MainTab_Me().click()
        time.sleep(5)
        # 获取Me-Tab按钮属性为选中状态
        expValue = "true"
        # 获取首页Me-Tab按钮属性为选中状态
        actValue = Jalebee().JalebeeHomePage_MainTab_Me().get_attribute("selected")
        time.sleep(2)
        # 断言：
        msg = "成功跳转至Profile页"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页背景图头像校验
    def test_Case039_JalebeeProfilePage_CheckUserInfo_BackgroundAndHeadView(self):
        # 获取页面背景图和头像
        Background = Profile().ProfilePage_UserInfo_Background()
        HeadView = Profile().ProfilePage_UserInfo_HeadView()
        time.sleep(2)
        # 断言：
        msg = "个人页 背景图和头像展示"
        self.assertTrue(Background and HeadView, E(msg))
        print(P(msg))

    # 个人页个人信息校验——用户名
    def test_Case040_JalebeeProfilePage_CheckUserInfo_StageName(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "StageName")
        # 获取用户昵称
        actValue = Profile().ProfilePage_UserInfo_StageName().text
        time.sleep(2)
        # 断言
        msg = "个人页 用户昵称显示"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页个人信息校验——等级
    def test_Case041_JalebeeProfilePage_CheckUserInfo_UserLevel(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "UserLevel")
        # 获取用户等级
        actValue = Profile().ProfilePage_UserInfo_UserLevel().text
        time.sleep(2)
        # 断言：
        msg = "个人页 用户等级显示"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页个人信息校验——VIP状态
    def test_Case042_JalebeeProfilePage_CheckUserInfo_VIPLevel(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "VIPLevel")
        # 获取用户VIP状态
        actValue = Profile().ProfilePag_UserInfo_VIPLevel().text
        time.sleep(2)
        # 断言：
        msg = "个人页 VIP状态"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页个人信息校验——Followers数正确
    def test_Case043_JalebeeProfilePage_CheckUserInfo_FollowersCount(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Followers")
        # 获取用户Followers数
        actValue = Profile().ProfilePage_UserInfo_FollowersNumber().text
        time.sleep(2)
        # 断言：
        msg = "个人页 Followers数正确"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页个人信息校验——Following数正确
    def test_Case044_JalebeeProfilePage_CheckUserInfo_Following(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Following")
        # 获取用户Following数
        actValue = Profile().ProfilePage_UserInfo_FollowingNumber().text
        time.sleep(2)
        # 断言
        msg = "个人页 Following数正确"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页功能栏校验——功能列表显示正确
    def test_Case045_JalebeeProfilePage_CheckFunction(self):
        # 获取功能列表
        TextList = ReadXMLData().returnXMLFile("ProfileText.xml", "ProfileText", "FunctionBar_TextList")
        # 断言：
        msg = "个人页 功能栏列表入口显示"
        actValue = Page_Element_Verification().PEV_IDS(Profile().ProfilePage_CheckList_FunctionBar(), TextList)
        time.sleep(2)
        self.assertTrue(actValue, E(msg))
        print(P(msg))

    # 个人页Tab栏校验——Tab列表显示正确
    def test_Case046_JalebeeProfilePage_CheckTabBar(self):
        # 获取Tab列表
        TextList = ReadXMLData().returnXMLFile("ProfileText.xml", "ProfileText", "TabBar_TextList")
        # 向上滑动1/2屏
        Screen().SWipeUp_Half()
        # 断言：
        msg = "个人页 Tab列表入口显示"
        actValue = Page_Element_Verification().PEV_IDS(Profile().ProfilePage_CheckList_TabBar(), TextList)
        time.sleep(2)
        self.assertTrue(actValue, E(msg))
        print(P(msg))

    # 个人页ProfileTab校验-Personal_Info Tips
    def test_Case047_JalebeeProfilePage_ProfileTab_CheckPersonalInfoTips(self):
        # 获取多语言文案
        expValue = Internationalization().Internationalization("Personal_info", "IN")
        # 向上滑动1/2屏
        Screen().SWipeUp_Half()
        time.sleep(2)
        # 点击Profile-Tab
        Profile().ProfilePage_Tab_ProfileTab().click()
        time.sleep(5)
        # 获取 Personal_Info Title
        actValue = Profile().ProfilePage_ProfileTab_PersonalInfo_Text().text
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-Personal_Info Tips文案"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页ProfileTab校验-Personal_Info 内容
    def test_Case048_JalebeeProfilePage_ProfileTab_CheckPersonalInfoDesc(self):
        # 读取预期文案
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "PersonalInfo")
        # 获取当前用户个人信息
        actValue = Profile().ProfilePage_ProfileTab_PersonalInfo_Desc().text
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-Personal_Info Desc文案"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页ProfileTab校验-Album Tips
    def test_Case049_JalebeeProfilePage_ProfileTab_CheckAlbumTips(self):
        # 获取多语言文案
        expValue = Internationalization().Internationalization("Album", "IN")
        # 获取 Album Tips
        actValue = Profile().ProfilePage_ProfileTab_Album_Text().text
        # 判断 Album 正常展示
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-Album Tips文案"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页ProfileTab校验-Album 数量
    def test_Case050_JalebeeProfilePage_ProfileTab_CheckAlbumCount(self):
        # 获取用户Album 图片数量
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Album_PhotoCount")
        # 获取Album 图片数量 并截图
        actValue = str(len(self.driver.find_elements_by_id(Profile().ProfilePage_ProfileTab_Album_PhotosCount())))
        # 断言：
        msg = "个人页ProfileTab校验-图片数量展示正确"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页ProfileTab校验-TopFans Tips
    def test_Case051_JalebeeProfilePage_ProfileTab_CheckTopFansTips(self):
        # 获取多语言文案
        expValue = Internationalization().Internationalization("Top_Fans", "IN")
        # 获取 TopFans Tips
        actValue = Profile().ProfilePage_ProfileTab_TopFans_Text().text
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-TopFans Tips"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页ProfileTab校验-TopFans 星光值展示正确
    def test_Case052_JalebeeProfilePage_ProfileTab_CheckStarlight(self):
        # 读取用户星光值信息
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Starlight")
        # 获取当前用户星光值
        actValue = Profile().ProfilePage_ProfileTab_TopFans_Starlight().text
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-TopFans 星光值"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页ProfileTab校验-TopFans 头像显示正常
    def test_Case053_JalebeeProfilePage_ProfileTab_CheckTopFansHeadView(self):
        # 查找三个头像
        First_actValue = Profile().ProfilePage_ProfileTab_TopFans_FindFirstHeadView()
        Second_actValue = Profile().ProfilePage_ProfileTab_TopFans_FindSecondHeadView()
        Third_actValue = Profile().ProfilePage_ProfileTab_TopFans_FindThirdHeadView()
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-TopFans 头像显示正常"
        if all([First_actValue, Second_actValue, Third_actValue]):
            self.assertTrue(First_actValue, E(msg))
            print(P(msg))
        else:
            print("FirstHeadView:" + First_actValue)
            print("SecondHeadView:" + Second_actValue)
            print("ThirdHeadView:" + Third_actValue)

    # 个人页ProfileTab校验-Contribute Tips
    def test_Case054_JalebeeProfilePage_ProfileTab_CheckContribute(self):
        # 获取多语言文案
        expValue = Internationalization().Internationalization("Contribute", "IN")
        # 获取Contribute Tips
        actValue = Profile().ProfilePage_ProfileTab_Contribute_Text().text
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-Contribute Tips"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # Contribute 金币数正确
    def test_Case055_JalebeeProfilePage_ProfileTab_CheckGoldCount(self):
        # 获取用户消费金币数
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Golds")
        # 获取 Contribute 金币数
        actValue = Profile().ProfilePage_ProfileTab_Contribute_Gold().text
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-Contribute 金币数"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # Store 正常展示
    def test_Case056_JalebeeProfilePage_ProfileTab_CheckStore(self):
        # 获取多语言文案
        expValue = Internationalization().Internationalization("Store", "IN")
        # 获取 Store Tips
        actValue = Profile().ProfilePage_ProfileTab_Store_Text().text
        time.sleep(2)
        # 断言：
        msg = "个人页ProfileTab校验-Store Tips"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页MomentsTab校验—删除作品校验作品数统计
    def test_Case057_JalebeeProfilePage_MomentsTab_DelShootCheckCountNum(self):
        # 点击MomentsTab
        Profile().ProfilePage_Tab_MomentsTab().click()
        time.sleep(5)
        # 获取帐号作品数
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "ProfilePage_ShootCounts")
        CountNum = Profile().ProfilePage_MomentsTab_CountNum().text
        # 提取数字
        actValue = re.sub("\\D", "", CountNum)
        time.sleep(2)
        # 点击首个作品More按钮
        Profile().ProfilePage_MomentsTab_ShootInfo_More().click()
        time.sleep(2)
        # 删除刚刚发布的作品
        Profile().ProfilePage_MomentsTab_ShootInfo_More_Delete().click()
        time.sleep(2)
        # 确认删除
        Profile().ProfilePage_MomentsTab_ShootInfo_More_Delete_Confirm().click()
        time.sleep(2)
        # 断言：
        msg = "个人页MomentsTab校验-删除作品功能，作品数统计"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页MomentsTab校验—私密标签
    def test_Case058_JalebeeProfilePage_MomentsTab_CheckPrivateTag(self):
        # 获取多语言文案
        expValue = Internationalization().Internationalization("Private", "IN")
        actValue = Profile().ProfilePage_MomentsTab_ShootInfo_Private().text
        time.sleep(2)
        # 断言：
        msg = "个人页MomentsTab校验-私密标签"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页MomentsTab校验—Title校验
    def test_Case059_JalebeeProfilePage_BrowseBottomTab_ShowTitle(self):
        # 获取测试数据
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "StageName")
        # 获取顶部Title
        actValue = Profile().ProfilePage_Title().text
        time.sleep(2)
        # 断言
        msg = "个人页 当浏览底部Tab时展示Title"
        self.assertEqual(expValue, actValue, E(msg))
        print(P(msg))

    # 个人页MomentsTab校验—其他元素校验
    def test_Case060_JalebeeProfilePage_MomentsTab_CheckElement(self):
        # 添加朋友
        FindFriends = Profile().ProfilePage_FindFriends()
        # 设置
        Setting = Profile().ProfilePage_Setting()
        # 发布时间
        PostTime = Profile().ProfilePage_MomentsTab_ShootInfo_PostTime()
        # Like
        Like = Profile().ProfilePage_MomentsTab_ShootInfo_Like()
        # Comment
        Comment = Profile().ProfilePage_MomentsTab_ShootInfo_Comment()
        # Share
        Share = Profile().ProfilePage_MomentsTab_ShootInfo_Share()
        time.sleep(2)
        # 断言：
        msg = "个人页MomentsTab校验—其他元素校验"
        self.assertTrue(FindFriends and Setting and PostTime and Like and Comment and Share, E(msg))
        print(P(msg))

