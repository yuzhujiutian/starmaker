# coding=utf-8
import unittest
from StarMaker.Utils.CreateTestReport import CreatTestReporter
# from StarMaker.Action.ModeTestCase1 import ModeTestClass1
# from StarMaker.Action.ModeTestCase2 import ModeTestClass2


class ModelSuite(unittest.TestCase):
    # def TestSuite(self):
    #     # 定义一个测试套
    #     ModeTestSuite = unittest.TestSuite()
    #     # 添加测试套模版
    #     ModeTestSuite.addTest(unittest.makeSuite(ModeTestClass1))
    #     ModeTestSuite.addTest(unittest.makeSuite(ModeTestClass2))
    #     NameFile = "测试"
    #     T = "<邮箱登录—P0>测试用例报告"
    #     Des = "Email-LogIn 功能测试"
    #     CreatTestReporter().HTMLReporter(NameFile, T, Des, ModeTestSuite)
    @staticmethod
    def test_Suite():
        Suite = unittest.TestSuite()
        # 添加测试套模版
        from XXX import XXX1
        from XXX import XXX2
        Suite.addTests(unittest.makeSuite(XXX1))
        Suite.addTests(unittest.makeSuite(XXX2))
        NameFile = "测试"
        T = "<邮箱登录—P0>测试用例报告"
        Des = "Email-LogIn 功能测试"
        CreatTestReporter().HTMLReporter(NameFile, T, Des, Suite)


if __name__ == '__main__':
    unittest.main()
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(ModeTestClass1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(ModeTestClass2)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)
