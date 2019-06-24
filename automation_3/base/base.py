# encoding=utf-8
import random
import sys
import time
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

from automation_3.common.activity import Activity
from automation_3.report.performance_mem import AndroidMemoryReport
from automation_3.utils.android_proguard_mapping import AndroidProGuardMapping
from .log import QmClassMethodLog

sys.path.append('..')


# 基础方法封装
class BaseAction(metaclass=QmClassMethodLog):
    def __init__(self, baseTestCase):
        self.tc = baseTestCase

    # 对话框确认逻辑，
    def dialogBtnClick(self, confirm=True):
        # 检查dialog是否存在
        if confirm:
            yesBtn = self.findElementById('md_buttonDefaultPositive')
            self.singleTap(yesBtn)
        else:
            noBtn = self.findElementById('md_buttonDefaultNegative')
            self.singleTap(noBtn)

    def findElementById(self, elementId, wait=False):
        return self.tc.findElementById(elementId, wait)

    def findElementsById(self, elementId, wait=False):
        return self.tc.findElementsById(elementId, wait)

    def findElementByAId(self, elementId, wait=False):
        return self.tc.findElementByAId(elementId, wait)

    def waitActivity(self, activity, timeout=9):
        return self.tc.waitActivity(activity, timeout)

    def log(self, info):
        return self.tc.log(info)

    def actionSleep(self, duration):
        self.tc.actionSleep(duration)

    def clearDialog(self):
        self.tc.clearDialog()

    def singleTap(self, element):
        self.tc.singleTap(element)


class BaseTestCase(unittest.TestCase):
    # 某些test case的连接的属性值会有不同，提供给子类进行自定义
    def capsSetup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'fe5bb46e'
        desired_caps['appPackage'] = 'com.starmakerinteractive.starmaker'
        desired_caps['appActivity'] = 'com.ushowmedia.starmaker.activity.SplashActivity'
        desired_caps['appWaitActivity'] = ','.join([Activity.Main, Activity.Nux_Language])
        # desired_caps['automationName'] = 'uiautomator2'
        # desired_caps['noReset'] = 'true'
        desired_caps['autoGrantPermissions'] = True
        # desired_caps['autoAcceptAlerts'] = True
        # defaultCommandTimeout
        desired_caps['newCommandTimeout'] = 500  # session默认超时时间
        return desired_caps

    def setUp(self):
        desired_caps = self.capsSetup()
        self.appPackage = desired_caps.get('appPackage')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait15 = WebDriverWait(self.driver, 15, 1)
        self.wait5 = WebDriverWait(self.driver, 5, 1)

        # 内存统计
        self.memoryProfile = None

        self.mappingFile = desired_caps.get('mappingFile', None)
        # print dir(self.driver)
        # self.mappingFile = '../example/mapping.txt'
        self.mapping = AndroidProGuardMapping(self.mappingFile)

    def tearDown(self):
        pass

    # wait: 如果为true, 会一直等待知道元素出现
    def findElementById(self, elementId, wait=False):
        # print elementId
        elementId = self.mapping.getId(elementId)
        # print elementId
        element = None
        while element is None:
            try:
                element = self.wait5.until(lambda driver: driver.find_element_by_id(elementId))
            except Exception as e:
                print(e)

            if not wait:
                break

        return element

    def findElementsById(self, elementId, wait=False):
        # print elementId
        elementId = self.mapping.getId(elementId)
        # print elementId
        element = None
        while element is None:
            try:
                element = self.wait5.until(lambda driver: driver.find_elements_by_id(elementId))
            except Exception as e:
                print(e)

            if not wait:
                break

        return element

    def findElementByAId(self, elementId, wait=False):
        element = None
        while element is None:
            try:
                element = self.wait5.until(lambda driver: driver.find_element_by_accessibility_id(elementId))
            except Exception as e:
                print(e)

            if not wait:
                break

        return element

    def findElementsByAID(self, elementId):
        elements = None
        try:
            elements = self.wait15.until(lambda driver: driver.find_elements_by_accessibility_id(elementId))
        except Exception as e:
            print(e)

        return elements

    # 获取一个随机时间
    def _random_time(self, minTime=150, maxTime=300):
        return random.randint(minTime, maxTime)

    # 手指向上滑动
    def swipeUp(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration is None:
            duration = self._random_time()
        self.driver.swipe(width / 2, height / 2, width / 2, height / 4, duration)
        self.actionSleep(3)

    # 手指向下滑动
    def swipeDown(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration is None:
            duration = self._random_time()
        self.driver.swipe(width / 2, height / 2, width / 2, height * 3 / 4, duration)
        self.actionSleep(3)

    # 手指向左滑动
    def swipeLeft(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration is None:
            duration = self._random_time()
        self.driver.swipe(width / 2, height / 4, width / 2, height / 2, duration)
        self.actionSleep(3)

    # 手指向右滑动
    def swipeRight(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration is None:
            duration = self._random_time()
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 2, duration)
        self.actionSleep(3)

    def singleTap(self, element=None):
        if element is None:
            return
        action = TouchAction(self.driver)
        action.tap(element)
        action.perform()

    # 等待activity启动
    def waitActivity(self, activity, timeout=9):
        return self.driver.wait_activity(activity, timeout)

    # 获取当前meminfo
    def getCurrentMem(self):
        return self.driver.get_performance_data(self.appPackage, 'memoryinfo', 5)

    # 睡眠暂停duration秒
    def actionSleep(self, duration=2):
        time.sleep(duration)

    # 清理弹窗
    def clearDialog(self):
        self.log('check to clear dialog...')
        try:
            el = self.findElementById('iv_close')
            self.singleTap(el)
        except Exception as e:
            self.log(e)

    # 按钮back键，回到上一个activity, waitActivity为上一个activity
    # 如果不设置waitActivity, 那么只是执行back键
    def actionBack(self, waitActivity=None):
        try:
            self.wait5.until(lambda driver: driver.back())
        except Exception as e:
            print(e)

        if waitActivity is not None:
            returned = False
            while not returned:
                # 等待回到上一个页面
                returned = self.waitActivity(waitActivity)

                if not returned:
                    try:
                        self.wait5.until(lambda driver: driver.back())
                    except Exception as e:
                        print(e)

    # 开始内存统计
    def startMemoryProfile(self):
        if self.memoryProfile is None:
            self.memoryProfile = AndroidMemoryReport(self.appPackage, self.driver)
            self.memoryProfile.profile()

    # 统计当前内存占用
    def profile(self):
        if self.memoryProfile is None:
            print('error: please call startMemoryProfile first...')
        else:
            self.memoryProfile.profile()

    def profileReport(self):
        if self.memoryProfile is None:
            pass
        else:
            self.memoryProfile.toReport()

    # 打印日志相关， TODO: 丰富功能
    def log(self, info):
        # print info
        pass
