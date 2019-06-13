# coding=utf-8
# 维护版本：
# 维护日期：
# 维护人员：
# ----------
# StartMaker的Moment模块
# ----------
from StarMaker.CommonView.VData import Moment_VD
from StarMaker.Utils.FindElement import find_element


class Moment(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU

    # ----------
    # 首页-Moment界面
    # ----------
    # Moment界面-Moment[0]
    def MomentPage_Tab_Moment(self):
        MomentPage_Tab_Moment_IDS = self.findIDS(Moment_VD.MomentPage_Tab_Moment_IDS, 0)
        return MomentPage_Tab_Moment_IDS

    # Moment界面下的Popular元素
    def Moment_Tab_MomentPopular(self):
        Moment_Tab_MomentPopular_IDS = self.findIDS(Moment_VD.Moment_Tab_MomentPopular_IDS, 0)
        return Moment_Tab_MomentPopular_IDS

    # Moment界面下的发布
    # ----------------
    # Moment发布
    def Moment_Tab_MomentPublish(self):
        Moment_Tab_MomentPublish_ID = self.findID(Moment_VD.Moment_Tab_MomentPublish_ID)
        return Moment_Tab_MomentPublish_ID

    # Moment发布-sing
    def Moment_Tab_MomentPublish_Sing(self):
        Moment_Tab_MomentPublish_Sing_IDS = self.findIDS(Moment_VD.Moment_Tab_MomentPublish_Sing_IDS, 0)
        return Moment_Tab_MomentPublish_Sing_IDS

    # Moment发布-Album
    def Moment_Tab_MomentPublish_Album(self):
        Moment_Tab_MomentPublish_Album_IDS = self.findIDS(Moment_VD.Moment_Tab_MomentPublish_Sing_IDS, 1)
        return Moment_Tab_MomentPublish_Album_IDS

    # Moment发布-Camera
    def Moment_Tab_MomentPublish_Camera(self):
        Moment_Tab_MomentPublish_Camera_IDS = self.findIDS(Moment_VD.Moment_Tab_MomentPublish_Sing_IDS, 2)
        return Moment_Tab_MomentPublish_Camera_IDS

    # Moment发布-Text
    def Moment_Tab_MomentPublish_Text(self):
        Moment_Tab_MomentPublish_Text_IDS = self.findIDS(Moment_VD.Moment_Tab_MomentPublish_Sing_IDS, 3)
        return Moment_Tab_MomentPublish_Text_IDS

    # Moment发布-发布界面-返回上一页
    def Moment_Function_Post_Back(self):
        Moment_Function_Post_Back_Clas = self.findCla(Moment_VD.Source_Moment_Function_Post_Back_Class)
        return Moment_Function_Post_Back_Clas

    # Post输入内容返回上一页文案
    def Moment_Function_Post_CheckBackElements(self):
        Moment_Function_Post_CheckBackElements_Text = self.findAU("new UiSelector().text(\"Do you want to save the draft?\")")
        return Moment_Function_Post_CheckBackElements_Text

    # Post的返回Discard
    # def Moment_Function_Post_DiscardElement(self):
    #     Moment_Function_Post_DiscardElement_Text = self.findAU("new UiSelector().text(\"Discard\")")
    #     return Moment_Function_Post_DiscardElement_Text

    def Moment_Function_PostDiscardElements(self):
        Moment_Function_Post_DiscardElements_Clas = self.findClaS(Moment_VD.Source_Moment_Function_Post_DiscardElements_ClaS, 0)
        return Moment_Function_Post_DiscardElements_Clas

    # def Moment_Function_PostDiscardElement(self):
    #     Moment_Function_PostDiscardElement_ID = self.findID(Moment_VD.Source_Moment_Function_Post_DiscardElements_IDS)
    #     return Moment_Function_PostDiscardElement_ID

    # Post的返回Save
    def Moment_Function_Post_Savelements(self):
        Moment_Function_Post_Savelements_Clas = self.findClaS(Moment_VD.Source_Moment_Function_Post_DiscardElements_ClaS, 1)
        return Moment_Function_Post_Savelements_Clas

    # Moment界面下的发布的Album
    # ----------------
    # 选择图片页“Album”  JalebeeShootingPage_Function_MusicName
    def Moment_MomentPublish_AlbumPage(self):
        Moment_MomentPublish_AlbumPage_ID = self.findID(Moment_VD.Moment_MomentPublish_AlbumPage_ID)
        return Moment_MomentPublish_AlbumPage_ID

    # 选择图片
    def Moment_MomentPublish_Album_CheckPicture(self):
        Moment_MomentPublish_Album_CheckPicture_IDS = self.findIDS(Moment_VD.Moment_MomentPublish_Album_CheckPicture_IDS, 0)
        return Moment_MomentPublish_Album_CheckPicture_IDS
    def Moment_MomentPublish_Album_CheckPicture1(self):
        Moment_MomentPublish_Album_CheckPicture_IDS = self.findIDS(Moment_VD.Moment_MomentPublish_Album_CheckPicture_IDS, 1)
        return Moment_MomentPublish_Album_CheckPicture_IDS
    def Moment_MomentPublish_Album_CheckPicture2(self):
        Moment_MomentPublish_Album_CheckPicture_IDS = self.findIDS(Moment_VD.Moment_MomentPublish_Album_CheckPicture_IDS, 2)
        return Moment_MomentPublish_Album_CheckPicture_IDS
    def Moment_MomentPublish_Album_CheckPicture3(self):
        Moment_MomentPublish_Album_CheckPicture_IDS = self.findIDS(Moment_VD.Moment_MomentPublish_Album_CheckPicture_IDS, 3)
        return Moment_MomentPublish_Album_CheckPicture_IDS



    # 发布界面的title：Post
    def MomentPublish_Function_Post(self):
        MomentPublish_Function_Post_Text = self.findAU("new UiSelector().text(\"Post\")")
        return MomentPublish_Function_Post_Text

    # send发布
    def MomentPublish_Function_Send(self):
        MomentPublish_Function_Send_ID = self.findID(Moment_VD.MomentPublish_Function_Send_ID)
        return MomentPublish_Function_Send_ID

    # Publish-Album-Next
    def MomentPublish_Function_AlbumNext(self):
        MomentPublish_Function_AlbumNext_ID = self.findID(Moment_VD.MomentPublish_Function_AlbumNext_ID)
        return MomentPublish_Function_AlbumNext_ID

    # Moment-Following 发布作品成功后展示时间
    def MomentFollowing_Function_SendSuc(self):
        MomentPublish_Function_Send_Text = self.findAU("new UiSelector().text(\"1mins ago\")")
        return MomentPublish_Function_Send_Text

    # Moment-Following 发布作品成功后展示文字
    def MomentFollowing_Function_SendSucText(self):
        MomentPublish_Function_SendSucText_ID = self.findID(Moment_VD.MomentPublish_Function_SendSucText_ID)
        return MomentPublish_Function_SendSucText_ID

    # 发布页的元素
    # ---------------------
    # 文案
    def MomentPublish_Function_PublishGuide(self):
        MomentPublish_Function_PublishGuide_Text = self.findAU("new UiSelector().text(\"What's on your mind?\")")
        return MomentPublish_Function_PublishGuide_Text

    # 背景图
    def MomentPublish_Function_CheckBackgroundImage(self):
        MomentPublish_Function_CheckImage_ClaS = self.findClaS(Moment_VD.MomentPublish_Function_CheckImageClaS, 1)
        return MomentPublish_Function_CheckImage_ClaS

    # 背景图-选择第三个彩色图片
    def TextPostPage_Function_BackPicture(self):
        TextPostPage_Function_BackPicture_IDS = self.findIDS(Moment_VD.TextPostPage_Function_BackPicture_IDS, 2)
        return TextPostPage_Function_BackPicture_IDS

    # 背景图-选中彩色图片（输入文案）
    def TextPostPage_Function_CheckBackPicture(self):
        TextPostPage_Function_CheckBackPicture_ID = self.findID(Moment_VD.TextPostPage_Function_CheckBackPicture_ID)
        return TextPostPage_Function_CheckBackPicture_ID


    # 图片标识
    def MomentPublish_Function_CheckImage(self):
        MomentPublish_Function_CheckImage_ClaS = self.findClaS(Moment_VD.MomentPublish_Function_CheckImageClaS, 2)
        return MomentPublish_Function_CheckImage_ClaS

    # "@"符号标识
    def MomentPublish_Function_Checka(self):
        MomentPublish_Function_Checka_ClaS = self.findClaS(Moment_VD.MomentPublish_Function_CheckImageClaS, 3)
        return MomentPublish_Function_Checka_ClaS

    # "#"号标识
    def MomentPublish_Function_CheckJingHao(self):
        MomentPublish_Function_CheckJingHao_ClaS = self.findClaS(Moment_VD.MomentPublish_Function_CheckImageClaS, 4)
        return MomentPublish_Function_CheckJingHao_ClaS

    # 位置图标标识
    def MomentPublish_Function_CheckPosition(self):
        MomentPublish_Function_CheckPosition_ClaS = self.findClaS(Moment_VD.MomentPublish_Function_CheckImageClaS, 5)
        return MomentPublish_Function_CheckPosition_ClaS

    # 文字大小范围标识	0/280
    def MomentPublish_Function_CheckText(self):
        MomentPublish_Function_CheckText_Text = self.findAU("new UiSelector().text(\"0/280\")")
        return MomentPublish_Function_CheckText_Text

    # Moment界面下的发布后的，在Following的加载条
    # ----------------
    # 发布人的头像
    def MomentFollowing_Function_LoadAvatar(self):
        MomentFollowing_Function_LoadAvatar_ID = self.findID(Moment_VD.MomentFollowing_Function_LoadAvatar_ID)
        return MomentFollowing_Function_LoadAvatar_ID

    # 上传中提示
    def MomentFollowing_Function_UploadingAvatar(self):
        MomentFollowing_Function_UploadingAvatar_ID = self.findID(Moment_VD.MomentFollowing_Function_UploadingAvatar_ID)
        return MomentFollowing_Function_UploadingAvatar_ID

    # 进度圈
    def MomentFollowing_Function_ProgressBar(self):
        MomentFollowing_Function_ProgressBar_ID = self.findID(Moment_VD.MomentFollowing_Function_ProgressBar_ID)
        return MomentFollowing_Function_ProgressBar_ID