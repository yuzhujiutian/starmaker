# coding=utf-8
# 维护版本：
# 维护日期：
# 维护人员：
# ----------
# Development页
# ----------
from StarMaker.CommonView.VData import Development_VD
from StarMaker.Utils.FindElement import find_element


# Development页
class Development(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU

    # Development-勾选框-测试打点服务器
    def DevelopmentPage_CheckBox_DotTestServer(self):
        DevelopmentPage_CheckBox_IDS = self.findIDS(Development_VD.DevelopmentPage_CheckBox_IDS, 3)
        return DevelopmentPage_CheckBox_IDS

    # Development-测试打点服务器-文本(可点击)
    def DevelopmentPage_DotTestServer_TextView(self):
        DevelopmentPage_DotTestServer_TextView_Text = self.findAU("new UiSelector().text(\"测试打点服务器\")")
        return DevelopmentPage_DotTestServer_TextView_Text

    # Development-打点服务器弹窗-输入框
    def DevelopmentPage_DotTestServer_InputBox(self):
        DevelopmentPage_DotTestServer_InputBox_ID = self.findID(Development_VD.DevelopmentPage_DotTestServer_InputBox_ID)
        return DevelopmentPage_DotTestServer_InputBox_ID

    # Development-打点服务器弹窗-确认按钮
    def DevelopmentPage_DotTestServer_ConfirmButton(self):
        DevelopmentPage_DotTestServer_ConfirmButton_ID = self.findID(Development_VD.DevelopmentPage_DotTestServer_ConfirmButton_ID)
        return DevelopmentPage_DotTestServer_ConfirmButton_ID
