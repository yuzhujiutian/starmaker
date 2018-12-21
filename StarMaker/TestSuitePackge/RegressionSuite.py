#coding=utf-8
import unittest
from Utils.CreateTestReport import CreatTestReporter
Tester = "崔尧椋"


# 回归测试套
class RegressionSuite(unittest.TestCase):
    # 启动app测试套
    @staticmethod
    def test_Suite_001_StarUpSuite():
        from Action import StartUpModular
        # 定义一个测试套
        StarUpSuiteTest = unittest.TestSuite()
        # 添加测试套模版
        StarUpSuiteTest.addTest(unittest.makeSuite(
            StartUpModular.StarUpCase)
        )
        NameFile = "启动app"
        Title = "<启动app—P0>自动化测试用例执行结果"
        Describe = "启动appP0级用例——共6条"
        CreatTestReporter().HTMLReporter(NameFile, Title, Describe, StarUpSuiteTest, Tester)

    # 邮箱登录测试套
    @staticmethod
    def test_Suite_002_EmailLoginSuite():
        from Action import LogInModular
        EmailLogInSuiteTest = unittest.TestSuite()
        EmailLogInSuiteTest.addTest(unittest.makeSuite(
            LogInModular.EmailLogInCase)
        )
        NameFile = "邮箱登录"
        T = "<邮箱登录—P0>自动化测试用例执行结果"
        Des = "邮箱登录P0级用例——共8条"
        CreatTestReporter().HTMLReporter(NameFile, T, Des, EmailLogInSuiteTest, Tester)

    # Profile页验证测试套
    @staticmethod
    def test_Suite_003_ProfileSuite():
        from TestCase import ProfileCase
        # 定义一个测试套
        ProfileSuiteTest = unittest.TestSuite()
        # 添加测试套模版
        ProfileSuiteTest.addTest(unittest.makeSuite(
            ProfileCase.ProfileCase)
        )
        NameFile = "Profile页"
        Title = "<Profile页—P0+P1>自动化测试用例执行结果"
        Describe = "Profile页P0+P1级用例——共19条"
        CreatTestReporter().HTMLReporter(NameFile, Title, Describe, ProfileSuiteTest, Tester)

    # 录制发布流程验证测试套
    @staticmethod
    def test_Suite_004_PostSoloSuite():
        from TestCase import PostSoloCase
        # 定义一个测试套
        ProfileSuiteTest = unittest.TestSuite()
        # 添加测试套模版
        ProfileSuiteTest.addTest(unittest.makeSuite(
            PostSoloCase.PostSoloCase)
        )
        NameFile = "录制发布"
        Title = "<录制发布—P0>自动化测试用例执行结果"
        Describe = "录制发布P0级用例——共5条"
        CreatTestReporter().HTMLReporter(NameFile, Title, Describe, ProfileSuiteTest, Tester)

# if __name__ == '__main__':
#     unittest.main()
#     LogInSuite = unittest.TestSuite()
#     LogInSuite.addTest(unittest.makeSuite())
