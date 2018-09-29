#coding=utf-8
import unittest
from Utils.CreateTestReport import CreatTestReporter
Tester = "崔尧椋"


# 登录测试套
class LogInSuite(unittest.TestCase):
    # 启动app测试套
    @staticmethod
    def test_Suite_001_StarUpSuite():
        from TestCase import StartUpCase
        # 定义一个测试套
        StarUpSuiteTest = unittest.TestSuite()
        # 添加测试套模版
        StarUpSuiteTest.addTest(unittest.makeSuite(
            StartUpCase.StarUpCase)
        )
        NameFile = "启动app"
        Title = "<启动app—P0>自动化测试用例执行结果"
        Describe = "启动appP0级用例——共6条"
        CreatTestReporter().HTMLReporter(NameFile, Title, Describe, StarUpSuiteTest, Tester)

    # 手机号登录测试套
    @staticmethod
    def test_Suite_002_PhoneLoginSuite():
        from TestCase import PhoneLogInCase
        PhoneLoginSuiteTest = unittest.TestSuite()
        PhoneLoginSuiteTest.addTest(unittest.makeSuite(
            PhoneLogInCase.PhoneLogInCase)
        )
        NameFile = "手机号登录"
        T = "<手机号登录—P0>自动化测试用例执行结果"
        Des = "手机号登录P0级用例——共17条"
        CreatTestReporter().HTMLReporter(NameFile, T, Des, PhoneLoginSuiteTest, Tester)

    # 邮箱登录测试套
    @staticmethod
    def test_Suite_003_EmailLoginSuite():
        from TestCase import EmailLogInCase
        EmailLogInSuiteTest = unittest.TestSuite()
        EmailLogInSuiteTest.addTest(unittest.makeSuite(
            EmailLogInCase.EmailLogInCase)
        )
        NameFile = "邮箱登录"
        T = "<邮箱登录—P0>自动化测试用例执行结果"
        Des = "邮箱登录P0级用例——共8条"
        CreatTestReporter().HTMLReporter(NameFile, T, Des, EmailLogInSuiteTest, Tester)

    # Profile页验证测试套
    @staticmethod
    def test_Suite_004_ProfileSuite():
        from TestCase import ProfileCase
        # 定义一个测试套
        ProfileSuiteTest = unittest.TestSuite()
        # 添加测试套模版
        ProfileSuiteTest.addTest(unittest.makeSuite(
            ProfileCase.ProfileCase)
        )
        NameFile = "Profile页"
        Title = "<Profile页—P1>自动化测试用例执行结果"
        Describe = "Profile页P1级用例——共19条"
        CreatTestReporter().HTMLReporter(NameFile, Title, Describe, ProfileSuiteTest, Tester)

# if __name__ == '__main__':
#     unittest.main()
#     LogInSuite = unittest.TestSuite()
#     LogInSuite.addTest(unittest.makeSuite())
