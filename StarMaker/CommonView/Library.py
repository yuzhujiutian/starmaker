# coding=utf-8
# ----------
# Library页
# ----------
from StarMaker.Utils.FindElement import find_element
from StarMaker.CommonView.VData import Library_VD


# Library
class Library(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAUS = find_element().AUS

    # Library页搜索框
    def Library_SearchBox(self):
        Library_SearchBox_ID = self.findID(Library_VD.Library_SearchBox_ID)
        return Library_SearchBox_ID

    # 搜索页输入框
    def SearchPage_InputBox(self):
        SearchPage_InputBox_ID = self.findID(Library_VD.SearchPage_InputBox_ID)
        return SearchPage_InputBox_ID

    # Library Tab——HOT
    def LibraryTab_HOT(self):
        LibraryPage_SongInfo_ClaS = self.findClaS(Library_VD.LibraryPage_SongInfo_ClaS, 0)
        return LibraryPage_SongInfo_ClaS

    # 第二首歌曲
    def LibraryPage_SecondSong(self):
        LibraryPage_SongInfo_ClaS = self.findClaS(Library_VD.LibraryPage_SongInfo_ClaS, 9)
        return LibraryPage_SongInfo_ClaS

    # 第二首歌曲——Sing按钮
    def LibraryPage_SecondSong_SingBtn(self):
        LibraryPage_SecondSong_SingBtn_AU = self.findAUS(Library_VD.LibraryPage_SecondSong_SingBtn_AUS, 1)
        return LibraryPage_SecondSong_SingBtn_AU

    # Library页录制模式
    @staticmethod
    def LibraryPage_SongMode():
        LibraryPage_SongMode_ClaS = Library_VD.LibraryPage_SongMode_ClaS
        return LibraryPage_SongMode_ClaS

    # ----------
    # 歌曲详情页
    # ----------

    # 歌名
    def SongInfoPage_SongInfo_SongName(self):
        SongInfoPage_SongInfo_ClaS = self.findClaS(Library_VD.SongInfoPage_SongInfo_ClaS, 0)
        return SongInfoPage_SongInfo_ClaS

    # SING
    def SongInfoPage_SongInfo_SING(self):
        SongInfoPage_SongInfo_ClaS = self.findClaS(Library_VD.SongInfoPage_SongInfo_ClaS, 3)
        return SongInfoPage_SongInfo_ClaS

    # 录制类型——SOLO
    def SongInfoPage_SingType_Solo(self):
        SongInfoPage_Type_ClaS = self.findClaS(Library_VD.SongInfoPage_Type_ClaS, 1)
        return SongInfoPage_Type_ClaS
