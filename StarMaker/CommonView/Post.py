# coding=utf-8
# 维护版本：
# 维护日期：
# 维护人员：
# ----------
# 点唱流程
# ----------
from StarMaker.CommonView.VData import Post_VD
from StarMaker.Utils import Tools
from StarMaker.Utils.FindElement import find_element


# 发布专辑
class Album(object):
    pass


# 发布图片
class Camera(object):
    pass


# 发布短文
class Text(object):
    pass


# 发布作品
class Sing(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findAU = find_element().AU

    # 插入耳机引导(text=I KNOW)
    # 插入耳机引导(text=I KNOW)
    def HeadphonesRecommended(self):
        from StarMaker.CommonView.VData import Popup_VD
        Popup_HeadphonesRecommended_ID = self.findID(Popup_VD.Popup_HeadphonesRecommended_ID)
        return Popup_HeadphonesRecommended_ID

    # 录制准备页——START
    @staticmethod
    def START_Btn_Coordinate():
        x1 = Post_VD.RecordStart_ID_R[0]
        y1 = Post_VD.RecordStart_ID_R[1]
        t = Post_VD.RecordStart_ID_R[2]
        if Tools.Screen().AccurateClicks_Percentage(x1, y1, t):
            return True
        else:
            return False

    # 录制准备页——START
    def RecordStart(self):
        RecordStart_ID = self.findID(Post_VD.RecordStart_ID)
        return RecordStart_ID

    # 录制页——剩余时间(text=03:36)
    def RecordTime(self):
        RecordTime_ID = self.findID(Post_VD.RecordTime_ID)
        return RecordTime_ID

    # 发布预览页——POST
    def PostBtn(self):
        PostBtn_ID = self.findID(Post_VD.PostBtn_ID)
        return PostBtn_ID

    # 发布编辑页——SEND
    def EditSend(self):
        EditSend_ID = self.findID(Post_VD.EditSend_ID)
        return EditSend_ID

    # 评分页——DONE
    def ScoreDone(self):
        ScoreDone_ID = self.findID(Post_VD.ScoreDone_ID)
        return ScoreDone_ID
