# encoding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Caps:
    def __init__(self):
        self.remoteAddress = 'http://localhost:4723/wd/hub'
        self.platformName = 'Android'
        self.appPackage = 'com.starmakerinteractive.starmaker'
        self.appActivity = 'com.ushowmedia.starmaker.activity.SplashActivity'
        self.appWaitActivity = 'com.ushowmedia.starmaker.activity.MainActivity'
        self.noReset = 'true'

    # 连接设备
    def connect(self):
        desired_caps = {}
        desired_caps['platformName'] = self.platformName
        desired_caps['deviceName'] = 'fe5bb46e'
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity
        desired_caps['appWaitActivity'] = self.appWaitActivity
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['noReset'] = self.noReset
        self.driver = webdriver.Remote(self.remoteAddress, desired_caps)
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']

        actions = TouchAction(self.driver)
        print(dir(actions))
        print(dir(actions.press(x=width/2, y=height/2)))
        actions.move_to(x=width/2, y=height/4)
        actions.perform()
        actions.release()

        return self.driver


caps = Caps()
caps.connect()
