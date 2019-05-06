# coding=utf-8
from appium import webdriver
from StarMaker.Utils.Common import singleton


@singleton
class GetAppiumDeriver(object):
    # init为只初始化，不返回值
    def __init__(self):
        desired_caps = {}
        desired_caps["platformName"] = "平台"
        desired_caps["platformVersion"] = "系统版本"
        desired_caps["device"] = "型号"
        desired_caps["deviceName"] = "设备名"
        desired_caps["appPackage"] = "com.starmakerinteractive.starmaker"
        desired_caps["appActivity"] = "com.ushowmedia.starmaker.activity.SplashActivity"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 启动设备
driver = GetAppiumDeriver().driver

