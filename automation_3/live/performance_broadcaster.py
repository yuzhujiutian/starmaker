# encoding=utf-8
import sys

from automation_3.base.base import BaseTestCase
from automation_3.base.launch import LaunchAction
from automation_3.main.main import testSuite

sys.path.append('..')


class PerformanceBroadcaster(BaseTestCase):
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
        # 启动
        LaunchAction(self).launch()

        # # 处理轮盘弹窗
        # if self.findElementById("open_promotion_iv_close"):
        #     self.findElementById("open_promotion_iv_close").click()

        # 切换到discovery tab
        LaunchAction(self).toTab(LaunchAction.Discovery)
        el = None

        self.startMemoryProfile()

        while el is None:
            # 点击按钮
            el = self.findElementById(PerformanceBroadcaster.ID_Live_Menu_Btn)
            if el:
                # 统计开始前的内存使用
                self.profile()
                el.click()

        # 开始直播按钮
        self.findElementById(PerformanceBroadcaster.ID_Go_Live_Btn).click()

        # 如果未登录
        if self.findElementById("img_login_email"):
            LaunchAction(self).login()

        self.findElementById(PerformanceBroadcaster.ID_Live_Menu_Btn).click()
        self.actionSleep()
        self.findElementById(PerformanceBroadcaster.ID_Go_Live_Btn).click()

        # 权限弹窗处理
        permissionOkTv = self.findElementById("permissionOkTv")
        if permissionOkTv:
            permissionOkTv.click()
            while self.findElementById("com.android.packageinstaller:id/permission_allow_button"):
                self.findElementById("com.android.packageinstaller:id/permission_allow_button").click()
                self.actionSleep()

        # 等待进入到直播activity
        self.waitActivity(PerformanceBroadcaster.Activity_Live)
        self.actionSleep(8)

        # 处理美颜滤镜引导
        if self.findElementByAU("Be more beautiful!"):
            self.driver.back()
            self.actionSleep()

        # 开启美颜，选择滤镜，做成参数设置

        # 开始直播
        self.findElementById(PerformanceBroadcaster.ID_Start_Live_Btn).click()

        # 处理FB分享弹窗
        self.actionSleep(10)
        self.driver.back()
        self.actionSleep()
        # 处理部分FB客户端会有保存草稿提示
        giveUp_btn = self.findElementByAU("放弃")
        if giveUp_btn:
            giveUp_btn.click()
            self.actionSleep()
        # confirm_btn = self.findElementById(PerformanceBroadcaster.IDE_Close_Live_Confirm_Btn)
        # if confirm_btn:
        #     self.actionBack()

        # 暂停x秒，其实就是直播x秒，目前只能sleep 1秒，多了就会报connect abort的错，原因待查
        count = 0
        threshold = int(testSuite().run_time) * 60
        while count < threshold:
            count += 1
            self.actionSleep(1)

            if count % 5 == 0:
                print("当前直播进度：%.2f%%" % (count/threshold * 100) + "(%u/%u)" % (count, threshold))
                self.profile()

        # 关闭直播
        self.findElementById("iv_room_quit").click()
        confirm_btn = self.findElementById(PerformanceBroadcaster.IDE_Close_Live_Confirm_Btn)
        if confirm_btn:
            confirm_btn.click()

        # 退出关播页面
        self.actionBack()

        # 等待5秒后，计算退出测试用例后的内存占用
        self.actionSleep(5)

        print('stop live, get the memory profile...')
        self.profile()

        self.profileReport(self.__class__.__name__, str(threshold))

        self.driver.quit()


if __name__ == '__main__':
    num = 0
    while num < testSuite().num:
        num += 1
        print("\n当前运行第%s次" % num)
        PerformanceBroadcaster().suiteRunner(PerformanceBroadcaster)
