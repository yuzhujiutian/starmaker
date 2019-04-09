# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
from airtest.core.api import *
from airtest.core.android.android import *
auto_setup(__file__)
# -------------------
dev = connect_device("android:///")
devs = device()
# 安装包
install("C:/Users/cucumber/Desktop/thevoiceRelease-minApi21-armeabi-v7a-82727000-2018-11-30-02-25.apk")

A = Android().start_app_timing("com.starmakerinteractive.thevoice","com.ushowmedia.starmaker.activity.SplashActivity")
print(A)
print(A)
print(A)
uninstall("com.starmakerinteractive.thevoice")
# clear_app("com.starmakerinteractive.thevoice")
