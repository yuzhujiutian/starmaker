# coding=utf-8
import time
import unittest
from StarMaker.CommonView.Home import Home
from StarMaker.CommonView.Search import Search
from StarMaker.CommonView.HotTopics import HotTopics
from StarMaker.CommonView.Profile import Profile
from StarMaker.CommonView.PlaybackDetails import PlaybackDetails
from StarMaker.Utils.Tools import Tools
from StarMaker.Utils.Tools import Screen
from StarMaker.Utils.Tools import ToastTips_Processing
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver


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
    # 首页-切换到Moment
    def test_Case0101_HomePage_SwitchTab_SelectMomentTab(self):
        Home().HomePage_MainTab_MomentTab().click()
        time.sleep(2)
        # 获取MomentTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_MomentTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到HomeTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到Party
    def test_Case0102_HomePage_SwitchTab_SelectPartyTab(self):
        Home().HomePage_MainTab_PartyTab().click()
        time.sleep(2)
        # 获取PartyTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_PartyTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到DiscoverTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到Sing
    def test_Case0103_HomePage_SwitchTab_SelectSingTab(self):
        Home().HomePage_MainTab_SingTab().click()
        time.sleep(2)
        # 获取Sing的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_SingTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PostTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到Message
    def test_Case0104_HomePage_SwitchTab_SelectMessageTab(self):
        Home().HomePage_MainTab_MessageTab().click()
        time.sleep(2)
        # 获取MessageTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_MessageTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到NotificationTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到Me
    def test_Case0105_HomePage_SwitchTab_SelectMeTab(self):
        Home().HomePage_MainTab_MeTab().click()
        time.sleep(2)
        # 获取MeTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_MeTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到ProfileTab
        self.assertEqual(expValue, actValue)

    # ----------
    # 默认首页
    # ----------
    # 首页-切换到Following内容Tab
    def test_Case0106_HomePage_SwitchContentTab_SelectFollowingTab(self):
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
    def test_Case0107_HomePage_SwitchContentTab_SelectPopularTab(self):
        Home().HomePage_SwitchTab_PopularTab().click()
        time.sleep(2)
        # 获取PopularTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_SwitchTab_PopularTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PopularTab
        self.assertEqual(expValue, actValue)

    # 首页-切换到Sing内容Tab
    def test_Case0108_HomePage_SwitchContentTab_SelectSingTab(self):
        Home().HomePage_SwitchTab_SingTab().click()
        time.sleep(2)
        # 获取SingTab的selected属性
        expValue = "true"
        actValue = Home().HomePage_SwitchTab_SingTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到SingTab
        self.assertEqual(expValue, actValue)

    # 首页-点击搜索框
    def test_Case0109_HomePage_Common_ClickSearch(self):
        Home().HomePage_Common_Search().click()
        time.sleep(2)
        # 查找搜索页搜索框
        actValue = Search().SearchPage_Search_SearchBox()
        time.sleep(2)
        # 断言：已跳转到搜索页
        self.assertTrue(actValue)

    # 首页-点击Library
    def test_Case0110_HomePage_Common_ClickLibrary(self):
        Home().HomePage_Common_Library().click()
        time.sleep(2)
        # 获取Sing的selected属性
        expValue = "true"
        actValue = Home().HomePage_MainTab_SingTab().get_attribute("selected")
        time.sleep(2)
        # 断言：已切换到PostTab
        self.assertEqual(expValue, actValue)

    # 首页-点击切换内容语言
    def test_Case0111_HomePage_Common_ClickContentLanguage(self):
        Home().HomePage_Common_ContentLanguage().click()
        time.sleep(2)
        # 获取语言选择弹窗Tips(English)
        expValue = "The content displayed will be based on the language you choose."
        actValue = Home().HomePage_ChooseLanguage_IndiaTips().text
        time.sleep(2)
        # 断言：已调起内容语言弹窗
        self.assertEqual(expValue, actValue)

    # ----------
    # 首页-Hot topics
    # ----------
    # 首页Hot topics正常显示
    def test_Case0112_HomePage_HotTopics_Existence(self):
        # 获取Hot topics的text
        expValue = "Hot topics"
        actValue = Home().HomePage_HotTopics_Text().text
        time.sleep(2)
        # 断言：首页Hot topics正常显示
        self.assertEqual(expValue, actValue)

    # 首页点击Hot topics的See All
    def test_Case0113_HomePage_HotTopics_SeeAll(self):
        Home().HomePage_HotTopics_SeeAll().click()
        time.sleep(2)
        # 获取Hot topics页面的title
        expValue = "Hot Topics"
        actValue = HotTopics().HotTopicsPage_Title_Text().text
        time.sleep(2)
        # 断言：已跳转到Hot Topics页面
        self.assertEqual(expValue, actValue)

    # ----------
    # 首页-卡片（当前页同元素多个时默认操作第一个）
    # ----------
    # 首页卡片-点击头像
    def test_Case0114_HomePage_FeedCard_HeadView(self):
        Home().HomePage_FeedCard_HeadView().click()
        time.sleep(2)
        # 获取该用户的Name
        expValue = Home().HomePage_FeedCard_UserName().text
        actValue = Profile().ProfilePage_UserInfo_StageName().text
        time.sleep(2)
        # 断言：已跳转到该用户Profile页
        self.assertEqual(expValue, actValue)

    # 首页卡片-点击用户名
    def test_Case0115_HomePage_FeedCard_UserName(self):
        Home().HomePage_FeedCard_UserName().click()
        time.sleep(2)
        # 获取该用户的Name
        expValue = Home().HomePage_FeedCard_UserName().text
        actValue = Profile().ProfilePage_UserInfo_StageName().text
        time.sleep(2)
        # 断言：已跳转到该用户Profile页
        self.assertEqual(expValue, actValue)

    # 首页卡片-获取用户名
    def test_Case0116_HomePage_FeedCard_UserName(self):
        UserName = Home().HomePage_FeedCard_UserName().text
        print(UserName)
        time.sleep(2)
        # 将用户名加self以便外部调用
        self.UserName = UserName

    # 首页卡片-Follow成功
    def test_Case0117_HomePage_FeedCard_Follow(self):
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

    # 首页卡片，点击叉号调起dislike对话框
    def test_Case0118_HomePage_FeedCard_Dislike(self):
        Home().HomePage_FeedCard_Dislike().click()
        time.sleep(2)
        # 获取dislike对话框的CancelText
        expValue = "Cancel"
        actValue = Home().HomePage_DislikePop_Cancel().text
        time.sleep(2)
        # 断言：已调起dislike对话框
        self.assertEqual(expValue, actValue)

    # 首页卡片，Unwanted
    def test_Case0119_HomePage_FeedCard_Unwanted(self):
        Home().HomePage_DislikePop_Unwanted().click()
        time.sleep(2)
        # 循环查找toast提示
        expValue = "You will see fewer similar posts."
        actValue = ToastTips_Processing().ToastTips_TextXpath_IsDisplayed(expValue)
        time.sleep(2)
        # 断言：Unwanted成功
        self.assertTrue(actValue)

    # 首页卡片，描述(暂无text文案，待修复)
    def test_Case0120_HomePage_FeedCard_Describe(self):
        Home().HomePage_FeedCard_Describe().click()
        time.sleep(2)
        # 断言待补充

    # 首页卡片，播放图片
    def test_Case0121_HomePage_FeedCard_Img(self):
        Home().HomePage_FeedCard_Img().click()
        time.sleep(2)
        # 查找图片详情页图片预览
        actValue = PlaybackDetails().PlaybackDetailsPage_Img_Preview()
        time.sleep(2)
        # 断言：成功跳转至图片详情页
        self.assertTrue(actValue)

    # 首页卡片，播放视屏
    def test_Case0122_HomePage_FeedCard_Video(self):
        Home().HomePage_FeedCard_Video().click()
        time.sleep(2)
        # 查找视屏详情页视屏预览
        actValue = PlaybackDetails().PlaybackDetailsPage_Video_Preview()
        time.sleep(2)
        # 断言：成功跳转至视屏详情页
        self.assertTrue(actValue)

    # 首页卡片，点击分享按钮
    def test_Case0123_HomePage_FeedCard_Share(self):
        Home().HomePage_FeedCard_Share().click()
        time.sleep(2)
        # 查找分享弹窗分享外框
        actValue = Home().HomePage_SharePop_Frame()
        time.sleep(2)
        # 断言：成功拉起分享弹窗
        self.assertTrue(actValue)

    # 首页卡片，记录分享数
    def test_Case0124_HomePage_FeedCard_ShareCount(self):
        ShareCount = Home().HomePage_FeedCard_ShareCount().text
        print(ShareCount)
        time.sleep(2)
        # 判断统计存在
        actValue = Home().HomePage_FeedCard_ShareCount()
        time.sleep(2)
        # 断言：数据正常
        self.assertTrue(actValue)

    # 首页卡片，点击评论按钮
    def test_Case0125_HomePage_FeedCard_Comment(self):
        Home().HomePage_FeedCard_Comment().click()
        time.sleep(2)
        # 查找评论框
        actValue = PlaybackDetails().PlaybackDetailsPage_Video_Comment()
        time.sleep(2)
        # 断言：成功跳转至详情页评论区域
        self.assertTrue(actValue)

    # 首页卡片，记录评论数
    def test_Case0126_HomePage_FeedCard_CommentCount(self):
        CommentCount = Home().HomePage_FeedCard_CommentCount().text
        print(CommentCount)
        time.sleep(2)
        # 判断统计存在
        actValue = Home().HomePage_FeedCard_CommentCount()
        time.sleep(2)
        # 断言：数据正常
        self.assertTrue(actValue)

    # 首页卡片，点击like按钮
    def test_Case0127_HomePage_FeedCard_Like(self):
        LikeCount1 = Home().HomePage_FeedCard_LikeCount().text
        Home().HomePage_FeedCard_Like().click()
        time.sleep(2)
        LikeCount2 = Home().HomePage_FeedCard_LikeCount().text
        # 判断like成功
        expValue = 1
        actValue = LikeCount2 - LikeCount1
        time.sleep(2)
        # 断言：like成功
        self.assertEqual(expValue, actValue)

    # 首页卡片，记录like数
    def test_Case0128_HomePage_FeedCard_LikeCount(self):
        LikeCount = Home().HomePage_FeedCard_LikeCount().text
        print(LikeCount)
        time.sleep(2)
        # 判断统计存在
        actValue = Home().HomePage_FeedCard_LikeCount()
        time.sleep(2)
        # 断言：数据正常
        self.assertTrue(actValue)

    # 首页卡片，点击下载按钮
    def test_Case0129_HomePage_FeedCard_Download(self):
        Home().HomePage_FeedCard_Video().click()
        time.sleep(2)
        # 循环查找toast提示
        expValue = "Saved to this device."
        actValue = ToastTips_Processing().ToastTips_TextXpath_IsDisplayed(expValue)
        time.sleep(2)
        # 断言：download成功
        self.assertTrue(actValue)

    # 首页卡片，点击WhatsApp按钮
    def test_Case0130_HomePage_FeedCard_WhatsApp(self):
        Home().HomePage_FeedCard_Video().click()
        time.sleep(2)
        # 查找WhatsApp分享框
        actValue = Home().HomePage_WhatsAppPop_Frame()
        time.sleep(2)
        # 断言：成功拉起WhatsApp分享弹窗
        self.assertTrue(actValue)

    # ----------
    # 切换内容语言弹窗-选择内容语言
    # ----------
    # 切换内容语言弹窗-选择内容语言Hindi
    def test_Case0401_ChooseLanguagePop_IndiaSwitchLanguage_Hindi(self):
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

    # 切换内容语言弹窗-选择内容语言Bengali
    def test_Case0402_ChooseLanguagePop_IndiaSwitchLanguage_Bengali(self):
        Language = "हবাংলা(Bengali)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(1).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(1).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Bengali_text=জনপ্রিয়)
        expValue = "জনপ্রিয়"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为孟加拉语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Kannada
    def test_Case0403_ChooseLanguagePop_IndiaSwitchLanguage_Kannada(self):
        Language = "ಕನ್ನಡ(Kannada)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(2).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(2).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Kannada_text=ಜನಪ್ರಿಯ)
        expValue = "ಜನಪ್ರಿಯ"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为卡纳达语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Tamil
    def test_Case0404_ChooseLanguagePop_IndiaSwitchLanguage_Tamil(self):
        Language = "தமிழ்(Tamil)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(3).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(3).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Tamil_text=பிரபலமான)
        expValue = "பிரபலமான"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为泰米尔语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Gujarati
    def test_Case0405_ChooseLanguagePop_IndiaSwitchLanguage_Gujarati(self):
        Language = "ગુજરાતી(Gujarati)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(4).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(4).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Gujarati_text=POPULAR)
        expValue = "POPULAR"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为古吉拉特语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Odia
    def test_Case0406_ChooseLanguagePop_IndiaSwitchLanguage_Odia(self):
        Language = "ଓଡ଼ିଆ(Odia)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(5).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(5).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Odia_text=POPULAR)
        expValue = "POPULAR"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为奥里亚语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Malayalam
    def test_Case0407_ChooseLanguagePop_IndiaSwitchLanguage_Malayalam(self):
        Language = "മലയാളം(Malayalam)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(6).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(6).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Malayalam_text=ജനപ്രിയം)
        expValue = "ജനപ്രിയം"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为马拉雅拉姆语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Marathi
    def test_Case0408_ChooseLanguagePop_IndiaSwitchLanguage_Marathi(self):
        Language = "मराठी(Marathi)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(7).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(7).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Marathi_text=लोकप्रिय)
        expValue = "लोकप्रिय"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为马拉地语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Telugu
    def test_Case0409_ChooseLanguagePop_IndiaSwitchLanguage_Telugu(self):
        Language = "తెలుగు(Telugu)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(8).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(8).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Telugu_text=ప్రముఖ)
        expValue = "ప్రముఖ"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为泰卢固语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Punjabi
    def test_Case0410_ChooseLanguagePop_IndiaSwitchLanguage_Punjabi(self):
        Language = "ਪੰਜਾਬੀ(Punjabi)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(9).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(9).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Punjabi_text=POPULAR)
        expValue = "POPULAR"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为旁遮普语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Assamese
    def test_Case0411_ChooseLanguagePop_IndiaSwitchLanguage_Assamese(self):
        Language = "অসমীয়া(Assamese)"
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(10).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(10).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Assamese_text=POPULAR)
        expValue = "POPULAR"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为阿萨姆语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Haryanvi
    def test_Case0412_ChooseLanguagePop_IndiaSwitchLanguage_Haryanvi(self):
        Language = "हरियाणवी(Haryanvi)"
        # 滑动屏幕
        Screen().SWipeUp_Quarter()
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(-4).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(-4).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Haryanvi_text=POPULAR)
        expValue = "POPULAR"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为哈里亚纳维语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Rajasthani
    def test_Case0413_ChooseLanguagePop_IndiaSwitchLanguage_Rajasthani(self):
        Language = "राजस्थानी(Rajasthani)"
        # 滑动屏幕
        Screen().SWipeUp_Quarter()
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(-3).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(-3).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Rajasthani_text=POPULAR)
        expValue = "POPULAR"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为拉贾斯坦语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言Bhojpuri
    def test_Case0414_ChooseLanguagePop_IndiaSwitchLanguage_Bhojpuri(self):
        Language = "भोजपूरी(Bhojpuri)"
        # 滑动屏幕
        Screen().SWipeUp_Quarter()
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(-2).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(-2).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(Bhojpuri_text=POPULAR)
        expValue = "POPULAR"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为博杰普尔语
        self.assertEqual(expValue, actValue)

    # 切换内容语言弹窗-选择内容语言English
    def test_Case0415_ChooseLanguagePop_IndiaSwitchLanguage_English(self):
        Language = "English(English)"
        # 滑动屏幕
        Screen().SWipeUp_Quarter()
        if Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(-1).text == Language:
            Home().HomePage_ChooseLanguage_IndiaSwitchLanguage(-1).click()
        else:
            Home().HomePage_ChooseLanguage_ByTextSwitchLanguage(Language).click()
        time.sleep(2)
        # 获取首页Popular文案(English_text=POPULAR)
        expValue = "POPULAR"
        actValue = Home().HomePage_SwitchTab_PopularTab().text
        time.sleep(2)
        # 断言：校验首页Popular文案为英语
        self.assertEqual(expValue, actValue)
