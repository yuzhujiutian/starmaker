# coding=utf-8
# ----------
# 启动模块
# ----------
from Utils import Tools
from Utils.FindElement import find_element
from CommonView.VData import StartUp_VD


# 启动模块
class StartUp(object):
    def __init__(self):
        self.findID = find_element().ID

    # 开屏广告
    def OpenAdd_Link(self):
        OpenAdd_Link_ID = self.findID(StartUp_VD.OpenAdd_Link_ID)
        return OpenAdd_Link_ID

    # 开屏广告倒计时
    def OpenAdd_Time_Btn(self):
        OpenAdd_Time_Btn = self.findID(StartUp_VD.OpenAdd_Time_Btn)
        return OpenAdd_Time_Btn

    # Skip 跳过开屏广告
    def Skip_OpenAdd_Btn(self):
        Skip_OpenAdd_Btn_ID = self.findID(StartUp_VD.Skip_OpenAdd_Btn_ID)
        return Skip_OpenAdd_Btn_ID

    # 登录首页Tips（text="sing with 50,000,000+ music lovers"）
    def StartUpHome_Tips(self):
        StartUpHome_Tips_ID = self.findID(StartUp_VD.StartUpHome_Tips_ID)
        return StartUpHome_Tips_ID

    # 登录首页说明（text=You agree to our Terms of Service & Privacy Policy）
    def StartUpHome_Explain(self):
        StartUpHome_Explain_ID = self.findID(StartUp_VD.StartUpHome_Explain_ID)
        return StartUpHome_Explain_ID

    # Email 登录按钮
    def Email_LogIn_Btn(self):
        Email_LogIn_Btn_ID = self.findID(StartUp_VD.Email_LogIn_Btn_ID)
        return Email_LogIn_Btn_ID

    # Email R登录按钮
    @staticmethod
    def Email_LogIn_Btn_R():
        x1 = StartUp_VD.Email_LogIn_Btn_R[0]
        y1 = StartUp_VD.Email_LogIn_Btn_R[1]
        t = StartUp_VD.Email_LogIn_Btn_R[2]
        if Tools.Screen().AccurateClicks_Percentage(x1, y1, t):
            return True
        else:
            return False

    # 登录方式验证——Email 登录
    def LogInModeCase_Email(self):
        if self.findID(StartUp_VD.Email_LogIn_Btn_ID):
            return True
        else:
            return False

    # Phone 登录按钮
    def Phone_LogIn_Btn(self):
        Phone_LogIn_Btn_ID = self.findID(StartUp_VD.Phone_LogIn_Btn_ID)
        return Phone_LogIn_Btn_ID

    # 登录方式验证——Phone 登录
    def LogInModeCase_Phone(self):
        if self.findID(StartUp_VD.Phone_LogIn_Btn_ID):
            return True
        else:
            return False

    # G+ 登录按钮
    def Google_LogIn_Btn(self):
        Google_LogIn_Btn_ID = self.findID(StartUp_VD.Google_LogIn_Btn_ID)
        return Google_LogIn_Btn_ID

    # 登录方式验证——Google 登录
    def LogInModeCase_Google(self):
        if self.findID(StartUp_VD.Google_LogIn_Btn_ID):
            return True
        else:
            return False

    # Facebook 登录按钮
    def FB_LogIn_Btn(self):
        FB_LogIn_Btn_ID = self.findID(StartUp_VD.FB_LogIn_Btn_ID)
        return FB_LogIn_Btn_ID

    # 登录方式验证——Facebook 登录
    def LogInModeCase_Facebook(self):
        if self.findID(StartUp_VD.FB_LogIn_Btn_ID):
            return True
        else:
            return False
