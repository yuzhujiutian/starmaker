# coding=utf-8
# ----------
# 注册模块
# ----------
from CommonView.VData import SignUp_VD
from Utils.FindElement import find_element


# 登录模块
# noinspection PyBroadException
class SignUp(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findXpa = find_element().Xpa

    # SignUp 选择账号以继续（accessibility id=Name）
    def Select_AN(self):
        Select_AN_IDS = self.findIDS(SignUp_VD.Select_AN_IDS, 0)
        return Select_AN_IDS

    # SignUp 以上都不是
    def NoneOfThem_Btn(self):
        NoneOfThem_Btn_ID = self.findID(SignUp_VD.NoneOfThem_Btn_ID)
        return NoneOfThem_Btn_ID

    # SignUp 输入框
    def SignUp_Input_Box(self):
        SignUp_Input_Box_ID = self.findID(SignUp_VD.SignUp_Input_Box_ID)
        return SignUp_Input_Box_ID

    # SignUp 下一步
    def SignUp_Next_Btn(self):
        SignUp_Next_Btn_ID = self.findID(SignUp_VD.SignUp_Next_Btn_ID)
        return SignUp_Next_Btn_ID

    # SignUp 报错信息
    def SignUp_InputEmail_Error(self):
        SignUp_InputEmail_Error_ID = self.findID(SignUp_VD.SignUp_InputEmail_Error_ID)
        return SignUp_InputEmail_Error_ID

    # SignUp 成功 Tips（text:输入邮箱/"Verifying your email address …"/"Sent!"/"Open the email and confirm your email address"）
    def SignUp_Tips(self):
        SignUp_Tips_ID = self.findID(SignUp_VD.SignUp_Tips_ID)
        return SignUp_Tips_ID

    # SignUp Tips
    def SignUpModeCase_Tips(self):
        if self.findID(SignUp_VD.SignUp_Tips_ID):
            return True
        else:
            return False

    # SignUp 打开邮箱
    def SignUp_OpenEmail(self):
        SignUp_OpenEmail_ID = self.findID(SignUp_VD.SignUp_OpenEmail_ID)
        return SignUp_OpenEmail_ID

    # SignUp 重发邮件
    def SignUp_ResendEmail(self):
        SignUp_ResendEmail_ID = self.findID(SignUp_VD.SignUp_ResendEmail_ID)
        return SignUp_ResendEmail_ID

    # Gmail 开启自动同步
    def Gmail_AutoSynchronization(self):
        Gmail_AutoSynchronization_ID = self.findID(SignUp_VD.Gmail_AutoSynchronization_ID)
        return Gmail_AutoSynchronization_ID

    # Gmail 选择会话
    def Gmail_SelectSession(self):
        Gmail_SelectSession_IDS = self.findIDS(SignUp_VD.Gmail_SelectSession_IDS, 0)
        return Gmail_SelectSession_IDS

    # Gmail 登录邮件——继续
    def Gmail_Confirm(self):
        Gmail_Confirm_Xpath = self.findXpa(SignUp_VD.Gmail_Confirm_Xpath)
        return Gmail_Confirm_Xpath

    # Gmail 登录邮件——Tips（message:"登录失败。"/"登录 Music App"/"你已登录"）
    def Gmail_ConfirmTips(self):
        Gmail_ConfirmTips_Xpath = self.findXpa(SignUp_VD.Gmail_ConfirmTips_Xpath)
        return Gmail_ConfirmTips_Xpath

    # Gmail 登录邮件——登录/打开应用
    def Gmail_LogIn(self):
        Gmail_LogIn_Xpath = self.findXpa(SignUp_VD.Gmail_LogIn_Xpath)
        return Gmail_LogIn_Xpath
