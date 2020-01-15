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
package_name = "com.horadrim.android.sargam"
clear_app(package_name)
sleep(4)
# ----------------------------------------------------------------------------------
# 逻辑混淆替换
title = "c8x"  # 语言选择页title
txt_language = "cv7"  # 语言选择页语言项
iv_close = "akf"  # TVC弹窗关闭按钮

tv_more_ways = "cif"  # More ways登录方式
tv_login_email  = "chi"  # Email登录按钮
et_email = "xg"  # Email帐号输入框
btn_next = "jc"  # Next按钮
et_input = "xk"  # 密码输入框
btw_email_confirm = "ke"  # LOG IN按钮

iv_new_entrance_profile = "ao8"  # 个人页songs入口
btn_action = "i9"  # songs页面Sing按钮
item_play_detail_dialog_text = "ahu"  # 录制类型弹窗的选项Solo/Join Duet/Start Duet/Chorus
permissionOkTv = "bha"  # 录制权限申请弹窗按钮
recording_headset_dialog_i_know_btn = "bq_"  # 耳机引导弹窗
tv_pitch_guide_tip = "ckc"  # Pitch引导
media_type_chb = "b_z"  # 录制类型切换
record_btn = "bpp"  # Start开始录制按钮
record_time_tv = "bq7"  # 录制剩余时长
btn_post = "ji"  # 预览页Post按钮
btn_next  = "jc"  # 发布页Send按钮
tv_done = "cdm"  # 结果页Done按钮
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
    sleep(5)

    # 处理TVC弹窗
    poco(package_name + ":id/" + iv_close).click()
    sleep(3)

    # 点击Me Tab
    poco("main_tab_me").click()
    sleep(3)

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
        
    # 点击个人页歌曲入口
    poco(package_name + ":id/" + iv_new_entrance_profile)[1].click()
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
        poco(package_name + ":id/" + btn_action)[0].click()
        sleep(3)

        # 点击录制类型弹窗的Solo
        poco(package_name + ":id/" + item_play_detail_dialog_text)[0].click()
        sleep(3)

        # 同意权限弹窗
        if poco(package_name + ":id/" + permissionOkTv):
            poco(package_name + ":id/" + permissionOkTv).click()
            sleep(2)
            poco("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(2)
            poco("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(2)
            poco("com.android.packageinstaller:id/permission_allow_button").click()
            sleep(2)

        # 点击耳机引导弹窗
        poco(package_name + ":id/" + recording_headset_dialog_i_know_btn).click()
        sleep(2)

        # 处理Pitch引导
        if poco(package_name + ":id/" + tv_pitch_guide_tip):
            poco(package_name + ":id/" + tv_pitch_guide_tip).click()
            sleep(3)

        # 点击切换视频录制
        if Count == 0:
            poco(package_name + ":id/" + media_type_chb).click()  
            sleep(5)

        # 点击Start录制按钮
        poco(package_name + ":id/" + record_btn).click()
        sleep(8)

        # 获取剩余录制时间
        song_duration = poco(package_name + ":id/" + record_time_tv).get_text()
        seconds = int(song_duration[:2]) * 60 + int(song_duration[3:5]) + 10
        print("本首歌曲剩余录制时长为")
        print(seconds)

        # 等待歌曲录制完成
        sleep(seconds)
        sleep(8)

        try:
            # 点击预览页post按钮
            poco(package_name + ":id/" + btn_post).click()
            sleep(8)
        except:
            touch((578,1215))
            

        # 点击发布页Send按钮
        poco(package_name + ":id/" + btn_next).click()
        sleep(8)

        # 点击结果页Done按钮
        poco(package_name + ":id/" + tv_done).click()
        sleep(8)

        Count += 1
        
        sleep(30)
        
        if Count < songs_run_num:
            # 点击Me Tab
            poco("main_tab_me").click()
            sleep(5)

            # 点击个人页歌曲入口
            poco(package_name + ":id/" + iv_new_entrance_profile)[1].click()
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






