# coding=utf-8
import re
import time
import unittest
from CommonView.StartUp import StartUp
from CommonView.LogIn import LogIn
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver


# 手机号登录
class PhoneLogInCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # 成功跳转至Phone登录页
    def test_Case001_PhoneLogInHomeCase(self):
        # 点击Phone登录按钮
        StartUp().Phone_LogIn_Btn().click()
        time.sleep(1)
        expValue = "输入手机号"
        # 获取Phone登录页Tips
        actValue = LogIn().PhoneHome_Tips().text
        # 判断跳转成功
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # PhoneHome 描述正确
    def test_Case002_PhoneHomeDescribeCase(self):
        expValue = "轻触下一步通过 Account Kit powered by Facebook 验证你的帐户。即使没有 Facebook 帐户，你也可以使用 Account Kit。你可通过手机短信接收手机号验证码。此过程可能产生短信和流量资费。详细了解 Facebook 如何使用你的信息。"
        # 获取Phone登录页Tips
        actValue = LogIn().PhoneHome_Describe().text
        # 判断描述正确
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 进入PhoneLogInHome时光标聚焦输入框
    def test_Case003_PhoneInput_CursorFocusedCase(self):
        expValue = "true"
        # 获取输入框focused状态
        actValue = LogIn().Phone_input().get_attribute("focused")
        # 判断光标聚焦
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 输入框内默认填入国家区号
    def test_Case004_DefaultAreaCode(self):
        expValue = "+86 "
        # 获取输入框内容
        actValue = LogIn().Phone_input().text
        # 判断是否默认填入国家区号
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # "下一步"按钮置灰不可点击
    def test_Case005_Empty_NextEnabledCase(self):
        expValue = "false"
        # 获取"下一步"按钮enabled状态
        actValue = LogIn().Phone_Next().get_attribute("enabled")
        # 判断"下一步"按钮置灰不可点击
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 输入符合规则手机号，"下一步"按钮取消置灰可点击
    def test_Case006_Normal_NextEnabledCase(self):
        # 输入符合规则手机号(176 0017 5705)
        self.driver.keyevent(8)
        time.sleep(1)
        self.driver.keyevent(14)
        time.sleep(1)
        self.driver.keyevent(13)
        time.sleep(1)
        self.driver.keyevent(7)
        time.sleep(1)
        self.driver.keyevent(7)
        time.sleep(1)
        self.driver.keyevent(8)
        time.sleep(1)
        self.driver.keyevent(14)
        time.sleep(1)
        self.driver.keyevent(12)
        time.sleep(1)
        self.driver.keyevent(14)
        time.sleep(1)
        self.driver.keyevent(7)
        time.sleep(1)
        self.driver.keyevent(12)
        time.sleep(1)
        expValue = "true"
        # 获取"下一步"按钮enabled状态
        actValue = LogIn().Phone_Next().get_attribute("enabled")
        # 判断"下一步"按钮取消置灰可点击
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 点击国旗，拉起切换国家区号弹窗
    def test_Case007_PullUp_SwitchWindowCase(self):
        # 点击当前国旗
        LogIn().Phone_NowCountryCode().click()
        time.sleep(1)
        expValue = "中国 (+86)"
        # 获取弹窗内最后一个国家区号
        actValue = LogIn().Phone_SwitchCountryCode_CN().text
        # 判断是否成功拉起切换国家区号弹窗
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 选择国家，弹窗收起，清空输入框内手机号，输入框内只显示对应区号
    def test_Case008_SelectAreaCodeCase(self):
        # 选择英国 (+44)
        LogIn().Phone_SwitchCountryCode_GB().click()
        time.sleep(1)
        expValue = "+44 "
        # 获取输入框内容
        actValue = LogIn().Phone_input().text
        # 判断输入框内自动填入"+44"
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 输入框前展示对应国旗
    def test_Case009_SwitchNationalFlagCase(self):
        expValue = "🇬🇧"
        # 获取输入框前国旗
        actValue = LogIn().Phone_NowCountryCode().text
        # 判断输入框展示对应国旗
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 输入符合规则手机号——跳转验证码输入页
    def test_Case010_InputNumber_JumpValidationPageCase(self):
        # 点击当前国旗
        LogIn().Phone_NowCountryCode().click()
        time.sleep(1)
        # 选择中国
        LogIn().Phone_SwitchCountryCode_CN().click()
        time.sleep(1)
        # 输入符合规则手机号(176 0017 5705)——可优化为自动获取本机号码
        self.driver.keyevent(8)
        time.sleep(1)
        self.driver.keyevent(14)
        time.sleep(1)
        self.driver.keyevent(13)
        time.sleep(1)
        self.driver.keyevent(7)
        time.sleep(1)
        self.driver.keyevent(7)
        time.sleep(1)
        self.driver.keyevent(8)
        time.sleep(1)
        self.driver.keyevent(14)
        time.sleep(1)
        self.driver.keyevent(12)
        time.sleep(1)
        self.driver.keyevent(14)
        time.sleep(1)
        self.driver.keyevent(7)
        time.sleep(1)
        self.driver.keyevent(12)
        time.sleep(1)
        # 点击"下一步"按钮
        LogIn().Phone_Next().click()
        time.sleep(10)
        expValue = "请输入发送到+8617600175705的验证码"
        # 获取验证页Tips
        actValue = LogIn().PhoneHome_Tips().text
        # 判断跳转验证码输入页成功
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 非P0级
    # # 输入验证码以登录成功
    # def test_Case0XX_InputCode_SuccessfulLoginCase(self):
    #     # 滑动打开通知栏
    #     Tools().SwipeOpen_NoticeBoard()
    #     # 获取短信内容——可优化为在此页面监听短信
    #     time.sleep(1)
    #     message = LogIn().Code().text
    #     # 提取验证码
    #     code = re.sub("\D", "", message)
    #     r_code = []
    #     for i in code:
    #         r_code.append(int(i) + 7)
    #     print(r_code)
    #     # 滑动收起通知栏
    #     Tools().SwipeClose_NoticeBoard()
    #     # 输入获取的验证码
    #     time.sleep(1)
    #     self.driver.keyevent(r_code[0])
    #     self.driver.keyevent(r_code[1])
    #     self.driver.keyevent(r_code[2])
    #     self.driver.keyevent(r_code[3])
    #     self.driver.keyevent(r_code[4])
    #     self.driver.keyevent(r_code[5])
    #     time.sleep(5)
    #     # 点击登录
    #     LogIn().Phone_Next().click()
    #     time.sleep(5)

    # 进入验证码验证页时光标聚焦输入框
    def test_Case011_CodeInput_CursorFocusedCase(self):
        expValue = "true"
        # 获取验证码输入框focused状态
        actValue = LogIn().Code_FirstInputBox().get_attribute("focused")
        # 判断光标聚焦
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # "继续"按钮置灰不可点击
    def test_Case012_Empty_ContinueEnabledCase(self):
        expValue = "false"
        # 获取"下一步"按钮enabled状态
        actValue = LogIn().Phone_Next().get_attribute("enabled")
        # 判断"下一步"按钮置灰不可点击
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 输入符合规则验证码，"继续"按钮取消置灰可点击
    def test_Case013_Normal_ContinueEnabledCase(self):
        # 输入错误验证码(123456)
        self.driver.keyevent(8)
        time.sleep(1)
        self.driver.keyevent(9)
        time.sleep(1)
        self.driver.keyevent(10)
        time.sleep(1)
        self.driver.keyevent(11)
        time.sleep(1)
        self.driver.keyevent(12)
        time.sleep(1)
        self.driver.keyevent(13)
        time.sleep(1)
        expValue = "true"
        # 获取"继续"按钮enabled状态
        actValue = LogIn().Phone_Next().get_attribute("enabled")
        # 判断"继续"按钮取消置灰可点击
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 点击继续，验证失败时跳转至验证码重发页
    def test_Case014_VerificationFailureCase(self):
        # 点击继续
        LogIn().Phone_Next().click()
        time.sleep(5)
        expValue = "无法验证你的代码，请重试：\n+8617600175705"
        # 获取 Tips 提示
        actValue = LogIn().PhoneHome_Tips().text
        # 判断验证失败时跳转至验证码重发页
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 点击未收到验证码，正常跳转至验证码重发页
    def test_Case015_NotReceivedCodeCase(self):
        # 点击未收到验证码
        LogIn().Not_Received_Code().click()
        time.sleep(1)
        expValue = "如果你还未收到验证码："
        # 获取 Tips 提示
        actValue = LogIn().PhoneHome_Tips().text
        # 判断正常跳转至验证码重发页
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 验证码重发页显示之前输入的区号+手机号：{AreaCode}{PhoneNumber}
    def test_Case016_VerifyYourNumberCase(self):
        expValue = "验证你的手机号：+8617600175705"
        # 获取验证你的手机号：{AreaCode}{PhoneNumber}
        actValue = LogIn().Verify_Your_Number().text
        # 判断正常显示之前输入的区号+手机号：{AreaCode}{PhoneNumber}
        time.sleep(1)
        self.assertEqual(expValue, actValue)

    # 点击重发短信，跳转至输入手机号，自动填充之前输入的区号+手机号：{AreaCode}{PhoneNumber}
    def test_Case017_RecaptureCodeCase(self):
        # 判断还有多久可以重发短信
        message = LogIn().Recapture_Code().text
        # 提取时间
        time_a = re.sub("\D", "", message)
        print(time_a)
        # 如果不可点击，则等待xx秒后再点击
        if time_a != "":
            time.sleep(int(time_a) + 1)
            # 点击重发短信
            LogIn().Recapture_Code().click()
        else:
            # 点击重发短信
            LogIn().Recapture_Code().click()
        time.sleep(1)
        expValue = "+86 176 0017 5705"
        # 获取输入框内容
        actValue = LogIn().Phone_input().text
        # 判断输入框内自动填入区号+手机号
        time.sleep(1)
        self.assertEqual(expValue, actValue)
        self.driver.back()


if __name__ == '__main__':
    pass
