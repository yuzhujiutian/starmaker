# coding=utf-8
# ----------
# Jalebee
# ----------
from Utils.FindElement import find_element
from CommonView.VData import Jalebee_VD
from Utils.Tools import Popular_Elements_Disposes


# Jalebee
class Jalebee(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU
        self.ID_IDS = Popular_Elements_Disposes().ID_IDS
        self.ID_IDS_Count = Popular_Elements_Disposes().ID_IDS_Count

    # ----------
    # Jalebee首页
    # ----------
    # 首页-MainTab-通用(用于校验)
    def JalebeeHomePage_MainTab_Check(self):
        JalebeeHomePage_MainTab_Check_IDS = Jalebee_VD.Jalebee_MainTab_Common_IDS
        return JalebeeHomePage_MainTab_Check_IDS

    # 首页-MainTab-Home
    def JalebeeHomePage_MainTab_Home(self):
        JalebeeHomePage_MainTab_Home_IDS = self.findIDS(Jalebee_VD.Jalebee_MainTab_Common_IDS, 0)
        return JalebeeHomePage_MainTab_Home_IDS

    # 首页-MainTab-Party
    def JalebeeHomePage_MainTab_Party(self):
        JalebeeHomePage_MainTab_Party_IDS = self.findIDS(Jalebee_VD.Jalebee_MainTab_Common_IDS, 1)
        return JalebeeHomePage_MainTab_Party_IDS

    # 首页-MainTab-Message
    def JalebeeHomePage_MainTab_Message(self):
        JalebeeHomePage_MainTab_Message_IDS = self.findIDS(Jalebee_VD.Jalebee_MainTab_Common_IDS, 2)
        return JalebeeHomePage_MainTab_Message_IDS

    # 首页-MainTab-Me
    def JalebeeHomePage_MainTab_Me(self):
        JalebeeHomePage_MainTab_Me_IDS = self.findIDS(Jalebee_VD.Jalebee_MainTab_Common_IDS, 3)
        return JalebeeHomePage_MainTab_Me_IDS

    # 首页-MainTab-Post
    def Jalebee_MainTab_Post(self):
        Jalebee_MainTab_Post_ID = self.findID(Jalebee_VD.Jalebee_MainTab_Post_ID)
        return Jalebee_MainTab_Post_ID

    # Jalebee首页内容Tab(用于校验)
    def JalebeeHomePage_FeedTab_Check(self):
        Jalebee_FeedTab_Common_IDS = Jalebee_VD.Jalebee_FeedTab_Common_IDS
        return Jalebee_FeedTab_Common_IDS

    # Jalebee首页内容Tab-FOLLOWING
    def JalebeeHomePage_FeedTab_FOLLOWING(self):
        Jalebee_FeedTab_Common_IDS = self.findIDS(Jalebee_VD.Jalebee_FeedTab_Common_IDS, 0)
        return Jalebee_FeedTab_Common_IDS

    # Jalebee首页内容Tab-POPULAR
    def JalebeeHomePage_FeedTab_POPULAR(self):
        Jalebee_FeedTab_Common_IDS = self.findIDS(Jalebee_VD.Jalebee_FeedTab_Common_IDS, 1)
        return Jalebee_FeedTab_Common_IDS

    # ----------
    # Jalebee-Party页
    # ----------
    # Jalebee-Party页-Title
    def JalebeePartyPage_Title_Text(self):
        JalebeePartyPage_Title_Text_ID = self.findID(Jalebee_VD.JalebeePartyPage_Title_Text_ID)
        return JalebeePartyPage_Title_Text_ID

    # Jalebee-Party页-MyRoom("मेरा रूम")
    def JalebeePartyPage_MyRoom_Text(self):
        JalebeePartyPage_MyRoom_History_Text_IDS = self.findIDS(Jalebee_VD.JalebeePartyPage_MyRoom_History_Text_IDS, 0)
        return JalebeePartyPage_MyRoom_History_Text_IDS

    # Jalebee-Party页-History("इतिहास")
    def JalebeePartyPage_History_Text(self):
        JalebeePartyPage_MyRoom_History_Text_IDS = self.findIDS(Jalebee_VD.JalebeePartyPage_MyRoom_History_Text_IDS, 1)
        return JalebeePartyPage_MyRoom_History_Text_IDS

    # Jalebee-Party页-首个房间
    def JalebeePartyPage_KTVRoom_FirstRoom(self):
        JalebeePartyPage_MyRoom_History_Text_IDS = self.findIDS(Jalebee_VD.JalebeePartyPage_MyRoom_History_Text_IDS, 2)
        return JalebeePartyPage_MyRoom_History_Text_IDS

    # Jalebee-Party页-第二个房间
    def JalebeePartyPage_KTVRoom_SecondRoom(self):
        JalebeePartyPage_MyRoom_History_Text_IDS = self.findIDS(Jalebee_VD.JalebeePartyPage_MyRoom_History_Text_IDS, 3)
        return JalebeePartyPage_MyRoom_History_Text_IDS

    # Jalebee-Party页-Search
    def Source_JalebeePartyPage_Search_Btn(self):
        Source_JalebeePartyPage_Search_Btn_ID = self.findID(Jalebee_VD.Source_JalebeePartyPage_Search_Btn_ID)
        return Source_JalebeePartyPage_Search_Btn_ID

    # ----------
    # Jalebee-拍摄页
    # ----------
    # Jalebee-拍摄页-选择音乐引导(首次进入时显示，该元素为单独一个页面，遮挡其他元素)
    def JalebeeShotPage_Guide_AddMusic(self):
        JalebeeShotPage_Guide_AddMusic_ID = self.findID(Jalebee_VD.JalebeeShotPage_Guide_AddMusic_ID)
        return JalebeeShotPage_Guide_AddMusic_ID

    # Jalebee-拍摄页-Start按钮
    def JalebeeShotPage_Start_Btn(self):
        JalebeeShotPage_Start_Btn_ID = self.findID(Jalebee_VD.JalebeeShotPage_Start_Btn_ID)
        return JalebeeShotPage_Start_Btn_ID
