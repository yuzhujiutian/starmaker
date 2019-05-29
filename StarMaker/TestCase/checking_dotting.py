# coding=utf-8
import time
import unittest

from StarMaker.CommonView.Home import Home
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver
from StarMaker.Utils.Tools import AssertReportManage
from StarMaker.Utils.Tools import Tools
from analysis_dot.analysis_report_dot.checking_dotting import check_log

P = AssertReportManage().Pass
E = AssertReportManage().Error


# 自动化校验基础打点
class checking_dotting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # >>>初始化app<<<
        cls.driver = GetAppiumDeriver().driver
        time.sleep(8)

    def setUp(self):
        time.sleep(2)

    def tearDown(self):
        # 记录测试数据
        T = check_log.check_time()
        if self.exp_dot:
            check_log.write(self.exp_dot, T)
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        if check_log.check_dotting():
            print("打点校验全部通过")

    # 展示-Recommend-歌曲展示
    def test_Case001_ShowLibraryRecommendSongShow(self):
        self.exp_dot = "show,library:Recommend,song_show"

    # 点击-Recommend-歌曲信息
    def test_Case002_ClickLibraryRecommendSongDetail(self):
        # 点击首页第一首歌曲的歌曲名
        Home().SingPage_CommonTab_FirstSongName().click()
        self.exp_dot = "click,library:Recommend,song_detail"
        time.sleep(2)
        self.driver.back()

    # 点击-Recommend-歌曲的Sing按钮
    def test_Case003_ClickLibraryRecommendSingButton(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        self.exp_dot = "click,library:Recommend,sing_button"

    # 点击-Recommend-点唱类型弹窗的Solo
    def test_Case004_ClickLibraryRecommendSolo(self):
        # 点击点唱类型弹窗的Solo
        Home().SingPage_SingRecommend_SingType_Solo().click()
        self.exp_dot = "click,library:Recommend,solo"
        time.sleep(2)
        self.driver.back()

    # 点击-Recommend-点唱类型弹窗的JoinCollab
    def test_Case005_ClickLibraryRecommendJoinCollab(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的JoinCollab
        Home().SingPage_SingRecommend_SingType_JoinCollab().click()
        self.exp_dot = "click,library:Recommend,join_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-Recommend-点唱类型弹窗的StartCollab
    def test_Case006_ClickLibraryRecommendStartCollab(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的StartCollab
        Home().SingPage_SingRecommend_SingType_StartCollab().click()
        self.exp_dot = "click,library:Recommend,start_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-Recommend-点唱类型弹窗的Chorus
    def test_Case007_ClickLibraryRecommendChorus(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的Chorus
        if Home().SingPage_SingRecommend_SingType_Chorus():
            Home().SingPage_SingRecommend_SingType_Chorus().click()
            self.exp_dot = "click,library:Recommend,hook"
            time.sleep(2)
            self.driver.back()
        else:
            self.exp_dot = ""
            time.sleep(2)
            self.driver.back()
            self.skipTest("歌曲不支持Chorus")

    # 展示-Trending-歌曲展示
    def test_Case008_ShowLibraryTrendingSongShow(self):
        # 点击Trending
        Home().SingPage_SingHeat_Trending().click()
        self.exp_dot = "show,library:Trending,song_show"

    # 点击-Trending-歌曲信息
    def test_Case009_ClickLibraryTrendingSongDetail(self):
        # 点击首页第一首歌曲的歌曲名
        Home().SingPage_CommonTab_FirstSongName().click()
        self.exp_dot = "click,library:Trending,song_detail"
        time.sleep(2)
        self.driver.back()

    # 点击-Trending-歌曲的Sing按钮
    def test_Case010_ClickLibraryTrendingSingButton(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        self.exp_dot = "click,library:Trending,sing_button"

    # 点击-Trending-点唱类型弹窗的Solo
    def test_Case011_ClickLibraryTrendingSolo(self):
        # 点击点唱类型弹窗的Solo
        Home().SingPage_SingRecommend_SingType_Solo().click()
        self.exp_dot = "click,library:Trending,solo"
        time.sleep(2)
        self.driver.back()

    # 点击-Trending-点唱类型弹窗的JoinCollab
    def test_Case012_ClickLibraryTrendingJoinCollab(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的JoinCollab
        Home().SingPage_SingRecommend_SingType_JoinCollab().click()
        self.exp_dot = "click,library:Trending,join_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-Trending-点唱类型弹窗的StartCollab
    def test_Case013_ClickLibraryTrendingStartCollab(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的StartCollab
        Home().SingPage_SingRecommend_SingType_StartCollab().click()
        self.exp_dot = "click,library:Trending,start_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-Trending-点唱类型弹窗的Chorus
    def test_Case014_ClickLibraryTrendingChorus(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的Chorus
        if Home().SingPage_SingRecommend_SingType_Chorus():
            Home().SingPage_SingRecommend_SingType_Chorus().click()
            self.exp_dot = "click,library:Trending,hook"
            time.sleep(2)
            self.driver.back()
        else:
            self.exp_dot = ""
            time.sleep(2)
            self.driver.back()
            self.skipTest("歌曲不支持Chorus")




if __name__ == '__main__':
    pass