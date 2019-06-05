# coding=utf-8
import time
import unittest
import warnings

from StarMaker.CommonView.Home import Home
from StarMaker.CommonView.LogIn import LogIn
from StarMaker.CommonView.Me import Me
from StarMaker.CommonView.Moment import Moment
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver
from StarMaker.Utils.ReadXMLData import ReadXMLData
from StarMaker.Utils.Tools import AssertReportManage
from StarMaker.Utils.Tools import TestData_Processing
from StarMaker.Utils.Tools import Tools

P = AssertReportManage().Pass
E = AssertReportManage().Error


# StarMaker自动化用例
class StartMakerAutoTestCase(unittest.TestCase):
    # StartMaker
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = GetAppiumDeriver().driver
        # 处理上次运行留下的测试数据
        TestData_Processing().TestPicture_Processing()
        time.sleep(8)

    def setUp(self):
        time.sleep(2)

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # 语言选择页校验"Choose Language"
    def test_Case001_ChooseLanguagePage_CheckElement(self):
        '''进入语言选择页，校验是否进入此页面'''
        choose_language_copywriting = LogIn().LogInPopup_Languagedisplay_Copywriting().text
        self.assertTrue(choose_language_copywriting, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "copywriting"))

    # 处理引导
    def test_Case002_Processingguide_English(self):
        '''判断引导是否存在'''
        LogIn().LogInPopup_Chooselanguage_English().click()
        time.sleep(2)
        if LogIn().LogInPopup_Noviceguide():
            guide_ele = LogIn().LogInPopup_Noviceguide().text
            self.assertTrue(guide_ele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "guide"))
        else:
            pass

    def test_Case003_LogIn_Email(self):
        '''选择邮箱登录,判断邮箱登录是否成功'''
        LogIn().LogInPopup_Noviceguide().click()
        LogIn().LogInPopup_SelectbarMe().click()
        time.sleep(2)
        LogIn().LogInPopup_SelectLoginMode_SelectEmail().click()
        time.sleep(2)
        LogIn().LogInPopup_SelectLoginMode_LogIn().click()
        time.sleep(2)
        LogIn().LogInPopup_SelectLoginMode_SendEmail().send_keys(ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "email"))
        LogIn().LogInPopup_SelectLoginMode_SendPw().send_keys(ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "password"))
        LogIn().LogInPopup_EmailLoginMode_LogIn().click()
        time.sleep(2)
        user_name = LogIn().LogInPopup_LogIn_UserName().text
        self.assertTrue(user_name, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "username"))

    # 首页——切换到Me页面
    def test_Case004_HomePage_SwitchMePage(self):
        '''判断是否进入到首页的me界面'''
        LogIn().LogInPopup_SelectbarMe().click()
        time.sleep(2)
        Me_ele = Me().MePage_Tab_Me().text
        print(Me_ele)
        self.assertTrue(Me_ele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "mepage"))

    def test_Case005_SwitchMePage_MeExperience(self):
        '''判断用户个人经验值展示是否正确'''
        Me().MePage_Tab_MeExperience().click()
        time.sleep(2)
        my_level = Me().MyLevel_Tab_MeExperience().text
        self.assertTrue(my_level, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "mylevel"))

    def test_Case006_MePage_VIPIdentification(self):
        '''判断用户个人是非VIP展示'''
        # 点击My Level页的返回按钮
        Me().MeExperience_MyLevel_backButton().click()
        time.sleep(2)
        vip_identification = Me().MyLevel_Tab_VIPIdentification().text
        self.assertTrue(vip_identification, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "nvip"))

    # 首页——切换到Moment页面
    def test_Case007_HomePage_SwitchMomentPage(self):
        '''判断是否进入到首页的Moment界面'''
        Moment().MomentPage_Tab_Moment().click()
        time.sleep(2)
        popular_ele = Moment().Moment_Tab_MomentPopular().text
        self.assertTrue(popular_ele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_popular"))

    # 作品发布展示
    def test_Case008_MomentPage_PublishWork(self):
        '''判断作品四种发布方式'''
        time.sleep(2)
        Moment().Moment_Tab_MomentPublish().click()
        # 获取各个发布方式
        sing_publish = Moment().Moment_Tab_MomentPublish_Sing()
        album_publish = Moment().Moment_Tab_MomentPublish_Album()
        camera_publish = Moment().Moment_Tab_MomentPublish_Camera()
        text_publish = Moment().Moment_Tab_MomentPublish_Text()
        # 断言：
        msg = "四种发布方式"
        self.assertTrue(sing_publish and album_publish and camera_publish and text_publish, E(msg))
        print(P(msg))

    # 进入文本发布界面
    def test_Case009_EnterPublish_CheckSelectPublicPageTitle(self):
        '''判断进入发布（Text）作品界面'''
        Moment().Moment_Tab_MomentPublish_Text().click()
        time.sleep(2)
        post_title = Moment().MomentPublish_Function_Post().text
        self.assertTrue(post_title, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_pulish"))


    # 发布作品（Text）界面元素判断
    def test_Case010_MomentPage_PublishText_CheckElements(self):
        '''发布作品（Text）界面元素判断'''
        # 获取页面元素
        # 界面文案
        copywriting = Moment().MomentPublish_Function_PublishGuide()
        # 背景图
        background_image = Moment().MomentPublish_Function_CheckBackgroundImage()
        # 小图片标识
        picture = Moment().MomentPublish_Function_CheckImage()
        # "@"符号标识
        symbola = Moment().MomentPublish_Function_Checka()
        symbolb = Moment().MomentPublish_Function_CheckJingHao()
        # 位置图标
        position = Moment().MomentPublish_Function_CheckPosition()
        # 输入内容限制
        text1 = Moment().MomentPublish_Function_CheckText()
        # 断言：
        msg = "7种元素核查"
        self.assertTrue(copywriting and background_image and picture and symbola and symbolb and position and text1, E(msg))
        print(P(msg))


    def test_Case011_PublishText_CheckSendElements(self):
        '''判断text发布没有写入内容，send置灰'''
        # 获取发布编辑页send的focused状态
        actValue1 = Moment().MomentPublish_Function_Send().get_attribute("focused")
        expValue1 = "false"
        time.sleep(2)
        # 断言
        msg1 = "Text发布编辑页Send未写入作品不可点击"
        self.assertEqual(expValue1, actValue1, E(msg1))
        print(P(msg1))


    def test_Case012_MomentPage_CheckBackElements(self):
        '''判断丢弃发送Text作品的文案信息'''
        # 输入文本“good day !”
        print("输入文本信息")
        Moment().MomentPublish_Function_PublishGuide().send_keys(
            ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendwork"))
        time.sleep(10)
        print("输入信息完毕")
        # 点击返回按钮
        Moment().Moment_Function_Post_Back().click()
        time.sleep(2)
        discardpublishele = Moment().Moment_Function_Post_CheckBackElements().text
        # 断言
        self.assertTrue(discardpublishele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_public_back"))


    def test_Case013_FailPublishText_DiscardPublishText(self):
        '''丢弃要发布的Text作品'''
        # 点击Discard
        time.sleep(4)
        print("开始点击discard")
        Moment().Moment_Function_PostDiscardElements().click()
        time.sleep(2)
        print("结束点击discard")
        # 断言
        popular_ele = Moment().Moment_Tab_MomentPopular().text
        self.assertTrue(popular_ele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_popular"))

    def test_Case014_FailPublishText_SaveDraftText(self):
        '''保存要发送Text作品到草稿箱'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Text发布
        Moment().Moment_Tab_MomentPublish_Text().click()
        time.sleep(2)
        # 输入文本“good day !”
        Moment().MomentPublish_Function_PublishGuide().send_keys(
            ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendwork"))
        time.sleep(10)
        # 点击返回按钮
        Moment().Moment_Function_Post_Back().click()
        time.sleep(2)
        # 点击Save
        Moment().Moment_Function_Post_Savelements().click()
        # 断言
        popular_ele = Moment().Moment_Tab_MomentPopular().text
        self.assertTrue(popular_ele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_popular"))

    # 发布作品（Text）
    def test_Case015_MomentPage_SucPublishText(self):
        '''发布作品：good day !'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Text发布
        Moment().Moment_Tab_MomentPublish_Text().click()
        time.sleep(2)
        Moment().MomentPublish_Function_PublishGuide().send_keys(ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendwork"))
        time.sleep(6)
        Moment().MomentPublish_Function_Send().click()
        time.sleep(6)
        check_time = Moment().MomentFollowing_Function_SendSuc().text
        self.assertTrue(check_time,
                        ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendsuctime"))

    def test_Case016_MomentPage_CheckAttribute(self):
        '''发布带背景图的作品的元素定位'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Text发布
        Moment().Moment_Tab_MomentPublish_Text().click()
        time.sleep(2)
        # 选择背景图标
        Moment().MomentPublish_Function_CheckBackgroundImage().click()
        time.sleep(2)
        # 选择第三个背景图案
        Moment().TextPostPage_Function_BackPicture().click()
        time.sleep(2)
        # 获取光标位置
        cursoraddr = Moment().TextPostPage_Function_CheckBackPicture().get_attribute("focused")
        time.sleep(2)
        # send是否可点击
        send_ele = Moment().MomentPublish_Function_Send().get_attribute("clickable")
        # 断言
        self.assertTrue(cursoraddr and send_ele, True)

    def test_Case017_MomentPage_SucBackPublish(self):
        '''只存在背景图发送'''
        Moment().MomentPublish_Function_Send().click()
        time.sleep(10)
        check_time = Moment().MomentFollowing_Function_SendSuc().text
        time.sleep(2)
        self.assertTrue(check_time,
                        ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendsuctime"))

    def test_Case018_MomentPage_SucBackPublishInText(self):
        '''背景图里输入good day !'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Text发布
        Moment().Moment_Tab_MomentPublish_Text().click()
        time.sleep(2)
        # 选择背景图
        Moment().MomentPublish_Function_CheckBackgroundImage().click()
        time.sleep(2)
        # 选择背景文案
        Moment().TextPostPage_Function_BackPicture().click()
        time.sleep(2)
        # 在背景图里输入文字
        Moment().TextPostPage_Function_CheckBackPicture().send_keys(ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendwork"))
        time.sleep(6)
        Moment().MomentPublish_Function_Send().click()
        time.sleep(6)
        check_time = Moment().MomentFollowing_Function_SendSuc()
        # 断言
        self.assertTrue(check_time,
                        ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendsuctime"))

    def test_Case019_MomentPage_SucBackPublishInOutText(self):
        '''背景图里输入good day !:good day !'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Text发布
        Moment().Moment_Tab_MomentPublish_Text().click()
        time.sleep(2)
        # 选择背景图
        Moment().MomentPublish_Function_CheckBackgroundImage().click()
        time.sleep(2)
        # 选择背景文案
        Moment().TextPostPage_Function_BackPicture().click()
        time.sleep(2)
        # 在背景图里输入文字
        Moment().TextPostPage_Function_CheckBackPicture().send_keys(ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendwork"))
        time.sleep(6)
        # 点击背景图上方文案
        Moment().MomentPublish_Function_PublishGuide().send_keys(ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendwork"))
        time.sleep(6)
        Moment().MomentPublish_Function_Send().click()
        time.sleep(10)
        check_time = Moment().MomentFollowing_Function_SendSuc()
        desc_ele = Moment().MomentFollowing_Function_SendSucText()
        msg = "存在发布文字"
        # 断言：
        self.assertTrue(desc_ele, E(msg))
        print(P(msg))
        self.assertTrue(check_time,
                        ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendsuctime"))

    def test_Case020_MomentPage_PublicAlbum(self):
        '''判断进入Album的选择图片页'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Album发布
        Moment().Moment_Tab_MomentPublish_Album().click()
        time.sleep(2)
        album_page = Moment().Moment_MomentPublish_AlbumPage().text
        # 断言 进入选择图片页
        self.assertTrue(album_page,
                        ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_pulish_album"))

    def test_Case021_PublicAlbum_CheckSend(self):
        '''判断不选择图片，send是否置灰'''
        # 获取发布编辑页send的focused状态
        actValue1 = Moment().MomentPublish_Function_AlbumNext().get_attribute("focused")
        expValue1 = "false"
        time.sleep(2)
        # 断言
        msg1 = "图片未选择，send置灰"
        self.assertEqual(expValue1, actValue1, E(msg1))
        print(P(msg1))

    def test_Case022_MomentPage_PublishAlbum_CheckElements(self):
        '''发布作品（Album）界面元素判断'''
        # 选择图片
        Moment().Moment_MomentPublish_Album_CheckPicture().click()
        # 选择Next（1）
        time.sleep(2)
        Moment().MomentPublish_Function_AlbumNext().click()
        time.sleep(2)
        # 进入Album发布页，页面元素
        # 界面文案
        copywriting = Moment().MomentPublish_Function_PublishGuide()
        # 小图片标识
        picture = Moment().MomentPublish_Function_CheckImage()
        # "@"符号标识
        symbola = Moment().MomentPublish_Function_Checka()
        symbolb = Moment().MomentPublish_Function_CheckJingHao()
        # 位置图标
        position = Moment().MomentPublish_Function_CheckPosition()
        # 输入内容限制
        text1 = Moment().MomentPublish_Function_CheckText()
        # 断言：
        msg = "7种元素核查"
        self.assertTrue(copywriting and picture and symbola and symbolb and position and text1,
                        E(msg))
        print(P(msg))

    # 发布作品（Album）
    def test_Case023_MomentPage_PublishAlbum(self):
        '''发布Album带文字作品：good Picture !'''
        # 输入文字（图片）
        Moment().MomentPublish_Function_PublishGuide().send_keys(
            ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_pulish_album_send"))
        time.sleep(10)
        # 发送图片带文字作品
        Moment().MomentPublish_Function_Send().click()
        time.sleep(10)
        check_time = Moment().MomentFollowing_Function_SendSuc().text
        self.assertTrue(check_time,
                        ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendsuctime"))

    def test_Case024_MomentPage_PublishAlbum(self):
        '''发布Album图片作品'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Album发布
        Moment().Moment_Tab_MomentPublish_Album().click()
        time.sleep(2)
        # 选择图片
        Moment().Moment_MomentPublish_Album_CheckPicture().click()
        time.sleep(2)
        # 选择Next（1）
        Moment().MomentPublish_Function_AlbumNext().click()
        time.sleep(2)
        # 发送图片作品
        Moment().MomentPublish_Function_Send().click()
        time.sleep(6)
        check_time = Moment().MomentFollowing_Function_SendSuc().text
        self.assertTrue(check_time,
                        ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_sendsuctime"))

    # 看网络加载速度
    def test_Case025_MomentPage_PublishAlbum(self):
        '''9图片数据加载判断'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Album发布
        Moment().Moment_Tab_MomentPublish_Album().click()
        time.sleep(2)
        # 选择图片
        Moment().Moment_MomentPublish_Album_CheckPicture().click()
        Moment().Moment_MomentPublish_Album_CheckPicture1().click()
        Moment().Moment_MomentPublish_Album_CheckPicture2().click()
        Moment().Moment_MomentPublish_Album_CheckPicture3().click()
        time.sleep(2)
        # 选择Next（1）
        Moment().MomentPublish_Function_AlbumNext().click()
        time.sleep(2)
        # 发送图片作品
        Moment().MomentPublish_Function_Send().click()
        time.sleep(1)
        # Moment界面下的发布后的，在Following的加载条
        loadavatar = Moment().MomentFollowing_Function_LoadAvatar()
        uploadingavatar = Moment().MomentFollowing_Function_UploadingAvatar
        progressbar = Moment().MomentFollowing_Function_ProgressBar
        # 断言：
        msg = "3种加载元素核查"
        self.assertTrue(loadavatar and uploadingavatar and progressbar,
                        E(msg))
        print(P(msg))



    def test_Case026_MomentAlbumPage_CheckBackElements(self):
        '''判断丢弃发送Album作品的文案信息'''
        #点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Album发布
        Moment().Moment_Tab_MomentPublish_Album().click()
        time.sleep(2)
        # 选择图片
        Moment().Moment_MomentPublish_Album_CheckPicture().click()
        time.sleep(2)
        # 选择Next（1）
        Moment().MomentPublish_Function_AlbumNext().click()
        time.sleep(2)
        # 点击返回按钮
        Moment().Moment_Function_Post_Back().click()
        time.sleep(2)
        discardalbumele = Moment().Moment_Function_Post_CheckBackElements().text
        # 断言
        self.assertTrue(discardalbumele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_public_back"))


    def test_Case027_FailPublishText_DiscardPublishText(self):
        '''丢弃要发布的Album作品'''
        # 点击Discard
        time.sleep(4)
        print("开始点击discard")
        Moment().Moment_Function_PostDiscardElements().click()
        time.sleep(2)
        print("结束点击discard")
        # 断言   进入的不正确
        popular_ele = Moment().Moment_Tab_MomentPopular().text
        self.assertTrue(popular_ele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_popular"))

    def test_Case028_FailPublishText_SaveDraftText(self):
        '''保存要发送Album作品到草稿箱'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 选择Album发布
        Moment().Moment_Tab_MomentPublish_Album().click()
        time.sleep(2)
        # 选择图片
        Moment().Moment_MomentPublish_Album_CheckPicture().click()
        time.sleep(2)
        # 选择Next（1）
        Moment().MomentPublish_Function_AlbumNext().click()
        time.sleep(2)
        # 点击返回按钮
        Moment().Moment_Function_Post_Back().click()
        time.sleep(2)
        # 点击Save
        Moment().Moment_Function_Post_Savelements().click()
        # 断言
        popular_ele = Moment().Moment_Tab_MomentPopular().text
        self.assertTrue(popular_ele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "moment_popular"))


    def test_Case029_PublishSing_CheckJumpSing(self):
        '''判断是否跳转到Sing页面'''
        # 点击发布按钮
        Moment().Moment_Tab_MomentPublish().click()
        time.sleep(2)
        # 点击Sing发布
        Moment().Moment_Tab_MomentPublish_Sing().click()
        time.sleep(4)
        # 进入Sing，页面元素
        # SIng页-sing
        singele = Home().SingPage_Function_CheckSingTitle().text
        # 断言
        self.assertTrue(singele, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "sing"))

    def test_Case030_PublishSing_CheckSingAttributes(self):
        '''判断sing页面元素属性'''
        # 获取Sing的selected属性
        expValue1 = "true"
        actValue1 = Home().HomePage_MainTab_SingTab().get_attribute("selected")
        # 断言
        self.assertEqual(expValue1, actValue1)

    def test_Case031_PublishSing_CheckSingElement(self):
        '''sing页面元素判断'''
        # Sing页面-搜索框
        singsearch = Home().SingPage_Common_Search()
        # Singy页面-播放器图标
        singplayer = Home().SingPage_Common_Player()
        # Sing页面-Banner
        singbanner = Home().SingPage_Common_Banner()
        # Sing页面-中上方四个Tab([0]Free Style)
        singfreestyle = Home().SingPage_TabName_FreeStyle()
        # Sing页面-中上方四个Tab([1]Collab)
        singcollab = Home().SingPage_TabName_Collab()
        # Sing页面-中上方四个Tab([2]Daily Task)
        singdailycollab = Home().SingPage_TabName_DailyTask()
        # Sing页面-中上方四个Tab([3]My Songs)
        singmysong = Home().SingPage_TabName_MySongs()
        # Sing页面-Take the Mic
        singtakethemic = Home().SingPage_Function_TakeTheMic()
        # Sing页面-Sing Party
        singparty = Home().SingPage_Function_SingParty()
        # Sing页面-中下方四个Tab([0]Recommend)
        singrecomend = Home().SingPage_SingHeat_Recommend()
        # Sing页面-中下方四个Tab([1]Hot)
        singhot = Home().SingPage_SingHeat_Hot()
        # Sing页面-中下方四个Tab([2]Trending)
        singtrending = Home().SingPage_SingHeat_Trending()
        # Sing页面-中下方四个Tab([3]New)
        singnew = Home().SingPage_SingHeat_New()
        # 断言：
        msg = "13种元素核查"
        self.assertTrue(singsearch and singplayer and singbanner and singfreestyle and singcollab
                       and singdailycollab and singmysong and singtakethemic and singparty and singrecomend and singhot
                       and singtrending and singnew,
                       E(msg))
        print(P(msg))

    def test_Case032_FailPublishSing_CheckSingType(self):
        '''判断sing类型'''
        # 选择歌曲的sing
        Home().SingPage_SingRecommend_SelectSing().click()
        # 歌曲类型Tab([0]Solo/[1]Join Collab/[2]Start Collab)
        singsolo = Home().SingPage_SingRecommend_SingType_Solo()
        singjoincollab = Home().SingPage_SingRecommend_SingType_JoinCollab()
        singstartcollab = Home().SingPage_SingRecommend_SingType_StartCollab()
        # 断言
        msg = "3种元素核查"
        self.assertTrue(singsolo and singjoincollab and singstartcollab, E(msg))
        print(P(msg))

    def test_Case033_PublishSing_CheckSingSoloGuide(self):
        '''判断进入到singsolo界面是否有引导'''
        # 选择歌曲类型singsolo
    # -------去掉----------------------------------------------
        Home().SingPage_SingRecommend_SelectSing().click()
        time.sleep(2)
    # --------去掉-------------------------------------------------------
        Home().SingPage_SingRecommend_SingType_Solo().click()
        time.sleep(2)
        # 警告提示
        Home().SingSolo_SafetyWarning_Allow().click()
        time.sleep(2)
        # 引导
        guideidentification = Home().SingSolo_TipsIcon_Check()
        # 引导的“I KNOW”
        guideinfo = Home().SingSolo_TipsIcon_CheckInfo().text
        # 断言
        msg = "1种元素核查"
        self.assertTrue(guideidentification, E(msg))
        print(P(msg))
        self.assertTrue(guideinfo, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "singsolo_guideinfo"))

    def test_Case034_PublishSing_CheckSoloToolGuide(self):
        '''判断是否存在工具的引导提示'''
        # 点击“IKNOW”引导
        Home().SingSolo_TipsIcon_CheckInfo().click()
        time.sleep(2)
        # 获取工具引导
        if Home().SingSolo_Tool_CheckGuide():
            toolguide = Home().SingSolo_Tool_CheckGuide().text
            print("toolguide:", toolguide)
            # 断言
            self.assertTrue(toolguide, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "singsolo_toolguide"))
        else:
            pass

    def test_Case035_PublishSing_CheckSoloPage(self):
        '''判断solo界面的元素'''
        # 如果存在工具引导
        if Home().SingSolo_Tool_CheckGuide():
            Home().SingSolo_Tool_CheckGuide().click()
        else:
            # Sing页面-选择歌曲-Solo-歌曲Pitch
            checkpitch = Home().SingSolo_Function_CheckPitch_ID()
            # Sing页面-选择歌曲-Solo-歌曲Start
            checkstart = Home().SingSolo_Function_ChecStart()
            # Sing页面-选择歌曲-Solo-歌曲Volume
            checkvolum = Home().SingSolo_Function_ChecVolume()
            # Sing页面-选择歌曲-Solo-歌曲Guide
            checkguide = Home().SingSolo_Function_ChecGuide()
            # Sing页面-选择歌曲-Solo-歌曲Effect
            checkeffect = Home().SingSolo_Function_CheckEffect()
            # Sing页面-选择歌曲-Solo-歌曲名称
            singname = Home().SingSolo_Function_SingName()
            # Sing页面-选择歌曲-Solo-音频和视频唱歌
            audiovideo = Home().SingSolo_Function_AudioVideo()
            # Sing页面-选择歌曲-Solo-返回上一页
            backpage = Home().SingSolo_Function_BackPage()
            # 断言
            msg = "8种元素核查"
            self.assertTrue(checkpitch and checkstart and checkvolum and checkguide
                            and checkeffect and singname and audiovideo and backpage, E(msg))
            print(P(msg))
    def test_Case036_PublishSing_CheckSoloStartPage(self):
        '''判断solo界面Start后的元素'''
        # 点击开唱start
        Home().SingSolo_Function_ChecStart().click()
        if Home().SingSolo_SafetyWarning_TextAllow():
            Home().SingSolo_SafetyWarning_TextAllow().click()
            time.sleep(2)
        # Sing页面-选择歌曲-Solo-播放歌曲-歌曲打分
        singrecirdscore = Home().SingSolo_SingRecordScore_CheckElement()
        # Sing页面-选择歌曲-Solo-播放歌曲-歌曲打分头像
        singrecordscoreimage = Home().SingSolo_SingRecordScoreImage_CheckElement()
        # Sing页面-选择歌曲-Solo-播放歌曲-歌曲音准器（上面的抖动条）
        songtone = Home().SingSolo_SongTone_CheckElement()
        # 断言
        msg = "3种元素核查"
        self.assertTrue(singrecirdscore and singrecordscoreimage and songtone, E(msg))
        print(P(msg))

    def test_Case037_PublishSing_CheckSoloPitchPage(self):
        '''判断Pitch的元素'''
        # 点击Pitch
        Home().SingSolo_Function_CheckPitch_ID().click()
        # 打开Pitch界面-pitch
        CheckPitch = Home().SingSolo_Function_CheckPitch_ID()
        # Pitch界面的-Close
        PitchClose = Home().SongTone_PitchPage_PitchClose()
        # Pitch界面的-"-"(低调节)
        PitchLower = Home().SongTone_PitchPage_PitchLower()
        # Pitch界面的-“+”（高调节）
        PitchRaise = Home().SongTone_PitchPage_PitchRaise()
        # Pitch界面的-“----”（调节条）
        PitchProgressBar = Home().SongTone_PitchPage_PitchProgressBar()
        # Pitch界面的-分数（调节分数）
        PitchContent = Home().SongTone_PitchPage_PitchContent()
        # 断言
        msg = "7种元素核查"
        self.assertTrue(CheckPitch and PitchClose and PitchLower and
                        PitchRaise and PitchProgressBar and PitchContent, E(msg))
        print(P(msg))

    def test_Case038_PublishSing_CheckSoloPitchPage(self):
        '''判断Pitch调节数据是否正确'''
        # Pitch界面的-“+”（高调节）
        Home().SongTone_PitchPage_PitchRaise().click()
        time.sleep(2)
        Home().SongTone_PitchPage_PitchRaise().click()
        time.sleep(2)
        Home().SongTone_PitchPage_PitchRaise().click()
        time.sleep(2)
        # Pitch界面的-"-"(低调节)
        Home().SongTone_PitchPage_PitchLower().click()
        time.sleep(2)
        # Pitch界面的-分数（调节分数）
        PitchContent = Home().SongTone_PitchPage_PitchContent().text
        time.sleep(2)
        # 断言
        self.assertTrue(PitchContent, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "singsolo_pitchcontent"))

    def test_Case039_PublishSing_CheckSoloPitchPage(self):
        '''判断Volume的元素'''
        # Pitch界面的-Close
        Home().SongTone_PitchPage_PitchClose().click()
        time.sleep(2)
        # 进入Volume界面
        Home().SingSolo_Function_ChecVolume().click()
        time.sleep(2)
        # Volume界面的-Volume
        volumetitle = Home().SongTone_PitchPage_PitchTitle().text
        time.sleep(2)
        # Volume界面的-Close
        volumeclose = Home().SongTone_PitchPage_PitchClose()
        # Volume界面的-Voice
        volumeadjust = Home().SongTone_VolumePage_VolumeAdjust()
        # Volume界面的-Voice
        nusicadjust = Home().SongTone_VolumePage_MusicAdjust()
        # 断言
        self.assertTrue(volumetitle, ReadXMLData().returnXMLFile("StartMaker.xml", "StartMark", "singsolo_volumetitle"))
        msg = "3种元素核查"
        self.assertTrue(volumeclose and volumeadjust and nusicadjust, E(msg))
        print(P(msg))

    def test_Case040_PublishSing_CheckSoloPitchPage(self):
        '''判断Effect的元素'''
        # volume界面的-Close
        Home().SongTone_PitchPage_PitchClose().click()
        time.sleep(2)
        # 进入Effect界面
        Home().SingSolo_Function_CheckEffect().click()
        time.sleep(2)
        # Effect界面的-Volume
        effecttitle = Home().SongTone_PitchPage_PitchTitle()
        # Effect界面的-Close
        effectclose = Home().SongTone_PitchPage_PitchClose()
        # Effect界面的-Effect的场景效果-NONE
        noneeffect = Home().SongTone_EffectPage_NoneEffect()
        # Effect界面的-Effect的场景效果-CUSTOM
        customeffect = Home().SongTone_EffectPage_CustomEffect()
        # Effect界面的-Effect的场景效果-HALL
        halleffect = Home().SongTone_EffectPage_HallEffect()
        # Effect界面的-Effect的场景效果-PARTY
        partyeffect = Home().SongTone_EffectPage_PartyEffect()
        # 断言
        msg = "6种元素核查"
        self.assertTrue(effecttitle and effectclose and noneeffect and customeffect
                        and halleffect and partyeffect, E(msg))
        print(P(msg))

    def test_Case041_PublishSing_CheckSoloPitchPage(self):
        '''判断Effect的元素'''
        # Effect界面的-Effect的场景效果-CUSTOM
        Home().SongTone_EffectPage_CustomEffect().click()
        # volume界面的-Close
        Home().SongTone_PitchPage_PitchClose().click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()

