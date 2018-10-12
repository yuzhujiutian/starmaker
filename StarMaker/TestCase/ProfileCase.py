# coding=utf-8
import time
import unittest
from CommonView.Popup import Popup
from CommonView.Profile import Profile
from CommonView.Home import Home
from CommonView import LogIn
from Utils.Tools import Tools
from Utils.Tools import Screen
from Utils.Tools import RegionalSliding
from Utils.Tools import Page_Element_Verification
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.ReadXMLData import ReadXMLData


class ProfileCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)
        Popup().HomePopup_CheckIn_Close_LiveClick()
        # 如果未登录
        if LogIn.StartUpTransition():
            # 处理首登引导弹窗
            Popup().HomePopup_NewFeature_NEXT_LiveClick()
            time.sleep(1)
            Popup().HomePopup_NewFeatureAdded_NEXT_LiveClick()
            time.sleep(1)
            Popup().HomePopup_NewFeatureSing_NEXT_LiveClick()
            time.sleep(1)
            Popup().HomePopup_NewFeaturePostOther_DONE_LiveClick()
            time.sleep(1)
            # 点击Profile-Tab进入Profile页
            Home().HomeTab_Profile().click()
            # 处理邮箱认证弹窗
            Popup().HomePopup_VerifyEmail_Close_LiveClick()
        else:
            # 处理签到弹窗
            Popup().HomePopup_CheckIn_Close_LiveClick()
            time.sleep(3)
            # # 点击Profile-Tab进入Profile页
            # Home().HomeTab_Profile().click()
            Screen().AccurateClicks_Percentage(0.902, 0.957, 500)
            time.sleep(3)
            # 处理邮箱认证弹窗
            Popup().HomePopup_VerifyEmail_Close_LiveClick()
            time.sleep(5)

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # Profile页展示用户昵称正确
    def test_Case001_StageNameCase(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "StageName")
        # 获取用户昵称
        actValue = Profile().Profile_StageName().text
        time.sleep(1)
        # 判断昵称正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户等级正确
    def test_Case002_UserLevelCase(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "UserLevel")
        # 获取用户等级
        actValue = Profile().Profile_UserLevel().text
        time.sleep(1)
        # 判断等级正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户VIP状态正确
    def test_Case003_VIPLevelCase(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "VIPLevel")
        # 获取用户VIP状态
        actValue = Profile().Profile_VIPLevel().text
        time.sleep(1)
        # 判断VIP状态正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户Followers数正确
    def test_Case004_FollowersCase(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Followers")
        # 获取用户Followers数
        actValue = Profile().Profile_FollowersNumber().text
        time.sleep(1)
        # 判断Followers数正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户Following数正确
    def test_Case005_FollowingCase(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Following")
        # 获取用户Following数
        actValue = Profile().Profile_FollowingNumber().text
        time.sleep(1)
        # 判断Following数正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户上榜作品数正确
    def test_Case006_RankRecordsCase(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "RankRecords")
        # 获取用户上榜作品数
        actValue = Profile().Profile_RankRecords().text
        time.sleep(1)
        # 判断上榜作品数正确
        self.assertEqual(expValue, actValue)

    # Profile页功能栏第一页——功能列表显示正确
    def test_Case007_FunctionBar1_check(self):
        # 获取功能列表
        TextList = ReadXMLData().returnXMLFile("ProfileText.xml", "ProfileText", "FunctionBar_TextList1")
        # 查看当前功能栏是否显示正确
        actValue = Page_Element_Verification().PEV_IDS(Profile().Profile_FunctionBar(), TextList)
        self.assertTrue(actValue)

    # Profile页功能栏第二页——功能列表显示正确
    def test_Case008_FunctionBar2_check(self):
        # 获取功能列表
        TextList = ReadXMLData().returnXMLFile("ProfileText.xml", "ProfileText", "FunctionBar_TextList2")
        # 在功能栏区域内滑动到第二页
        RegionalSliding(Profile().Profile_FunctionBar()).Transverse()
        # 查看当前功能栏是否显示正确
        actValue = Page_Element_Verification().PEV_IDS(Profile().Profile_FunctionBar(), TextList)
        self.assertTrue(actValue)

    # Profile页Tab栏——Tab列表显示正确
    def test_Case009_TabBar_check(self):
        # 获取Tab列表
        TextList = ReadXMLData().returnXMLFile("ProfileText.xml", "ProfileText", "TabBar_TextList1")
        # 向上滑动1/4屏
        Screen().SWipeUp_Quarter()
        # 查看当前Tab栏是否显示正确
        actValue = Page_Element_Verification().PEV_IDS(Profile().Profile_TabBar(), TextList)
        self.assertTrue(actValue)

    # Profile页 Personal_Info 正常展示
    def test_Case010_ShowPersonalInfoCase(self):
        expValue = "Personal info"
        # 向上滑动1/2屏
        Screen().SWipeUp_Half()
        time.sleep(2)
        Profile().Profile_Tab_PROFILE().click()
        time.sleep(1)
        # 获取 Personal_Info Title
        actValue = Profile().PersonalInfo_Title().text
        # 判断 Personal_Info 正常展示
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # PROFILE_Tab 个人信息描述正确
    def test_Case011_ShowPersonalInfo_descCase(self):
        # 读取用户个人信息
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "PersonalInfo")
        # 获取当前用户个人信息
        actValue = Profile().PersonalInfo_desc().text
        # 判断个人信息描述正确
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # PROFILE_Tab 校验
    # Album 正常展示
    def test_Case012_ShowAlbumCase(self):
        expValue = "Album"
        # 获取 Album Title
        actValue = Profile().Album_Title().text
        # 判断 Album 正常展示
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # Album 图片数量统计
    def test_Case013_Album_PhotoCountCase(self):
        # 获取用户Album 图片数量
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Album_PhotoCount")
        # 获取Album 图片数量 并截图
        actValue = str(len(self.driver.find_elements_by_class_name("android.widget.ScrollView")) - 1)
        # 判断 图片数量展示正确
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # TopFans 正常展示
    def test_Case014_ShowTopFansCase(self):
        expValue = "Top Fans"
        # 获取 TopFans Title
        actValue = Profile().TopFans_Title().text
        # 判断 TopFans 正常展示
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # TopFans 星光值展示正确
    def test_Case015_TopFans_StarlightCase(self):
        # 读取用户星光值信息
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Starlight")
        # 获取当前用户星光值
        actValue = Profile().Starlight().text
        # 判断星光值展示正确
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # TopFans 头像显示正常
    def test_Case016_TopFans_ShowHeadView(self):
        # 查找三个头像
        First_actValue = Profile().TopFans_FindFirstHeadView()
        Second_actValue = Profile().TopFans_FindSecondHeadView()
        Third_actValue = Profile().TopFans_FindThirdHeadView()
        # 判断头像显示正常
        time.sleep(1)
        if all([First_actValue, Second_actValue, Third_actValue]):
            self.assertTrue(First_actValue)
        else:
            print("FirstHeadView:" + First_actValue)
            print("SecondHeadView:" + Second_actValue)
            print("ThirdHeadView:" + Third_actValue)

    # Contribute 正常展示
    def test_Case017_ShowContributeCase(self):
        time.sleep(5)
        expValue = "Contribute"
        # 获取Contribute Title
        actValue = Profile().Contribute_Title().text
        print(actValue)
        # 判断 Contribute 正常展示
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # Contribute 金币数正确
    def test_Case018_Contribute_GoldCountCase(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Golds")
        # 获取 Contribute 金币数
        actValue = Profile().Contribute_Gold().text
        # 判断金币数正确
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # Store 正常展示
    def test_Case019_ShowStoreCase(self):
        expValue = "Store"
        # 获取 Store Title
        actValue = Profile().Store_Title().text
        # 判断 Contribute 正常展示
        time.sleep(1)
        self.assertEqual(expValue, actValue)
        time.sleep(3)
