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

    # ----------
    # SignUp
    # ----------
    # SignUp页面-预选帐号-Tips
    def SignUpPage_Preselection_Tips(self):
        SignUpPage_Preselection_Tips_ID = self.findID(SignUp_VD.SignUpPage_Preselection_Tips_ID)
        return SignUpPage_Preselection_Tips_ID

    # SignUp页面-Tips-text(text="Enter your email address")
    def SignUpPage_Tips_Text(self):
        SignUpPage_Tips_Text_ID = self.findID(SignUp_VD.SignUpPage_Tips_Text_ID)
        return SignUpPage_Tips_Text_ID
