# coding=utf-8
from appium import webdriver
from Utils import Setting
from Utils.Tools import Tools
from Utils.Common import singleton
from Utils.GetDevicesInfo import GetDevicesInfo


@singleton
class GetAppiumDeriver(object):
    # init为只初始化，不返回值
    def __init__(self):
        desired_caps = {}
        # 系统信息
        desired_caps["platformName"] = Setting.PlatformName  # PlatformVersion = "7.0"
        desired_caps["platformVersion"] = GetDevicesInfo().GetAndroidVersion()
        # 设备信息
        desired_caps["device"] = GetDevicesInfo().GetDeviceName()  # DeviceName = "SM_G9200"
        desired_caps["deviceName"] = GetDevicesInfo().GetDevice()  # Device = "zerofltezc"
        # 待测包信息
        desired_caps["appPackage"] = Tools().AppPackage()
        desired_caps["appActivity"] = Setting.AppActivity
        # 其他
        desired_caps["unicodeKeyboard"] = Setting.UnicodeKeyboard
        desired_caps["resetKeyboard"] = Setting.ResetKeyboard
        desired_caps["automationName"] = Setting.AutomationName
        # noReset决定是否清除app数据
        # desired_caps["noReset"] = Setting.NoReset
        self.driver = webdriver.Remote(Setting.desired_IP, desired_caps)




