# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
import time

from airtest.core.android.android import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
dev = connect_device("android:///")
devs = device()
# ----------------------------------------------------------------------------------
C = 0
TimeEnd_List = []
Count_List = []
print("测试开始")
while (C < 10):
    # setUp
    poco("com.netease.qa.emmagee:id/test").click()
    sleep(8)
    poco("com.ushow.android.jalebee:id/bh5").click()
    sleep(2)
    poco("com.ushow.android.jalebee:id/bg9").click()
    sleep(5)
    # -----测试脚本-----
    A = 0
    Count = 0
    print("测试开始")
    time_start = time.time()
    while (A < 600):
        try:
            swipe((560,1050),(560,92))
            sleep(2)
            Count += 1
        except:
            pass
        finally:
            time_end = time.time()
            A = time_end - time_start
            print(A)
    print("脚本结束共滑动次数")
    print(Count)
    Count_List.append(Count)
    # tearDown
    clear_app("com.ushow.android.jalebee")
    sleep(5)
    if poco("com.netease.qa.emmagee:id/test").get_text() == "停止测试":
        poco("com.netease.qa.emmagee:id/test").click()
    sleep(2)
    C = C + 1
    T = time.strftime('%H.%M.%S',time.localtime(time.time()))
    print("执行次数")
    print(C)
    print("结束时间")
    print(T)
    TimeEnd_List.append(T)
print("批次结束时间列表")
print(TimeEnd_List)
print("滑动次数列表")
print(Count_List)
print("测试结束")


# 19:10



# Jalebee:com.ushow.android.jalebee/com.ushowmedia.starmaker.activity.SplashActivity
# vmate:com.uc.vmate/.ui.MainActivity
# vigo:com.ss.android.ugc.boom/com.ss.android.ugc.live.main.MainActivity
##vigo lite:com.ss.android.ugc.boomlite/com.ss.android.ugc.live.main.MainActivity
# kwai:com.kwai.video/com.yxcorp.gifshow.login.SplashLoginActivity
# togetu:in.togetu.video/in.togetu.shortvideo.ui.activity.SplashActivity
# tiktok:com.ss.android.ugc.trill/com.ss.android.ugc.aweme.splash.SplashActivity