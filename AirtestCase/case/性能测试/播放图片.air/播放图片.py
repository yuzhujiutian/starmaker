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
    poco("android.support.v7.app.a$c")[0].click()
    sleep(5)
    poco("com.starmakerinteractive.thevoice:id/bvf")[2].click()
    # -----测试脚本-----
    A = 0
    photo = 0
    print("测试开始")
    time_start = time.time()
    while (A < 600):
        swipe((360,1088),(360,92))
        try:
            # 图片 yy
            poco("com.starmakerinteractive.thevoice:id/yy").click()
            sleep(2)
            keyevent("BACK")
            photo = photo + 1
            print(photo)
        except:
            pass
        finally:
            swipe((360,1088),(360,92))
            time_end = time.time()
            A = time_end - time_start
            print(A)
    # tearDown
    stop_app("com.starmakerinteractive.thevoice")
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

# 2>播放图片
# 02:11 —— 02:21 2:53 调整
# 02:54 —— 03:04 3:10 调整
# 03:11 —— 03:22
# 03:23 —— 03:33
# 03:34 —— 03:44