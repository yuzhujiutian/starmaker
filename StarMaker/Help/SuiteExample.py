#coding=utf-8
import unittest
from StarMaker.Utils.CreateTestReport import CreatTestReporter


class ModelSuite(unittest.TestCase):
    def testmore(self):
        #从某个 Package 导入 XXX 测试类
        from StarMaker.Help import CaseExample
        #定义一个测试套
        XXXSuiteTest = unittest.TestSuite()
        #添加测试套模版
        XXXSuiteTest.addTest(unittest.makeSuite(CaseExample.XXX))
        XXXSuiteTest.addTest(unittest.makeSuite(CaseExample.XXX))
        XXXSuiteTest.addTest(unittest.makeSuite(CaseExample.XXX))
        ...
        NameFile = "LibraryTabCase"
        T = "<首页 Tab 切换>测试用例报告"
        Des = "第一条case，登录后查看My Songs 第一首歌曲"
        CreatTestReporter().HTMLReporter(NameFile, T, Des, XXXSuiteTest)


if __name__ == "__main__":
    unittest.main()
