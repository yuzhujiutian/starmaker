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
        check_log.write(self.exp_dot, T)
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        if check_log.check_dotting():
            print("打点校验全部通过")

    # 展示首页Recommend歌曲
    def test_Case001_ShowLibraryRecommendSongShow(self):
        self.exp_dot = "show,library:Recommend,song_show"

    # 点击首页Recommend歌曲的Sing按钮
    def test_Case002_ClickLibraryRecommendSingButton(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        self.exp_dot = "click,library:Recommend,sing_button"






if __name__ == '__main__':
    pass