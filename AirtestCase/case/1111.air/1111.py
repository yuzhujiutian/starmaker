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
# install("C:/Users/cucumber/Desktop/thevoiceRelease-minApi21-armeabi-v7a-82727001-2018-12-05-03-06.apk")
A = 0
time_start = time.time()
print("测试开始")
while (A < 600):
    swipe((360,1088),(360,92))
    sleep(2)
    time_end = time.time()
    A = time_end - time_start
    print(A)
print("测试结束")
stop_app("com.starmakerinteractive.thevoice")
    


# 播放图片  727线上  end_time
# 1> 06:32:22  调整 06:38:00
# 2> 06:49:28
# 3> 07:00:55


