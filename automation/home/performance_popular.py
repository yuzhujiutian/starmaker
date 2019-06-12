#encoding=utf-8
import sys; 
sys.path.append('..') 

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from appium.webdriver.common.touch_action import TouchAction

import unittest
import random

from common.home import Home
from base.base import BaseTestCase

class PerformanceMoment(BaseTestCase):

    # 内容卡片
    AID_Popular_Content_Item = 'popular_content_item'

    # 直播activity
    Activity_Recording = 'com.ushowmedia.starmaker.playdetail.PlayDetailActivity'

    # 主activity
    Activity_Main = 'com.ushowmedia.starmaker.activity.MainActivity'

    '''
    测试首页的内存占用情况
    1.  切换到首页
    2.  等待卡片内容展示出来
    3.  随机点击一张卡片，进入播放详情页，观看10秒，退出播放详情页，
    4.  退回到首页，首页向下浏览，再重复动作3，反复执行n次
    '''
    def test_case001_performance(self):
        # 切换到trend tab
        home = Home(self.driver)
        els = None

        # 开始统计memory
        self.startMemoryProfile()

        while els is None:
            home.switch_tab(Home.Trend)

            # 内容卡片是否已经加载出来
            els = self.findElementsByAID(PerformanceMoment.AID_Popular_Content_Item)
            if els != None:
                print 'switch to trend tab...'
                break
            else:
                self.actionSleep(1)

        count = 0

        # 执行次数
        threshold = 150

        self.profile()

        while  count < threshold:
            # 随机选取一个，进入播放详情页
            index = random.randint(0, 1000)%len(els)
            el = els[index]
            el.click()

            # 等待播放详情页
            self.waitActivity(PerformanceMoment.Activity_Recording)

            # 播放5秒
            self.actionSleep(5)

            # 记录内存使用情况
            self.profile()

            # 再播放5秒
            self.actionSleep(5)

            # 回到首页
            self.actionBack(waitActivity=PerformanceMoment.Activity_Main)

            # 记录内存使用情况
            self.profile()

            self.actionSleep(1)

            # 向下浏览
            self.swipeUp()

            # 查找新的内容卡片
            els = self.findElementsByAID(PerformanceMoment.AID_Popular_Content_Item)

            count += 1

        self.profileReport()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PerformanceMoment)
    unittest.TextTestRunner(verbosity=2).run(suite)







            