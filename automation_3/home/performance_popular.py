# encoding=utf-8
import sys
import time
import unittest

from automation_3.base.base import BaseTestCase
from automation_3.home.launch import LaunchAction

sys.path.append('..')


class PerformanceMoment(BaseTestCase):

    # 内容卡片
    AID_Popular_Content_Item = 'popular_content_item'

    # Recording
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
        # 启动
        launch = LaunchAction(self)
        launch.launch()

        # 处理轮盘弹窗
        if self.findElementById("open_promotion_iv_close"):
            self.findElementById("open_promotion_iv_close").click()

        # 切换到trend tab
        LaunchAction(self).toTab(LaunchAction.Trend)
        els = None

        # 开始统计memory
        self.startMemoryProfile()

        while els is None:
            # 内容卡片是否已经加载出来
            els = self.findElementsByAID(PerformanceMoment.AID_Popular_Content_Item, 0)
            if els:
                print('switch to trend tab...')
                break
            else:
                self.actionSleep(1)

        # 等待播放详情页
        # self.findElementsByAID(PerformanceMoment.AID_Popular_Content_Item, 0).click()
        # self.waitActivity(PerformanceMoment.Activity_Recording)

        start_time = time.time()
        t = 0
        threshold = run_time * 60
        while t < threshold:
            # 找到当前屏首个recording
            self.findElementsByAID(PerformanceMoment.AID_Popular_Content_Item, 0).click()
            # 进入播放详情页
            self.profile()

            # 播放5秒
            self.actionSleep(5)

            # 记录内存使用情况
            self.profile()

            # 再播放5秒
            self.actionSleep(5)

            # 回到首页
            self.actionBack()

            # 记录内存使用情况
            self.profile()

            self.actionSleep(1)

            # 向下浏览
            self.swipeUp()

            end_time = time.time()
            t = end_time - start_time

        self.profileReport(self.__class__.__name__, str(threshold))

        self.driver.quit()


if __name__ == '__main__':
    # 设定运行时间(分钟)
    run_time = 10

    num = 0
    while num < 4:
        num += 1
        print(num)
        suite = unittest.TestLoader().loadTestsFromTestCase(PerformanceMoment)
        unittest.TextTestRunner(verbosity=2).run(suite)
        time.sleep(60)
