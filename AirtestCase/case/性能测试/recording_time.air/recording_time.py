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
# -------------------
TimeList = []
Count = 0
while(Count < 12):
    # 新安装首次启动
    install("C:/Users/cucumber/Desktop/thevoiceRelease-minApi21-armeabi-v7a-82729005-2019-01-08-10-23.apk")
    time_start = time.time()
    start_app("com.starmakerinteractive.thevoice")
    poco("android.widget.TextView").wait(10)
    time_end = time.time()
    A = int(round((time_end - time_start),3) * 1000)
    print(A)
    TimeList.append(A)
    Count = Count + 1
    print(Count)
    uninstall("com.starmakerinteractive.thevoice")
    # 非首次安装冷启动
    # time_start = time.time()
    # start_app("com.starmakerinteractive.thevoice")
    # poco("android.widget.TextView").wait(10)
    # time_end = time.time()
    # A = int(round((time_end - time_start),3) * 1000)
    # print(A)
    # TimeList.append(A)
    # Count = Count + 1
    # print(Count)
    # clear_app("com.starmakerinteractive.thevoice")
    
# 打印测试数据
print(TimeList)