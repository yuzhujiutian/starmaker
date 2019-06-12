#encoding=utf-8

import unittest
import time
import random

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.appPackage = 'com.starmakerinteractive.starmaker'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'fe5bb46e'
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = 'com.ushowmedia.starmaker.activity.SplashActivity'
        desired_caps['appWaitActivity'] = 'com.ushowmedia.starmaker.activity.MainActivity'
        # desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['noReset'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait15 = WebDriverWait(self.driver, 15, 1)
        self.wait5 = WebDriverWait(self.driver, 10, 1)

    def tearDown(self):
        pass

    def findElementById(self, elementId):
        element = None
        try:
            element = self.wait5.until(lambda driver: driver.find_element_by_id(elementId))
        except Exception as e:
            print e
        
        return element

    def findElementsByAID(self, elementId):
        elements = None
        try:
            elements = self.wait15.until(lambda driver: driver.find_elements_by_accessibility_id(elementId))
        except Exception as e:
            print e
        
        return elements

    # 获取一个随机时间
    def _random_time(self, minTime=150, maxTime=300):
        return random.randint(minTime, maxTime)

    # 手指向上滑动
    def swipeUp(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration == None:
            duration = self._random_time()
        self.driver.swipe(width/2, height/2, width/2, height/4, duration)
        self.actionSleep(3)

    # 手指向下滑动
    def swipeDown(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration == None:
            duration = self._random_time()
        self.driver.swipe(width/2, height/2, width/2, height*3/4, duration)
        self.actionSleep(3)

    # 手指向左滑动
    def swipeLeft(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration == None:
            duration = self._random_time()
        self.driver.swipe(width/2, height/4, width/2, height/2, duration)
        self.actionSleep(3)

    # 手指向右滑动
    def swipeRight(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration == None:
            duration = self._random_time()
        self.driver.swipe(width/2, height*3/4, width/2, height/2, duration)
        self.actionSleep(3)

    # 等待activity启动
    def waitActivity(self, activity):
        self.driver.wait_activity(activity, 15)

    # 获取当前meminfo
    def getCurrentMem(self):
        return self.driver.get_performance_data(self.appPackage, 'memoryinfo', 5)

    # 睡眠暂停duration秒
    def actionSleep(self, duration=2):
        time.sleep(duration)

    # 按钮back键操作
    def actionBack(self):
        try:
            self.wait5.until(lambda driver: driver.back())
        except Exception as e:
            print e






