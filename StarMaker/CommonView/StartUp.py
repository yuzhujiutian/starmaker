# coding=utf-8
# ----------
# 启动模块
# ----------
from Utils import Tools
from Utils.FindElement import find_element
from CommonView.VData import StartUp_VD
from CommonView.VData import LogIn_VD


# 启动模块
class StartUp(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findAU = find_element().AU
        self.findClaS = find_element().ClaS
        self.DIYSwipe_Percentage = Tools.Screen().DIYSwipe_Percentage

    # 语言选择页-ClaS(用于校验)
    def ChooseLanguagePage_Check(self):
        ChooseLanguagePage_Check_ClaS = StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS
        return ChooseLanguagePage_Check_ClaS

    # 语言选择页-校验启动成功-顶部Tips文案([0]text=Choose Language)
    def ChooseLanguagePage_CheckStartSuccess_Tips(self):
        ChooseLanguagePage_CheckStartSuccess_Tips_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_CheckStartSuccess_Tips_ClaS, 0)
        return ChooseLanguagePage_CheckStartSuccess_Tips_ClaS

    # 语言选择页-选择语言-选择印地语([1]text=हिन्दी)
    def ChooseLanguagePage_SelectLanguage_SelectHindi(self):
        ChooseLanguagePage_SelectLanguage_SelectHindi_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 1)
        return ChooseLanguagePage_SelectLanguage_SelectHindi_ClaS

    # 语言选择页-选择语言-选择孟加拉语([2]text=বাংলা)
    def ChooseLanguagePage_SelectLanguage_SelectBengali(self):
        ChooseLanguagePage_SelectLanguage_SelectBengali_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 2)
        return ChooseLanguagePage_SelectLanguage_SelectBengali_ClaS

    # 语言选择页-选择语言-选择卡纳达语([3]text=ಕನ್ನಡ)
    def ChooseLanguagePage_SelectLanguage_SelectKannada(self):
        ChooseLanguagePage_SelectLanguage_SelectKannada_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 3)
        return ChooseLanguagePage_SelectLanguage_SelectKannada_ClaS

    # 语言选择页-选择语言-选择泰米尔语([4]text=தமிழ்)
    def ChooseLanguagePage_SelectLanguage_SelectTamil(self):
        ChooseLanguagePage_SelectLanguage_SelectTamil_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 4)
        return ChooseLanguagePage_SelectLanguage_SelectTamil_ClaS

    # 语言选择页-选择语言-选择古吉拉特语([5]text=ગુજરાતી)
    def ChooseLanguagePage_SelectLanguage_SelectGujarati(self):
        ChooseLanguagePage_SelectLanguage_SelectGujarati_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 5)
        return ChooseLanguagePage_SelectLanguage_SelectGujarati_ClaS

    # 语言选择页-选择语言-选择奥里亚语([6]text=ଓଡ଼ିଆ)
    def ChooseLanguagePage_SelectLanguage_SelectOdia(self):
        ChooseLanguagePage_SelectLanguage_SelectOdia_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 6)
        return ChooseLanguagePage_SelectLanguage_SelectOdia_ClaS

    # 语言选择页-选择语言-选择马拉雅拉姆语([7]text=മലയാളം)
    def ChooseLanguagePage_SelectLanguage_SelectMalayalam(self):
        ChooseLanguagePage_SelectLanguage_SelectMalayalam_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 7)
        return ChooseLanguagePage_SelectLanguage_SelectMalayalam_ClaS

    # 语言选择页-选择语言-选择马拉地语([8]text=मराठी)
    def ChooseLanguagePage_SelectLanguage_SelectMarathi(self):
        ChooseLanguagePage_SelectLanguage_SelectMarathi_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 8)
        return ChooseLanguagePage_SelectLanguage_SelectMarathi_ClaS

    # 语言选择页-选择语言-选择泰卢固语([9]text=తెలుగు)
    def ChooseLanguagePage_SelectLanguage_SelectTelugu(self):
        ChooseLanguagePage_SelectLanguage_SelectTelugu_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 9)
        return ChooseLanguagePage_SelectLanguage_SelectTelugu_ClaS

    # 语言选择页-选择语言-选择旁遮普语([10]text=ਪੰਜਾਬੀ)
    def ChooseLanguagePage_SelectLanguage_SelectPunjabi(self):
        ChooseLanguagePage_SelectLanguage_SelectPunjabi_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 10)
        return ChooseLanguagePage_SelectLanguage_SelectPunjabi_ClaS

    # 语言选择页-选择语言-选择阿萨姆语([11]text=অসমীয়া)
    def ChooseLanguagePage_SelectLanguage_SelectAssamese(self):
        ChooseLanguagePage_SelectLanguage_SelectAssamese_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 11)
        return ChooseLanguagePage_SelectLanguage_SelectAssamese_ClaS

    # 语言选择页-选择语言-选择哈里亚纳维语([12]text=हरियाणवी)
    def ChooseLanguagePage_SelectLanguage_SelectHaryanvi(self):
        ChooseLanguagePage_SelectLanguage_SelectHaryanvi_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 12)
        return ChooseLanguagePage_SelectLanguage_SelectHaryanvi_ClaS

    # 语言选择页-选择语言-选择拉贾斯坦语([13]text=राजस्थानी)
    def ChooseLanguagePage_SelectLanguage_SelectRajasthani(self):
        ChooseLanguagePage_SelectLanguage_SelectRajasthani_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 13)
        return ChooseLanguagePage_SelectLanguage_SelectRajasthani_ClaS

    # 语言选择页-选择语言-选择博杰普尔语([14]text=भोजपूरी)
    def ChooseLanguagePage_SelectLanguage_SelectBhojpuri(self):
        ChooseLanguagePage_SelectLanguage_SelectBhojpuri_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS, 14)
        return ChooseLanguagePage_SelectLanguage_SelectBhojpuri_ClaS

    # 语言选择页-选择语言-选择英语([-1]text=English)
    def ChooseLanguagePage_SelectLanguage_SelectEnglish(self):
        ChooseLanguagePage_SelectLanguage_SelectEnglish_ClaS = self.findClaS(StartUp_VD.ChooseLanguagePage_SelectLanguage_Common_ClaS,-1)
        return ChooseLanguagePage_SelectLanguage_SelectEnglish_ClaS
