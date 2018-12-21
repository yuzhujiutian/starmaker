# coding=utf-8
import unittest
from Utils.CreateTestReport import CreatTestReporter
Tester = "崔尧椋"


# 登录测试套
class EmailLogInCase(unittest.TestCase):
    @staticmethod
    # 邮箱登录测试套
    def test_Suite_001_EmailLogInCase():
        from Action.StartUpModular import StarUpModular
        from Action.HomeModular import HomeModular
        from Action.LogInModular import LogInModular
        # 定义一个测试套
        EmailLogInCaseSuite = unittest.TestSuite()
        # 添加测试套模版
        EmailLogInCaseSuite.addTest(StarUpModular("test_Case001_ChooseLanguagePage_CheckStartSuccess_Tips"))
        EmailLogInCaseSuite.addTest(StarUpModular("test_Case016_ChooseLanguagePage_SelectLanguage_SelectEnglish"))
        EmailLogInCaseSuite.addTest(HomeModular("test_Case006_HomePage_Tourist_SelectProfileTab"))
        EmailLogInCaseSuite.addTest(LogInModular("test_Case002_LogInPopup_SelectLoginMode_SelectEmail"))
        EmailLogInCaseSuite.addTest(LogInModular("test_Case005_LogInPopup_EmailLoginMode_SelectLogIn"))
        EmailLogInCaseSuite.addTest(LogInModular("test_Case008_EmailLogInPage_InputBox_EmailInput"))
        EmailLogInCaseSuite.addTest(LogInModular("test_Case010_EmailLogInPage_InputBox_PasswordInput"))
        EmailLogInCaseSuite.addTest(LogInModular("test_Case011_EmailLogInPage_LogIn_Confirm"))
        NameFile = "邮箱登录"
        Title = "<邮箱登录—P0>自动化测试用例执行结果"
        Describe = "邮箱登录P0级用例——共8条"
        CreatTestReporter().HTMLReporter(NameFile, Title, Describe, EmailLogInCaseSuite, Tester)


if __name__ == '__main__':
    pass
