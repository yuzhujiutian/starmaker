# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
import time
from airtest.core.api import *
from airtest.core.android.android import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
dev = connect_device("android:///")
devs = device()
# ----------------------------------------------------------------------------------
C = 0
print("测试开始")
while (C < 4):
    # setUp
    poco("com.netease.qa.emmagee:id/test").click()
    sleep(10)
    poco("com.starmakerinteractive.thevoice:id/b4u").swipe([0.0533, -0.3112])
    poco("com.starmakerinteractive.thevoice:id/bzl")[-1].click()
    sleep(2)
    poco("android.support.v7.app.a$c")[0].click()
    sleep(8)
    poco("com.starmakerinteractive.thevoice:id/bvf")[2].click()
    # -----测试脚本-----
    A = 0
    video = 0
    print("测试开始")
    time_start = time.time()
    while (A < 600):
        swipe((360,1088),(360,92))
        try:
            # 视频 ab_
            poco("com.starmakerinteractive.thevoice:id/ab_").click()
            sleep(5)
            keyevent("BACK")
            video = video + 1
            print(video)
        except:
            pass
        finally:
            swipe((360,1088),(360,92))
            time_end = time.time()
            A = time_end - time_start
            print(A)
    # tearDown
    clear_app("com.starmakerinteractive.thevoice")
    sleep(5)
    if poco("com.netease.qa.emmagee:id/test").get_text() == "停止测试":
        poco("com.netease.qa.emmagee:id/test").click()
    C = C + 1
    T = time.strftime('%H.%M.%S',time.localtime(time.time()))
    print("执行次数")
    print(C)
    print("结束时间")
    print(T)
    
print("测试结束")

# 3>播放视频
# 03:46 —— 03:56
# 04:03 —— 04:13
# 04:14 —— 04:24
# 04:25 —— 04:35
# 04:37 —— 04:47
# 04:49 —— 04:59



# Jalebee:com.ushow.android.jalebee/com.ushowmedia.starmaker.activity.SplashActivity
# vmate:com.uc.vmate/.ui.MainActivity
# kwai:com.kwai.video/com.yxcorp.gifshow.login.SplashLoginActivity
# togetu:in.togetu.video/in.togetu.shortvideo.ui.activity.SplashActivity
# vigo:com.ss.android.ugc.boom/com.ss.android.ugc.live.main.MainActivity
# tiktok:com.ss.android.ugc.trill/com.ss.android.ugc.aweme.splash.SplashActivity