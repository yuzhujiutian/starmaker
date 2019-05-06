# coding=utf-8
import time
import unittest
from StarMaker.CommonView.StartUp import StartUp
from StarMaker.CommonView.Home import Home
from StarMaker.Utils.Tools import Tools
from StarMaker.Utils.Tools import Screen
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver


# 选择语言方法
def SelectLanguage(elements, text):
    if elements.text == text:
        elements.click()
    else:
        Tools().get_images()
        return ValueError


# 启动模块
class StarUpModular(unittest.TestCase):
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

    # 启动APP
    def test_Case0001_ChooseLanguagePage_CheckStartSuccess_Tips(self):
        # 获取语言选择页Tips文案
        expValue = "Choose Language"
        actValue = StartUp().ChooseLanguagePage_CheckStartSuccess_Tips().text
        time.sleep(2)
        # 断言：页面顶部Tips文案是"Choose Language"
        self.assertEqual(expValue, actValue)

    # 选择印地语进入Popular页
    def test_Case0002_ChooseLanguagePage_SelectLanguage_SelectHindi(self):
        # 选择Hindi语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectHindi(),"हिन्दी")
        time.sleep(5)
        # 获取底部SingTab文案(Hindi_text=गाएँ)
        expValue = "गाएँ"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为印地语
        self.assertEqual(expValue, actValue)

    # 选择孟加拉语语进入Popular页
    def test_Case0003_ChooseLanguagePage_SelectLanguage_SelectBengali(self):
        # 选择Bengali语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectBengali(),"বাংলা")
        time.sleep(5)
        # 获取底部SingTab文案(Bengali_text=গান)
        expValue = "গান"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为孟加拉语
        self.assertEqual(expValue, actValue)

    # 选择卡纳达语进入Popular页
    def test_Case0004_ChooseLanguagePage_SelectLanguage_SelectKannada(self):
        # 选择Kannada语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectKannada(),"ಕನ್ನಡ")
        time.sleep(5)
        # 获取底部SingTab文案(Kannada_text=ಹಾಡಿ)
        expValue = "ಹಾಡಿ"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为卡纳达语
        self.assertEqual(expValue, actValue)

    # 选择泰米尔语进入Popular页
    def test_Case0005_ChooseLanguagePage_SelectLanguage_SelectTamil(self):
        # 选择Tamil语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectTamil(),"தமிழ்")
        time.sleep(5)
        # 获取底部SingTab文案(Tamil_text=பாடவும்)
        expValue = "பாடவும்"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为泰米尔语
        self.assertEqual(expValue, actValue)

    # 选择古吉拉特语进入Popular页
    def test_Case0006_ChooseLanguagePage_SelectLanguage_SelectGujarati(self):
        # 选择Gujarati语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectGujarati(),"ગુજરાતી")
        time.sleep(5)
        # 获取底部SingTab文案(Gujarati_text=Sing)
        expValue = "Sing"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为古吉拉特语
        self.assertEqual(expValue, actValue)

    # 选择奥里亚语进入Popular页
    def test_Case0007_ChooseLanguagePage_SelectLanguage_SelectOdia(self):
        # 选择Odia语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectOdia(),"ଓଡ଼ିଆ")
        time.sleep(5)
        # 获取底部SingTab文案(Odia_text=Sing)
        expValue = "Sing"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为奥里亚语
        self.assertEqual(expValue, actValue)

    # 选择马拉雅拉姆语进入Popular页
    def test_Case0008_ChooseLanguagePage_SelectLanguage_SelectMalayalam(self):
        # 选择Malayalam语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectMalayalam(), "മലയാളം")
        time.sleep(5)
        # 获取底部SingTab文案(Malayalam_text=പാടുക)
        expValue = "പാടുക"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为马拉雅拉姆语
        self.assertEqual(expValue, actValue)

    # 选择马拉地语进入Popular页
    def test_Case0009_ChooseLanguagePage_SelectLanguage_SelectMarathi(self):
        # 选择Marathi语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectMarathi(), "मराठी")
        time.sleep(5)
        # 获取底部SingTab文案(Marathi_text=गा)
        expValue = "गा"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为马拉地语
        self.assertEqual(expValue, actValue)

    # 选择泰卢固语进入Popular页
    def test_Case0010_ChooseLanguagePage_SelectLanguage_SelectTelugu(self):
        # 选择Telugu语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectTelugu(), "తెలుగు")
        time.sleep(5)
        # 获取底部SingTab文案(Telugu_text=పాడండి)
        expValue = "పాడండి"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为泰卢固语
        self.assertEqual(expValue, actValue)

    # 选择旁遮普语进入Popular页
    def test_Case0011_ChooseLanguagePage_SelectLanguage_SelectPunjabi(self):
        # 选择Punjabi语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectPunjabi(), "ਪੰਜਾਬੀ")
        time.sleep(5)
        # 获取底部SingTab文案(Punjabi_text=Sing)
        expValue = "Sing"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为旁遮普语
        self.assertEqual(expValue, actValue)

    # 选择阿萨姆语进入Popular页
    def test_Case0012_ChooseLanguagePage_SelectLanguage_SelectAssamese(self):
        # 选择Assamese语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectAssamese(), "অসমীয়া")
        time.sleep(5)
        # 获取底部SingTab文案(Assamese_text=Sing)
        expValue = "Sing"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为阿萨姆语
        self.assertEqual(expValue, actValue)

    # 选择哈里亚纳维语进入Popular页
    def test_Case0013_ChooseLanguagePage_SelectLanguage_SelectHaryanvi(self):
        # 选择Haryanvi语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectHaryanvi(), "हरियाणवी")
        time.sleep(5)
        # 获取底部SingTab文案(Haryanvi_text=Sing)
        expValue = "Sing"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为哈里亚纳维语
        self.assertEqual(expValue, actValue)

    # 选择拉贾斯坦语进入Popular页
    def test_Case0014_ChooseLanguagePage_SelectLanguage_SelectRajasthani(self):
        # 选择Rajasthani语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectRajasthani(), "राजस्थानी")
        time.sleep(5)
        # 获取底部SingTab文案(Rajasthani_text=Sing)
        expValue = "Sing"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为拉贾斯坦语
        self.assertEqual(expValue, actValue)

    # 选择博杰普尔语进入Popular页
    def test_Case0015_ChooseLanguagePage_SelectLanguage_SelectBhojpuri(self):
        # 选择Bhojpuri语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectBhojpuri(), "भोजपूरी")
        time.sleep(5)
        # 获取底部SingTab文案(Bhojpuri_text=Sing)
        expValue = "Sing"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为博杰普尔语
        self.assertEqual(expValue, actValue)

    # 选择英语进入Popular页
    def test_Case0016_ChooseLanguagePage_SelectLanguage_SelectEnglish(self):
        # 向上滑动1/2屏幕
        Screen().SWipeUp_Half()
        time.sleep(2)
        # 选择English语
        SelectLanguage(StartUp().ChooseLanguagePage_SelectLanguage_SelectEnglish(),"English")
        time.sleep(5)
        # 获取底部SingTab文案(English_text=Sing)
        expValue = "Sing"
        actValue = Home().HomePage_MainTabName_Sing().text
        time.sleep(2)
        # 断言：校验底部SingTab文案为英语
        self.assertEqual(expValue, actValue)






