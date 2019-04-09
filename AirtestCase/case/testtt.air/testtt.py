# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
import time
from airtest.core.api import *
from airtest.core.android.android import *
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
dev = connect_device("android:///")
devs = device()
# -----------------------


# install("C:/Users/cucumber/Desktop/thevoiceRelease-minApi21-armeabi-v7a-82730001-2019-01-11-08-46.apk")
# 
# uninstall("com.starmakerinteractive.thevoice")

clear_app("com.starmakerinteractive.thevoice")
