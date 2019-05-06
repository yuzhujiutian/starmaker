# coding=utf-8
# ----------
# 作品播放详情页模块
# ----------
from StarMaker.Utils.FindElement import find_element
from StarMaker.CommonView.VData import PlaybackDetails_VD
from StarMaker.Utils.Tools import Popular_Elements_Disposes


# KTV模块
class PlaybackDetails(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU
        self.ID_IDS = Popular_Elements_Disposes().ID_IDS

    # ----------
    # 作品播放详情页
    # ----------
    # PlaybackDetails页-播放内容-播放表面
    def PlaybackDetailsPage_PlayContent_Surface(self):
        PlaybackDetailsPage_PlayContent_Surface_ID = self.findID(PlaybackDetails_VD.PlaybackDetailsPage_PlayContent_Surface_ID)
        return PlaybackDetailsPage_PlayContent_Surface_ID

    # PlaybackDetails页-播放内容-暂停
    def PlaybackDetailsPage_PlayContent_Suspend(self):
        PlaybackDetailsPage_PlayContent_Suspend_ID = self.findID(PlaybackDetails_VD.PlaybackDetailsPage_PlayContent_Suspend_ID)
        return PlaybackDetailsPage_PlayContent_Suspend_ID

    # PlaybackDetails页-播放内容-继续
    def PlaybackDetailsPage_PlayContent_Continue_ID(self):
        PlaybackDetailsPage_PlayContent_Continue_ID = self.findID(PlaybackDetails_VD.PlaybackDetailsPage_PlayContent_Continue_ID)
        return PlaybackDetailsPage_PlayContent_Continue_ID

    # PlaybackDetails页-作者信息-头像(ID_IDS)
    def PlaybackDetailsPage_AuthorInfo_HeadView(self):
        PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS = self.ID_IDS(PlaybackDetails_VD.PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS)
        return PlaybackDetailsPage_AuthorInfo_HeadView_ID_IDS

    # PlaybackDetails页-作者信息-用户名
    def PlaybackDetailsPage_AuthorInfo_UserName(self):
        PlaybackDetailsPage_AuthorInfo_UserName_ID = self.findID(PlaybackDetails_VD.PlaybackDetailsPage_AuthorInfo_UserName_ID)
        return PlaybackDetailsPage_AuthorInfo_UserName_ID

    # PlaybackDetails页-作品信息-描述
    def PlaybackDetailsPage_RecordingInfo_Describe(self):
        PlaybackDetailsPage_RecordingInfo_Describe_ID = self.findID(PlaybackDetails_VD.PlaybackDetailsPage_RecordingInfo_Describe_ID)
        return PlaybackDetailsPage_RecordingInfo_Describe_ID

    # PlaybackDetails页-作品信息-统计信息(需提取拆分，原文="173 shares · 333 likes · 2.4K plays · A")
    def PlaybackDetailsPage_RecordingInfo_Statistics(self):
        PlaybackDetailsPage_RecordingInfo_Statistics_ID = self.findID(PlaybackDetails_VD.PlaybackDetailsPage_RecordingInfo_Statistics_ID)
        return PlaybackDetailsPage_RecordingInfo_Statistics_ID

    # ----------
    # 图片/视屏播放详情页
    # ----------
    # PlaybackDetails页-图片详情页-图片预览
    def PlaybackDetailsPage_Img_Preview(self):
        PlaybackDetailsPage_Img_Preview_ID = self.findID(PlaybackDetails_VD.PlaybackDetailsPage_Img_Preview_ID)
        return PlaybackDetailsPage_Img_Preview_ID

    # PlaybackDetails页-视屏详情页-视屏预览
    def PlaybackDetailsPage_Video_Preview(self):
        PlaybackDetailsPage_Video_Preview_ID = self.findID(PlaybackDetails_VD.PlaybackDetailsPage_Video_Preview_ID)
        return PlaybackDetailsPage_Video_Preview_ID

    # PlaybackDetails页-视屏详情页-Repost[0]
    def PlaybackDetailsPage_Video_Repost(self):
        PlaybackDetailsPage_Video_Repost_IDS = self.findIDS(PlaybackDetails_VD.PlaybackDetailsPage_Video_Repost_IDS, 0)
        return PlaybackDetailsPage_Video_Repost_IDS

    # PlaybackDetails页-视屏详情页-Comment[1]
    def PlaybackDetailsPage_Video_Comment(self):
        PlaybackDetailsPage_Video_Comment_IDS = self.findIDS(PlaybackDetails_VD.PlaybackDetailsPage_Video_Comment_IDS)
        return PlaybackDetailsPage_Video_Comment_IDS
