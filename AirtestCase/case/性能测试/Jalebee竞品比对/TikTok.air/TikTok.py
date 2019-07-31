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
def tiktok_test():
    print("测试开始")
    # 点击录制
    poco("com.ss.android.ugc.trill:id/ad4").child("android.widget.FrameLayout")[2].child("android.widget.ImageView").click()
    # 等待贴纸出现
    poco("com.ss.android.ugc.trill:id/ahx").wait(20)
    # 选择贴纸Firework + 滤镜F1
    poco("com.ss.android.ugc.trill:id/ahx").click()
    sleep(5)
    poco("com.ss.android.ugc.trill:id/aw2").child("android.widget.RelativeLayout")[0].child("com.ss.android.ugc.trill:id/wt").click()
    keyevent("BACK")
    # 选择音乐
    poco("com.ss.android.ugc.trill:id/uv").click()
    sleep(5)
    poco("com.ss.android.ugc.trill:id/b97").child("android.widget.LinearLayout")[0].child("com.ss.android.ugc.trill:id/axs")[0].child("com.ss.android.ugc.trill:id/axt").child("com.ss.android.ugc.trill:id/anp").click()
    poco("com.ss.android.ugc.trill:id/apq").click()
    # 等待Start按钮
    poco("com.ss.android.ugc.trill:id/s6").wait(30)
    A = 0
    count = 0
    time_start = time.time()
    while (A < 600):
        try:
            # 开始录制
            poco("com.ss.android.ugc.trill:id/s6").click()
            poco("com.ss.android.ugc.trill:id/iv").wait(30)
            # tearDown：返回——删除——确认删除
            poco("com.ss.android.ugc.trill:id/iv").click()
            poco("com.ss.android.ugc.trill:id/ai4").click()
            poco("android:id/button1").click()
            sleep(1)
            count = count + 1
            print(count)
        except:
            if poco("com.ss.android.ugc.trill:id/iv").exists():
                poco("com.ss.android.ugc.trill:id/iv").click()
        finally:
            time_end = time.time()
            A = time_end - time_start
            print(A)
    print("测试结束")
    stop_app("com.ss.android.ugc.trill")
    
Rotation = 0
while (Rotation < 6):
    # 开始测试
    poco("com.netease.qa.emmagee:id/test").click()
    sleep(10)
    if poco("android:id/button2").exists():
        poco("android:id/button2").click()
    tiktok_test()
    sleep(3)
    Rotation = Rotation + 1
    print(Rotation)
    print(Rotation)
    print(Rotation)
    print(Rotation)
    print(Rotation)
    # 结束测试
    if poco("com.netease.qa.emmagee:id/test").get_text() == "停止测试":
        poco("com.netease.qa.emmagee:id/test").click()
    
    

    
    
# 开始时间：15:10