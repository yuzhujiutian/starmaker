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
# 4>测试类型
video_marker = True  # False=recording/True=video

clear_app(package_name)
sleep(5)
# ----------------------------------------------------------------------------------
# 逻辑混淆替换
title = "ca6"  # 语言选择页title
txt_language = "cy0"  # 语言选择页语言项
iv_close = "ala"  # TVC弹窗关闭按钮

tv_more_ways = "cl0"  # More ways登录方式
tv_login_email  = "ck2"  # Email登录按钮
et_email = "xv"  # Email帐号输入框
btn_next = "ji"  # Next按钮
et_input = "xz"  # 密码输入框
btw_email_confirm = "kl"  # LOG IN按钮

layout_music_parent = "avw"  # popular作品
iv_video = "asq"  # 作品cover左上角video标识
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
    
    # 测试recording需要登录
    if video_marker is False:
        # 点击Me Tab
        poco("main_tab_me").click()
        sleep(5)
        
        # 点击More ways
        poco(package_name + ":id/" + tv_more_ways).click()
        sleep(3)

        # 点击Email登录方式
        poco(package_name + ":id/" + tv_login_email).click()
        sleep(3)

        # 输入测试邮箱
        poco(package_name + ":id/" + et_email)[0].set_text("cyl@20.cn")
        sleep(2)

        # 点击Next按钮
        poco(package_name + ":id/" + btn_next).click()
        sleep(3)

        # 输入密码
        poco(package_name + ":id/" + et_input)[1].set_text("000000")
        sleep(2)

        # 点击LOG IN按钮
        poco(package_name + ":id/" + btw_email_confirm).click()
        sleep(8)
    
    # 点击Moment Tab
    poco("main_tab_trend").click()
    sleep(5)
    
    # 点击开始录制
    touch((395,99))
    sleep(2)
    touch((55,100))
    sleep(2)
    

    # -----测试脚本-----
    A = 0
    Count = 0
    print("测试开始")
    time_start = time.time()
    while (A < single_run_time):
        try:
            swipe((360,1050),(360,90))
            cover = poco(package_name + ":id/" + layout_music_parent)
            for i in range(2,6):
# ----------------------------------------------------------------------------------
                # 如果是recording/video则点击
                if cover[i].child(package_name + ":id/" + iv_video).exists() == video_marker:
                    if video_marker:
                        print("video")
                    else:
                        print("record")
                    cover[i].click()
                    # 播放5秒
                    sleep(5)
                    # 返回到feed流
                    keyevent("KEYCODE_BACK")
                    sleep(5)
                    Count += 1
                    break
# ----------------------------------------------------------------------------------
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
    touch((28,80))
    sleep(2)
    touch((395,99))
    sleep(5)
    
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




