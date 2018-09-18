# coding=utf-8
import time
import unittest
from CommonView.Popup import Popup
from CommonView.Profile import Profile
from CommonView.Home import Home
from CommonView import LogIn
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.ReadXMLData import ReadXMLData


class ProfileCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)
        # 如果未登录
        if LogIn.StartUpTransition():
            # 处理首登引导弹窗
            Popup().HomePopup_NewFeature_OK_LiveClick()
            Popup().HomePopup_RankingGuide_Next_LiveClick()
            print("Parties NEXT")
            Popup().HomePopup_PartiesGuide_Next_LiveClick()
            print("Live DONE")
            Popup().HomePopup_LiveGuide_Done_LiveClick()
            # 点击Profile-Tab进入Profile页
            Home().HomeTab_Profile().click()
            # 处理邮箱认证弹窗
            Popup().HomePopup_VerifyEmail_Close_LiveClick()
        else:
            # 处理签到弹窗
            Popup().HomePopup_CheckIn_Close_LiveClick()
            # 点击Profile-Tab进入Profile页
            Home().HomeTab_Profile().click()
            # 处理邮箱认证弹窗
            Popup().HomePopup_VerifyEmail_Close_LiveClick()

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # Profile页展示用户昵称正确
    def test_Case001_StageName(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "StageName")
        # 获取用户昵称
        actValue = Profile().Profile_StageName().text
        time.sleep(1)
        # 判断昵称正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户等级正确
    def test_Case002_UserLevel(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "UserLevel")
        # 获取用户等级
        actValue = Profile().Profile_UserLevel().text
        time.sleep(1)
        # 判断等级正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户VIP状态正确
    def test_Case003_VIPLevel(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "VIPLevel")
        # 获取用户VIP状态
        actValue = Profile().Profile_VIPLevel().text
        time.sleep(1)
        # 判断VIP状态正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户Followers数正确
    def test_Case004_Followers(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Followers")
        # 获取用户Followers数
        actValue = Profile().Profile_FollowersNumber().text
        time.sleep(1)
        # 判断Followers数正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户Following数正确
    def test_Case005_Following(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "Following")
        # 获取用户Following数
        actValue = Profile().Profile_FollowingNumber().text
        time.sleep(1)
        # 判断Following数正确
        self.assertEqual(expValue, actValue)

    # Profile页展示用户上榜作品数正确
    def test_Case006_RankRecords(self):
        expValue = ReadXMLData().returnXMLFile("AccountNumber.xml", "AccountNumber", "RankRecords")
        # 获取用户上榜作品数
        actValue = Profile().Profile_RankRecords().text
        time.sleep(1)
        # 判断上榜作品数正确
        self.assertEqual(expValue, actValue)

