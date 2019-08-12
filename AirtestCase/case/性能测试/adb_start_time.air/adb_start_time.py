# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
from airtest.core.android.android import *
from airtest.core.api import *

auto_setup(__file__)
dev = connect_device("android:///")
devs = device()
# -------------------
TimeList = []
Count = 0
while(Count < 12):
    # 新安装首次启动
    # install("C:/Users/cucumber/Desktop/thevoiceRelease-minApi21-armeabi-v7a-82730001-2019-01-11-08-46.apk")
    # A = Android().start_app_timing("com.starmakerinteractive.thevoice","com.ushowmedia.starmaker.activity.SplashActivity")
    # print(A)
    # TimeList.append(A)
    # uninstall("com.starmakerinteractive.thevoice")
    # Count = Count + 1
    # print(Count)
    # ----------------
    # 非首次安装冷启动
    A = Android().start_app_timing("com.starmakerinteractive.thevoice","com.ushowmedia.starmaker.activity.SplashActivity")
    print(A)
    TimeList.append(A)
    Count = Count + 1
    print(Count)
    clear_app("com.starmakerinteractive.thevoice")

# 打印测试数据
print(TimeList)