# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
import time

from airtest.core.android.android import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
dev = connect_device("android:///")
devs = device()
# ----------------------------------------------------------------------------------
A = 0
photo = 0
print("测试开始")
time_start = time.time()
while (A < 600):
    swipe((360,1088),(360,92))
    sleep(2)
    time_end = time.time()
    A = time_end - time_start
    print(A)
    # try:
    #     # 图片 yz
    #     # 视频 aba
    #     poco("com.starmakerinteractive.thevoice:id/yz").click()
    #     sleep(2)
    #     keyevent("BACK")
    #     photo = photo + 1
    #     print(video)
    # except:
    #     pass
    # finally:
    #     swipe((360,1088),(360,92))
    #     time_end = time.time()
    #     A = time_end - time_start
    #     print(A)
print("测试结束")
stop_app("com.starmakerinteractive.thevoice")


# 1>首页浏览
# 10:58 —— 07:35
# 07:35 —— 07:46
# 07:46 —— 07:57
# 07:58 —— 08:08
# 08:08 —— 08:18