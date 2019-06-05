# coding=utf-8
from appium import webdriver

from StarMaker.Utils import Setting
from StarMaker.Utils.Common import singleton
from StarMaker.Utils.GetDevicesInfo import DevicesInfo


@singleton
class GetAppiumDeriver(object):
    # init为只初始化，不返回值
    def __init__(self):
        desired_caps = {}
        # 系统信息
        desired_caps["platformName"] = Setting.PlatformName
        # 待测包信息
        desired_caps["appPackage"] = DevicesInfo().AppPackage()
        desired_caps["appActivity"] = Setting.AppActivity
        # 其他
        desired_caps["unicodeKeyboard"] = Setting.UnicodeKeyboard
        desired_caps["resetKeyboard"] = Setting.ResetKeyboard
        desired_caps["automationName"] = Setting.AutomationName
        desired_caps["autoGrantPermissions"] = Setting.AutoGrantPermissions
        # noReset决定是否清除app数据
        desired_caps["noReset"] = Setting.NoReset
        self.num = Setting.DeviceCount
        IP = Setting.desired_IP
        # 启动服务
        while self.num:
            self.num -= 1
            print(self.num)
            IP += 2
            desired_caps["platformVersion"] = Setting.PlatformVersion[self.num]
            desired_caps["device"] = Setting.Device[self.num]
            desired_caps["deviceName"] = Setting.DeviceName[self.num]
            self.driver = webdriver.Remote("http://127.0.0.1:" + str(IP) + "/wd/hub", desired_caps)


if __name__ == '__main__':
    A = GetAppiumDeriver().driver
