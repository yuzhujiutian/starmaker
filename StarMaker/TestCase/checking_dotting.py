# coding=utf-8
from StarMaker.Utils.ReadXMLData import ReadXMLData
from StarMaker.Utils.Tools import AssertReportManage

P = AssertReportManage().Pass
E = AssertReportManage().Error


# 自动化校验基础打点
# class checking_dotting(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         # 忽略警告
#         warnings.simplefilter("ignore", ResourceWarning)
#         # >>>初始化app<<<
#         cls.driver = GetAppiumDeriver().driver
#         time.sleep(8)
#
#     def setUp(self):
#         time.sleep(2)
#
#     def tearDown(self):
#         # 截图
#         Tools().get_images()
#         # 校验打点
#         if check_log.check_dotting(
#                 self.Click_LibraryRecommend_SingButton_key, self.Click_LibraryRecommend_SingButton_Time):
#             print("打点校验成功")
#
#     @classmethod
#     def tearDownClass(cls):
#         pass
#
#     # 启动app
#     def test_Case001_X(self):
#         # 点击首页sing_button
#         Home().SingPage_SingRecommend_SelectSing().click()
#         self.Click_LibraryRecommend_SingButton_key = ReadXMLData().returnXMLFile(
#             "dot_keys.xml", "Sing", "Click_LibraryRecommend_SingButton", path="./")
#         self.Click_LibraryRecommend_SingButton_Time = check_log.check_time()


if __name__ == '__main__':
    path = "../../analysis_dot/analysis_report_dot/checking_dotting/"
    A = ReadXMLData().returnXMLFile(
        "dot_keys.xml", "Sing", "Click_LibraryRecommend_SingButton", path=path)
    B = "1559037699857"
    print(A)


