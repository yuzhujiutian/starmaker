# coding=utf-8
import socket
import time

from StarMaker.CommonView.Development import Development
from StarMaker.CommonView.Home import Home
from StarMaker.CommonView.Library import Library
from StarMaker.CommonView.LogIn import LogIn
from StarMaker.CommonView.Popup import Popup
from StarMaker.CommonView.StartUp import StartUp
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver

driver = GetAppiumDeriver().driver


# Email登录方法
def login_mode(email="cyl@30.cn", pwd="000000"):
    # 选择英语
    StartUp().ChooseLanguagePage_SelectLanguage(1).click()
    time.sleep(5)
    # 处理TVC弹窗
    Popup().HomePopup_TVC_Close_LiveClick()
    time.sleep(2)
    # 点击Me Tab
    Home().HomePage_MainTab_MeTab().click()
    time.sleep(2)
    # 点击登录弹窗的More ways
    LogIn().LogInPopup_SelectLoginMode_MoreWays().click()
    time.sleep(2)
    # 点击登录弹窗的Email方式
    LogIn().LogInPopup_SelectLoginMode_SelectEmail().click()
    time.sleep(2)
    # 输入用户名
    LogIn().EmailLogInPage_EmailInputBox().send_keys(email)
    time.sleep(2)
    # 点击下一步
    LogIn().EmailLogInPage_EmailInputNext().click()
    time.sleep(2)
    # 输入密码
    LogIn().EmailLogInPage_InputBox_PasswordInput().send_keys(pwd)
    time.sleep(2)
    # 点击确认登录
    LogIn().EmailLogInPage_LogIn_Confirm().click()
    time.sleep(2)


# 开启打点测试服务
def start_dotTest_service(IP=socket.gethostbyname(socket.gethostname())):
    # 点击Sing Tab
    Home().HomePage_MainTab_SingTab().click()
    time.sleep(2)
    # 点击搜索入口
    Home().SingPage_Common_Search().click()
    time.sleep(2)
    # 输入"development入口"
    Library().SearchPage_InputBox().send_keys("stmk://developPage")
    time.sleep(2)
    # 输入回车
    driver.keyevent(66)
    time.sleep(2)
    # 勾选测试打点服务器
    Development().DevelopmentPage_CheckBox_DotTestServer().click()
    time.sleep(2)
    # 点击测试打点服务器
    Development().DevelopmentPage_DotTestServer_TextView().click()
    time.sleep(2)
    # 输入测试IP加端口
    Development().DevelopmentPage_DotTestServer_InputBox().send_keys(IP + ":8982")
    time.sleep(2)
    # 点击确定
    Development().DevelopmentPage_DotTestServer_ConfirmButton().click()
    time.sleep(2)
    driver.quit()
    time.sleep(2)
    driver()


if __name__ == '__main__':
    pass
