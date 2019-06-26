# encoding=utf-8
import sys
import unittest

from automation_2.base.base import BaseTestCase
from automation_2.home.launch import LaunchAction

sys.path.append('..')


class PerformanceBoradcaster(BaseTestCase):
    # 右上角按钮id
    ID_Live_Menu_Btn = 'entertainment_tab_drawer'

    # 开始直播按钮
    ID_Go_Live_Btn = 'go_live'

    # FB分享按钮
    ID_FB_Share_Btn = 'img_facebook'

    # 开始直播按钮
    ID_Start_Live_Btn = 'rlyt_start_live'

    # 关闭直播弹窗确认按钮
    IDE_Close_Live_Confirm_Btn = 'md_buttonDefaultPositive'

    # 直播activity
    Activity_Live = 'com.ushowmedia.livelib.room.LiveRoomActivity'

    """
    主播开播的自动化性能测试

    期望的结果
    1.  主播可以正常开播
    2.  推流正常
    3.  推流的内容正常
    4.  统计开播前的内存占用，cpu占用
    5.  统计直播中的平均内存占用，cpu占用，最高和最低的内存占用
    6.  统计结束直播后的内存占用，cpu占用

    对于已登录用户
    1.  打开App, 切换到discovery tab
    2.  点击右上角按钮，出现弹窗
    3.  点击直播按钮，进入直播页面
    4.  输入直播名称(可选)，开启美颜(可选)
    5.  点击开始直播按钮, 开始直播
    6.  每隔15秒采集一次性能
    7.  持续开播30分钟, 60分钟，3小时

    TODO:
    1.  直播中出现异常，网络不稳定，被踢下线等等
    2.  开播失败
    3.  直播推流的内容有问题，花屏，卡顿
    4.  长连接的问题
    """
    def test_case001_performance(self):
        # 切换到discovery tab
        home = LaunchAction(self.driver).toTab(LaunchAction.Discovery)
        el = None

        self.startMemoryProfile()

        while el is None:
            # home.switch_tab(Home.Discovery)

            # 点击按钮
            el = self.findElementById(PerformanceBoradcaster.ID_Live_Menu_Btn)
            if el:
                # 统计开始前的内存使用
                self.profile()
                el.click()

        # 开始直播按钮
        goLive = self.findElementById(PerformanceBoradcaster.ID_Go_Live_Btn)
        goLive.click()

        # TODO: 权限弹窗处理

        # 等待进入到直播activity
        self.waitActivity(PerformanceBoradcaster.Activity_Live)

        # 取消分享到FB, 开始直播
        fbShareBtn = self.findElementById(PerformanceBoradcaster.ID_FB_Share_Btn)
        fbShareBtn.click()

        # 开启美颜，选择滤镜，做成参数设置
        
        # 开始直播
        startLiveBtn = self.findElementById(PerformanceBoradcaster.ID_Start_Live_Btn)
        startLiveBtn.click()

        # 暂停15秒，其实就是直播15秒，目前只能sleep 1秒，多了就会报connect abort的错，原因待查
        count = 0
        threshold = 1 * 60 / 5
        while count < threshold:
            count += 1
            self.actionSleep(1)

            if count%5 == 0:
                self.profile()

        closeLiveConfirmBtn = None
        retryCount = 0
        while closeLiveConfirmBtn is None:
            # 准备关闭直播
            self.actionBack()
            closeLiveConfirmBtn = self.findElementById(PerformanceBoradcaster.IDE_Close_Live_Confirm_Btn)
            if closeLiveConfirmBtn:
                closeLiveConfirmBtn.click()

            retryCount += 1
            if retryCount >= 3:
                print 'some error happen when exit live room...'
                break

            self.actionSleep(1)

        # 退出直播页面
        self.actionBack()

        # 等待5秒后，计算退出测试用例后的内存占用
        self.actionSleep(1)

        print 'stop live, get the memory profile...'
        self.profile()

        self.profileReport()
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PerformanceBoradcaster)
    unittest.TextTestRunner(verbosity=2).run(suite)



