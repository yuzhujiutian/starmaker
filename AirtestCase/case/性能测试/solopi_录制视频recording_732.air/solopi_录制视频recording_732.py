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
songs_run_num = 2
# 3>测试package name
package_name = "com.starmakerinteractive.starmaker"
clear_app(package_name)
sleep(4)
# ----------------------------------------------------------------------------------
# 逻辑混淆替换


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
    poco("com.starmakerinteractive.starmaker:id/c0y").wait_for_appearance()

    # 选择语言页——选择英语
    poco("com.starmakerinteractive.starmaker:id/cki")[1].click()
    sleep(5)

    # 处理TVC弹窗
    poco("com.starmakerinteractive.starmaker:id/afo").click()
    sleep(3)

    # 点击Me Tab
    poco("main_tab_me").click()
    sleep(3)

    # 点击More ways
    poco("com.starmakerinteractive.starmaker:id/c_b").click()
    sleep(3)

    # 点击Email登录方式
    poco("com.starmakerinteractive.starmaker:id/aim").click()
    sleep(3)
    
    poco("com.starmakerinteractive.starmaker:id/ckp").click()
    sleep(3)

    # 输入测试邮箱/密码
    poco("com.starmakerinteractive.starmaker:id/vc")[0].set_text("cyl@20.cn")
    sleep(2)
    poco("com.starmakerinteractive.starmaker:id/vc")[1].set_text("000000")
    sleep(2)

    # 点击LOG IN按钮
    poco("com.starmakerinteractive.starmaker:id/ja").click()
    sleep(8)
        
    # 点击个人页歌曲入口
    poco("com.starmakerinteractive.starmaker:id/aja")[1].click()
    sleep(5)
    
    # 点击开始录制
    touch((395,99))
    sleep(2)
    touch((55,100))
    sleep(2)
    

    # -----测试脚本-----
    Count = 0
    print("测试开始")
    while (Count < songs_run_num):
        # 点击第一首歌曲的SING按钮
        poco(package_name + ":id/ha")[0].click()
        sleep(3)

        # 点击录制类型弹窗的Solo
        poco(package_name + ":id/adg")[0].click()
        sleep(3)

        # 同意权限弹窗
        if poco(package_name + ":id/baa"):
            poco(package_name + ":id/baa").click()
            sleep(2)
            poco("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(2)
            poco("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(2)
            poco("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(2)

        # 点击耳机引导弹窗
        poco(package_name + ":id/bix").click()
        sleep(2)

        # 处理Pitch引导
        if poco(package_name + ":id/cb0"):
            poco(package_name + ":id/cb0").click()
            sleep(3)

        # 点击切换视频录制
        if Count == 0:
            poco("com.starmakerinteractive.starmaker:id/b44").click()
            sleep(8)

        # 点击Start录制按钮
        poco(package_name + ":id/bic").click()
        sleep(8)

        # 获取剩余录制时间
        song_duration = poco(package_name + ":id/biu").get_text()
        seconds = int(song_duration[:2]) * 60 + int(song_duration[3:5]) + 10
        print("本首歌曲剩余录制时长为")
        print(seconds)

        # 等待歌曲录制完成
        sleep(seconds)
        sleep(8)

        # 点击预览页post按钮
        poco(package_name + ":id/ig").click()
        sleep(8)

        # 点击发布页Send按钮
        poco(package_name + ":id/ia").click()
        sleep(8)

        # 点击结果页Done按钮
        poco(package_name + ":id/c5u").click()
        sleep(8)

        Count += 1
        
        sleep(30)
        
        if Count < songs_run_num:
            # 点击Me Tab
            poco("main_tab_me").click()
            sleep(5)

            # 点击个人页歌曲入口
            poco("com.starmakerinteractive.starmaker:id/aja")[1].click()
            sleep(5)
        else:
            sleep(10)
            
    print("脚本结束共录制视频recording次数")
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






