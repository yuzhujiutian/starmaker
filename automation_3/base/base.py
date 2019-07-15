# encoding=utf-8
import datetime
import os
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
        # 定义测试图片存放路径
        self.png_file = "../report/images/"

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

    def actionSleep(self, duration=2):
        self.tc.actionSleep(duration)

    def clearDialog(self):
        self.tc.clearDialog()

    def singleTap(self, element):
        self.tc.singleTap(element)

    def TestPicture_Processing(self):
        self.tc.TestPicture_Processing()

    def get_error_screenshot(self):
        self.tc.get_error_screenshot()


class BaseTestCase(unittest.TestCase):
    # 某些test case的连接的属性值会有不同，提供给子类进行自定义
    def capsSetup(self):
        self.png_file = "../report/images/"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8'
        desired_caps['device'] = 'SM_G610F'
        desired_caps['deviceName'] = 'on7xelte'
        # desired_caps['appPackage'] = 'com.starmakerinteractive.starmaker'
        desired_caps['appPackage'] = 'com.horadrim.android.sargam'
        desired_caps['appActivity'] = 'com.ushowmedia.starmaker.activity.SplashActivity'
        desired_caps['appWaitActivity'] = ','.join([Activity.Main, Activity.Nux_Language])
        # desired_caps['automationName'] = 'appium'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['noReset'] = False
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        desired_caps['autoGrantPermissions'] = True
        desired_caps['autoAcceptAlerts'] = True
        # defaultCommandTimeout
        # desired_caps['newCommandTimeout'] = 500  # session默认超时时间
        return desired_caps

    def setUp(self):
        desired_caps = self.capsSetup()
        self.appPackage = desired_caps.get('appPackage')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait15 = WebDriverWait(self.driver, 15, 1)
        self.wait5 = WebDriverWait(self.driver, 5, 1)

        # 内存统计
        self.memoryProfile = None

        # cpu统计
        self.cpuProfile = None

        # self.mappingFile = desired_caps.get('mappingFile', None)
        self.mappingFile = '../example/mapping.txt'
        self.mapping = AndroidProGuardMapping(self.mappingFile)

    def tearDown(self):
        pass

    # 截图
    def get_screenshot(self):
        # 获取当前时间作为图片名称
        img_name = (datetime.datetime.now() + datetime.timedelta()).strftime('%Y%m%d_%H.%M.%S') + '.png'
        print(img_name)
        # 截图
        self.driver.get_screenshot_as_file('%s%s' % (self.png_file, img_name))

    # 错误截图，day -1置于images上方便于查找
    def get_error_screenshot(self):
        # 获取当前时间作为图片名称
        img_name = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d_%H.%M.%S') + '_error.png'
        print(img_name)
        # 截图
        self.driver.get_screenshot_as_file('%s%s' % (self.png_file, img_name))

    # 测试数据处理，处理测试图片
    def TestPicture_Processing(self):
        images_list = os.listdir(self.png_file)
        for i in images_list:
            images = os.path.join(self.png_file, i)
            Suffix = os.path.splitext(i)[1]
            if Suffix == ".png":
                os.remove(images)
        self.log("测试图片已清理完毕")

    # wait: 如果为true, 会一直等待直到元素出现
    def findElementById(self, elementId, wait=False):
        elementId = self.mapping.getId(elementId)
        element = None
        while element is None:
            try:
                element = self.wait5.until(lambda driver: driver.find_element_by_id(elementId))
            except Exception as e:
                self.get_error_screenshot()
                self.log(e)

            if not wait:
                break

        return element

    def findElementsById(self, elementId, num, wait=False):
        elementId = self.mapping.getId(elementId)
        element = None
        while element is None:
            try:
                element = self.wait5.until(lambda driver: driver.find_elements_by_id(elementId)[num])
            except Exception as e:
                self.get_error_screenshot()
                self.log(e)

            if not wait:
                break

        return element

    def findElementByAId(self, elementId, wait=False):
        element = None
        while element is None:
            try:
                element = self.wait5.until(lambda driver: driver.find_element_by_accessibility_id(elementId))
            except Exception as e:
                self.get_error_screenshot()
                self.log(e)

            if not wait:
                break

        return element

    def findElementsByAID(self, elementId, num, wait=False):
        elements = None
        while elements is None:
            try:
                elements = self.wait5.until(lambda driver: driver.find_elements_by_accessibility_id(elementId)[num])
            except Exception as e:
                self.get_error_screenshot()
                self.log(e)

            if not wait:
                break

        return elements

    def findElementByAU(self, elementId, wait=False):
        element = None
        elementId = "new UiSelector().text(\"%s\")" % elementId
        while element is None:
            try:
                element = self.wait5.until(lambda driver: driver.find_element_by_android_uiautomator(elementId))
            except Exception as e:
                self.get_error_screenshot()
                self.log(e)

            if not wait:
                break

        return element

    def findElementsByAU(self, elementId, num, wait=False):
        elements = None
        elementId = "new UiSelector().text(\"%s\")" % elementId
        while elements is None:
            try:
                elements = self.wait5.until(lambda driver: driver.find_element_by_android_uiautomator(elementId)[num])
            except Exception as e:
                self.get_error_screenshot()
                self.log(e)

            if not wait:
                break

        return elements

    # 获取一个随机时间
    @staticmethod
    def _random_time(minTime=150, maxTime=300):
        return random.randint(minTime, maxTime)

    # 手指向上滑动
    def swipeUp(self, duration=500):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration is None:
            duration = self._random_time()
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, duration)
        self.actionSleep(3)

    # 手指向下滑动
    def swipeDown(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration is None:
            duration = self._random_time()
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, duration)
        self.actionSleep(3)

    # 手指向左滑动
    def swipeLeft(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration is None:
            duration = self._random_time()
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, duration)
        self.actionSleep(3)

    # 手指向右滑动
    def swipeRight(self, duration=None):
        screenSize = self.driver.get_window_size()
        width = screenSize['width']
        height = screenSize['height']
        if duration is None:
            duration = self._random_time()
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, duration)
        self.actionSleep(3)

    # 点击
    def singleTap(self, element=None):
        if element is None:
            return
        action = TouchAction(self.driver)
        action.tap(element)
        action.perform()

    # 等待activity启动
    def waitActivity(self, activity, timeout=9):
        return self.driver.wait_activity(activity, timeout)

    # 获取当前memoryinfo
    def getCurrentMem(self):
        return self.driver.get_performance_data(self.appPackage, 'memoryinfo', 5)

    # 获取当前cpuinfo
    def getCurrentCPU(self):
        return self.driver.get_performance_data(self.appPackage, 'cpuinfo', 5)

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
            self.log(e)

        if waitActivity:
            returned = False
            while not returned:
                # 等待回到上一个页面
                returned = self.waitActivity(waitActivity)

                if not returned:
                    try:
                        self.wait5.until(lambda driver: driver.back())
                    except Exception as e:
                        self.log(e)

    # 开始内存/cpu统计
    def startMemoryProfile(self):
        if self.memoryProfile is None:
            self.memoryProfile = AndroidMemoryReport(self.appPackage, self.driver)
            self.memoryProfile.memory_profile()

        if self.cpuProfile is None:
            self.cpuProfile = AndroidMemoryReport(self.appPackage, self.driver)
            self.cpuProfile.cpu_profile()

    # 统计当前内存/cpu占用
    def profile(self):
        if self.memoryProfile is None:
            self.log('error: please call startMemoryProfile first...')
        else:
            self.memoryProfile.memory_profile()

        if self.cpuProfile is None:
            self.log('error: please call startMemoryProfile first...')
        else:
            self.cpuProfile.cpu_profile()

    def profileReport(self, module_name="check_list", run_time="10 minutes"):
        if self.memoryProfile is None:
            pass
        else:
            self.memoryProfile.toReport_memInfos(module_name, run_time)

        if self.cpuProfile is None:
            pass
        else:
            self.cpuProfile.toReport_cpuInfos(module_name, run_time)

    # 测试套运行
    def suiteRunner(self, task):
        suite = unittest.TestLoader().loadTestsFromTestCase(task)
        unittest.TextTestRunner(verbosity=2).run(suite)
        self.actionSleep(180)

    # 截图并打印日志
    def log(self, info):
        self.get_screenshot()
        print(info)
