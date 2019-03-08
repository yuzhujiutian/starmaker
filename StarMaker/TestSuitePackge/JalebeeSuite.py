# coding=utf-8
import unittest
from Utils.CreateTestReport import CreatTestReporter


class JalebeeSuite(unittest.TestCase):
    @staticmethod
    def test_Suite():
        Suite = unittest.TestSuite()
        # 添加测试套模版
        from TestCase.JalebeeAutoTestCase import JalebeeAutoTestCase
        Suite.addTests(unittest.makeSuite(JalebeeAutoTestCase))
        NameFile = "Jalebee1.3.4"
        T = NameFile + " <自动化回归>测试报告"
        Des = NameFile + " 冒烟回归"
        Tester = "崔尧椋"
        CreatTestReporter().HTMLReporter(NameFile, T, Des, Suite, Tester)


# if __name__ == '__main__':
#     unittest.main()
