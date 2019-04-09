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
print("测试开始")
# -----测试脚本-----
A = 0
time_start = time.time()
while (A < 1800):
    swipe((360,1088),(360,92))
    sleep(2)
    time_end = time.time()
    A = time_end - time_start
    print(A)
# tearDown
T = time.strftime('%H.%M.%S',time.localtime(time.time()))
print("结束时间")
print(T)
    
print("测试结束")

