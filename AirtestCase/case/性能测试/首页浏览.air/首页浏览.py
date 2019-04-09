# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
dev = connect_device("android:///")
devs = device()
# ----------------------------------------------------------------------------------
C = 0
print("测试开始")
while (C < 6):
    # setUp
    poco("com.netease.qa.emmagee:id/test").click()
    sleep(10)
    poco("com.starmakerinteractive.thevoice:id/b4u").swipe([0.0533, -0.3112])
    poco(text="English").click()
    poco("android.support.v7.app.a$c")[0].click()
    sleep(5)
    poco("com.starmakerinteractive.thevoice:id/bvf")[2].click()
    # -----测试脚本-----
    A = 0
    photo = 0
    time_start = time.time()
    while (A < 600):
        swipe((360,1088),(360,92))
        sleep(2)
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


# 1>首页浏览
# 11:05 —— 11:15  11:18调整
# 11:19 —— 11:29  11:31调整
# 11:31 —— 11:41  
# 11:42 —— 11:52
# 11:53 —— 12:03  12:18调整
