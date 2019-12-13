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
# 1>脚本执行次数
run_number = 5
# 2>单次脚本执行时间
single_run_time = 600
# 3>测试package name
package_name = "com.horadrim.android.sargam"
clear_app(package_name)
sleep(4)
# ----------------------------------------------------------------------------------
# 逻辑混淆替换
title = "c82"  # 语言选择页title
txt_language = "ctq"  # 语言选择页语言项
iv_close = "ak0"  # TVC弹窗关闭按钮
tab_animation_view = "c5n"  # Moment/Party/Sing/Message/Me
# ----------------------------------------------------------------------------------
C = 0
TimeEnd_List = []
Count_List = []
Data_Name_List = []
print("测试开始")
while (C < run_number):    
    # -----setUp-----
    # 启动app
    start_app(package_name)
    sleep(10)
    poco(package_name + ":id/" + title).wait_for_appearance()
    
    # 选择语言页——选择英语
    poco(package_name + ":id/" + txt_language)[1].click()
    sleep(3)
    
    # 处理TVC弹窗
    poco(package_name + ":id/" + iv_close).click()
    sleep(3)
    
    # 点击Moment Tab
    poco("main_tab_trend").click()
    sleep(5)
    
    # 点击开始录制
    touch((395,99))
    

    # -----测试脚本-----
    A = 0
    Count = 0
    print("测试开始")
    time_start = time.time()
    while (A < single_run_time):
        try:
            swipe((360,1050),(360,90))
            sleep(2)
            Count += 1
        except:
            pass
        finally:
            time_end = time.time()
            A = time_end - time_start
            print(A)
    print("脚本结束共滑动次数")
    print(Count)
    Count_List.append(Count)
    
    # -----tearDown-----
    # 点击暂停录制
    touch((395,99))
    sleep(2)
    
    # 记录数据结果文件名
    data_name = poco("android:id/message").get_text()
    sleep(2)
    print(data_name)
    Data_Name_List.append(data_name)
    
    # 点击数据结果弹窗的"确定"按钮
    poco("android:id/button1").click()
    sleep(2)
    
    # 清理app
    clear_app(package_name)
    sleep(5)

    C = C + 1
    T = time.strftime('%H.%M.%S',time.localtime(time.time()))
    print("执行次数")
    print(C)
    print("结束时间")
    print(T)
    TimeEnd_List.append(T)
print("批次结束时间列表")
print(TimeEnd_List)
print("滑动次数列表")
print(Count_List)
print("数据文件名列表")
print(Data_Name_List)
print("测试结束")







