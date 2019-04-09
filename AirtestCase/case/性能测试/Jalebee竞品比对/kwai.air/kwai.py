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
while (C < 3):
    # setUp
    poco("com.netease.qa.emmagee:id/test").click()
    sleep(8)
    # -----测试脚本-----
    A = 0
    video = 0
    print("测试开始")
    time_start = time.time()
    while (A < 600):
#         swipe((560,1050),(560,92))
        try:
            # 视频 abu
#             poco("com.kwai.video:id/player").click()
            swipe((560,1050),(560,92))
            sleep(8)
#             keyevent("BACK")
            video = video + 1
            print(video)
        except:
            pass
        finally:
#             swipe((560,1088),(560,92))
            time_end = time.time()
            A = time_end - time_start
            print(A)
    # tearDown
    clear_app("com.ss.android.ugc.trill")
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





# Jalebee:com.ushow.android.jalebee/com.ushowmedia.starmaker.activity.SplashActivity
# vmate:com.uc.vmate/.ui.MainActivity
# vigo:com.ss.android.ugc.boom/com.ss.android.ugc.live.main.MainActivity
# kwai:com.kwai.video/com.yxcorp.gifshow.login.SplashLoginActivity
# togetu:in.togetu.video/in.togetu.shortvideo.ui.activity.SplashActivity
# tiktok:com.ss.android.ugc.trill/com.ss.android.ugc.aweme.splash.SplashActivity