# coding=utf-8
import unittest

from StarMaker.Utils.CreateTestReport import CreatTestReporter


class StarMakerSuite(unittest.TestCase):
    @staticmethod
    def test_Suite():
        Suite = unittest.TestSuite()
        # 添加测试套模版
        from StarMaker.TestCase.LY import StartMakerTestCase
        Suite.addTests(unittest.makeSuite(StartMakerTestCase))
        NameFile = "StarMaker7.4.2"
        T = NameFile + " <自动化回归>测试报告"
        Des = NameFile + "登录回归"
        Tester = "刘悦"
        CreatTestReporter().HTMLReporter(NameFile, T, Des, Suite, Tester)


if __name__ == '__main__':
    unittest.main()
