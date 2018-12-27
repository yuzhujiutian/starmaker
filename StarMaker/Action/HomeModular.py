# coding=utf-8
import time
import unittest
from CommonView.Home import Home
from CommonView.HotTopics import HotTopics
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.Tools import ToastTips_Processing


# 默认首页
class HomeModular(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)

    def setUp(self):
        pass

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # ----------
    # 首页-MainTab
    # ----------
    # 首页-切换到HomeTab
    def test_Case001_HomePage_SwitchTab_SelectHomeTab(self):
        Home().HomePage_MainTab_HomeTab().click()
        time.sleep(2)
        # 获取HomeTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_HomeTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到HomeTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到DiscoverTab
    def test_Case002_HomePage_SwitchTab_SelectDiscoverTab(self):
        Home().HomePage_MainTab_DiscoverTab().click()
        time.sleep(2)
        # 获取DiscoverTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_DiscoverTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到DiscoverTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到PostTab
    def test_Case003_HomePage_SwitchTab_SelectPostTab(self):
        Home().HomePage_MainTab_PostTab().click()
        time.sleep(2)
        # 获取PostTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_PostTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PostTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到NotificationTab
    def test_Case004_HomePage_SwitchTab_SelectNotificationTab(self):
        Home().HomePage_MainTab_NotificationTab().click()
        time.sleep(2)
        # 获取NotificationTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_NotificationTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到NotificationTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到ProfileTab
    def test_Case005_HomePage_SwitchTab_SelectProfileTab(self):
        Home().HomePage_MainTab_ProfileTab().click()
        time.sleep(2)
        # 获取ProfileTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_ProfileTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到ProfileTab
        self.assertEqual(expValue, actValue)

    # ----------
    # 默认首页
    # ----------
    # 首页-切换到Following内容Tab
    def test_Case006_HomePage_SwitchContentTab_SelectFollowingTab(self):
        Home().HomePage_SwitchTab_FollowingTab().click()
        time.sleep(2)
        # 获取FollowingTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_SwitchTab_FollowingTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到FollowingTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到Popular内容Tab
    # English_text=POPULAR/Hindi_text=लोकप्रिय
    def test_Case007_HomePage_SwitchContentTab_SelectPopularTab(self):
        Home().HomePage_SwitchTab_PopularTab().click()
        time.sleep(2)
        # 获取PopularTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_SwitchTab_PopularTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PopularTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到Sing内容Tab
    def test_Case008_HomePage_SwitchContentTab_SelectSingTab(self):
        Home().HomePage_SwitchTab_SingTab().click()
        time.sleep(2)
        # 获取SingTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_SwitchTab_SingTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到SingTab
        self.assertEqual(expValue, actValue)

    # 首页-点击搜索框
    def test_Case009_HomePage_Common_ClickSearch(self):
        Home().HomePage_Common_Search().click()
        time.sleep(2)
        # 断言待补充

    # 首页-点击Library
    def test_Case010_HomePage_Common_ClickLibrary(self):
        Home().HomePage_Common_Library().click()
        time.sleep(2)
        # 断言待补充

    # 首页-点击切换内容语言
    def test_Case011_HomePage_Common_ClickContentLanguage(self):
        Home().HomePage_Common_ContentLanguage().click()
        time.sleep(2)
        # 获取语言选择弹窗Tips(English)
        expValue = "The content displayed will be based on the language you choose."
        actValue = Home().HomePage_ChooseLanguage_IndiaTips().text
        time.sleep(2)
        # 断言：已调起内容语言弹窗
        self.driver.back()
        self.assertEqual(expValue, actValue)

    # ----------
    # 切换内容语言弹窗-选择内容语言
    # ([0]हिन्दी(Hindi)/[1]বাংলা(Bengali)/[2]ಕನ್ನಡ(Kannada)/[3]தமிழ்(Tamil)/[4]ગુજરાતી(Gujarati)/
    # [5]ଓଡ଼ିଆ(Odia)/[6]മലയാളം(Malayalam)/[7]मराठी(Marathi)/[8]తెలుగు(Telugu)/[9]ਪੰਜਾਬੀ(Punjabi)/[10]অসমীয়া(Assamese)/
    # [滑动翻页][-4]हरियाणवी(Haryanvi)/[-3]राजस्थानी(Rajasthani)/[-2]भोजपूरी(Bhojpuri)/[-1]English(English))
    # ----------
    # 切换内容语言弹窗-选择内容语言Hindi
    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Language = "हिन्दी(Hindi)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Hindi_text=लोकप्रिय)
        expValue = "लोकप्रिय"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为印地语
        self.assertEqual(expValue, actValue)

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    def test_Case012_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
        Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(0).click()
        time.sleep(2)
        # 断言待补充

    # ----------
    # 首页-Hot topics
    # ----------
    # 首页Hot topics正常显示
    def test_Case012_HomePage_HotTopics_Existence(self):
        # 获取Hot topics的text
        expValue = "Hot topics"
        actValue = Home().HomePage_HotTopics_Text().text
        time.sleep(2)
        # 断言：首页Hot topics正常显示
        self.assertEqual(expValue, actValue)

    # 首页点击Hot topics的See All
    def test_Case013_HomePage_HotTopics_SeeAll(self):
        Home().HomePage_HotTopics_SeeAll().click()
        time.sleep(2)
        # 获取Hot topics页面的title
        expValue = "Hot Topics"
        actValue = HotTopics().HotTopicsPage_Title_Text().text
        time.sleep(2)
        # 断言：已跳转到Hot Topics页面
        self.driver.back()
        self.assertEqual(expValue, actValue)

    # ----------
    # 首页-卡片
    # ----------
    # 首页-feed卡片_头像(ID/IDS)
    def Source_HomePage_FeedCard_HeadView(self):

    # 首页-feed卡片_用户名(ID/IDS)
    def HomePage_FeedCard_UserName(self):

    # 首页卡片-Follow成功(点击第一个)
    def test_Case011_HomePage_FeedCard_Follow(self):
        Follow_Count_1 = Home().HomePage_FeedCard_FollowCount()
        time.sleep(2)
        if Follow_Count_1 == 1:
            Home().HomePage_FeedCard_Follow().click()
            time.sleep(2)
            # 检查Follow按钮是否消失
            actValue = Home().HomePage_FeedCard_Follow()
            time.sleep(2)
            # 断言：Follow成功
            self.assertFalse(actValue)
        else:
            Home().HomePage_FeedCard_Follow().click()
            time.sleep(2)
            # 检查当前页Follow按钮个数是否-1
            Follow_Count_2 = Home().HomePage_FeedCard_FollowCount()
            expValue = 1
            actValue = Follow_Count_2 - Follow_Count_1
            # 断言：Follow成功
            self.assertEqual(expValue, actValue)

    # 首页卡片，点击叉号调起dislike对话框(点击第一个)
    def test_Case012_HomePage_FeedCard_Dislike(self):
        Home().HomePage_FeedCard_Dislike().click()
        time.sleep(2)
        # 获取dislike对话框的CancelText
        expValue = "Cancel"
        actValue = Home().HomePage_DislikePop_Cancel().text
        time.sleep(2)
        # 断言：已调起dislike对话框
        self.assertEqual(expValue, actValue)

    # 首页卡片，Unwanted
    def test_Case013_HomePage_FeedCard_Unwanted(self):
        Home().HomePage_DislikePop_Unwanted().click()
        time.sleep(2)
        # 循环查找toast提示
        expValue = "You will see fewer similar posts."
        actValue = ToastTips_Processing().ToastTips_TextXpath_IsDisplayed(expValue)
        time.sleep(2)
        # 断言：Unwanted成功
        self.assertTrue(actValue)

    # 首页-feed卡片_描述(ID/IDS)
    def HomePage_FeedCard_Describe(self):

    # 首页-feed卡片_图片(ID/IDS)
    def HomePage_FeedCard_Img(self):

    # 首页-feed卡片_视屏(ID/IDS)
    def HomePage_FeedCard_Video(self):

    # 首页-feed卡片_分享按钮(ID/IDS)
    def HomePage_FeedCard_Share(self):

    # 首页-feed卡片_分享数(ID/IDS)
    def HomePage_FeedCard_ShareCount(self):

    # 首页-feed卡片_评论按钮(ID/IDS)
    def HomePage_FeedCard_Comment(self):

    # 首页-feed卡片_评论数(ID/IDS)
    def HomePage_FeedCard_CommentCount(self):

    # 首页-feed卡片_like按钮(ID/IDS)
    def HomePage_FeedCard_Like(self):

    # 首页-feed卡片_like数(ID/IDS)
    def HomePage_FeedCard_LikeCount(self):

    # 首页-feed卡片_下载按钮(ID/IDS)
    def HomePage_FeedCard_Download(self):

    # 首页-feed卡片_WhatsApp按钮(ID/IDS)
    def HomePage_FeedCard_WhatsApp(self):
