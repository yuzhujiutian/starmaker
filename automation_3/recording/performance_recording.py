# encoding=utf-8
import sys
import time
import unittest

from automation_3.base.base import BaseTestCase
from automation_3.base.launch import LaunchAction
from automation_3.common.activity import Activity

sys.path.append('..')


class PerformanceRecording(BaseTestCase):

    def test_case001_performance(self):
        launch = LaunchAction(self)

        # 启动
        launch.launch()

        # 开始统计内存占用
        self.startMemoryProfile()

        runs = 2
        song_time = 0
        while runs:
            runs -= 1
            # 切换到sing tab
            launch.toTab(LaunchAction.Sing)

            # 点击其中一首歌曲的sing按钮（共两首歌runs = 1 & 0）
            el = self.findElementsById('btn_sing', runs)
            # 统计开始前的内存占用
            self.profile()
            el.click()

            # 找到弹窗按钮，选择第一个solo
            el = self.findElementsById('item_play_detail_dialog_text', 0)
            el.click()

            # 等待录制页面出现
            self.waitActivity(Activity.Recording)

            # 权限弹窗
            el = self.findElementById('com.android.packageinstaller:id/permission_allow_button')
            while el:
                el.click()
                self.actionSleep()
            # 耳机提示引导
            el = self.findElementById('recording_headset_dialog_i_know_btn')
            el.click()
            self.actionSleep()
            # 音效引导
            el = self.findElementById('tv_pitch_guide_tip')
            if el:
                el.click()
            self.actionSleep(8)

            # 伴奏带下载
            record_btn = self.findElementById('record_btn')
            while record_btn.get_attribute("enabled") is False:
                self.actionSleep()

            # 切换摄像头
            el = self.findElementById('media_type_chb')
            el.click()
            self.actionSleep()

            # 开始录制
            record_btn.click()
            self.actionSleep(8)

            # 获取当前歌曲总时长
            song_time_text = self.findElementById("record_time_tv", True).text
            print(('%s:%s' % ("歌曲时长", song_time_text)))
            minute = song_time_text[0:2]
            second = song_time_text[3:5]
            song_time = int(int(minute) * 60 + int(second) + 3)

            # 等待歌曲录制完成，每5秒取一次性能数据
            t = 0
            while t < song_time:
                self.actionSleep(5)
                self.profile()
                t += 5
                print("当前歌曲进度：%.2f%%" % (t / song_time * 100) + "(%u/%u)" % (t, song_time))

            # 进入到预览页面
            self.waitActivity(Activity.RecordingPreview)
            self.profile()

            # 点击post发布按钮
            post_btn = self.findElementById('btn_post')
            post_btn.click()

            # 登录
            img_login_email = self.findElementById("img_login_email")
            if img_login_email:
                launch.login()
                self.actionSleep(5)
                self.profile()

            # 等待send按钮出现
            send_btn = self.findElementById('btn_next')
            send_btn.click()
            self.profile()
            self.actionSleep()

            # 点击Done按钮发布
            done_btn = self.findElementById('tv_done')
            done_btn.click()
            self.actionSleep(10)
            self.profile()

        # 收集报告
        self.profileReport(self.__class__.__name__, str(song_time))

        self.driver.quit()


if __name__ == '__main__':
    # 定义次数，每次录制发布一首歌曲，记录录制、发布过程中的性能数据
    num = 0
    while num < 5:
        num += 1
        print("\n当前运行第%s次" % num)
        suite = unittest.TestLoader().loadTestsFromTestCase(PerformanceRecording)
        unittest.TextTestRunner(verbosity=2).run(suite)
        time.sleep(60)
