# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"

from airtest.core.api import *
from airtest.core.api import using
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

using("reSource.air")
from reSource import get_mapping_from_file
from reSource import get_package_name
mapping_dict = get_mapping_from_file()
packages = get_package_name()
package_name = packages["sm"]
dev = connect_device("android:///")
devs = device()
# ----------------------------------------------------------------------------------
# 逻辑混淆替换
title = mapping_dict["title"]  # 语言选择页title
txt_language_english = mapping_dict["txt_language_english"]  # 语言选择页语言项
iv_close = mapping_dict["iv_close"]  # TVC弹窗关闭按钮
tv_content = mapping_dict["tv_content"]  # feed流无内容缺省提示"No More Data"
tv_more_ways = mapping_dict["tv_more_ways"]  # More ways登录方式
tv_login_email = mapping_dict["tv_login_email"]  # Email登录按钮
et_email = mapping_dict["et_email"]  # Email帐号输入框
btn_next = mapping_dict["btn_next"]  # Next按钮
et_input = mapping_dict["et_input"]  # 密码输入框
btw_email_confirm = mapping_dict["btw_email_confirm"]  # LOG IN按钮
iv_new_entrance_profile = mapping_dict["iv_new_entrance_profile"]  # 个人页songs入口
btn_action = mapping_dict["btn_action"]  # songs页面Sing按钮
item_play_detail_dialog_text = mapping_dict["item_play_detail_dialog_text"]  # 录制类型弹窗的选项Solo/Join Duet/Start Duet/Chorus
permissionOkTv = mapping_dict["permissionOkTv"]  # 录制权限申请弹窗按钮
recording_headset_dialog_i_know_btn = mapping_dict["recording_headset_dialog_i_know_btn"]  # 耳机引导弹窗
tv_pitch_guide_tip = mapping_dict["tv_pitch_guide_tip"]  # Pitch引导
iv_camera_switchover_recorder_song_fragment_song_record = mapping_dict["iv_camera_switchover_recorder_song_fragment_song_record"]  # 录制类型切换
rbtn_record_recorder_song_fragment_song_record = mapping_dict["rbtn_record_recorder_song_fragment_song_record"]  # Start开始录制按钮
record_time_tv = mapping_dict["record_time_tv"]  # 录制剩余时长
tv_next_baserecord_fragment_edit = mapping_dict["tv_next_baserecord_fragment_edit"]  # 预览页Post按钮
btn_next = mapping_dict["btn_next"]  # 发布页Send按钮
tv_done = mapping_dict["tv_done"]  # 结果页Done按钮
# ----------------------------------------------------------------------------------
auto_setup(__file__)


# print("测试开始")
def record_video(run_number = 5, songs_run_num = 2):
    C = 0
    TimeEnd_List = []
    Data_Name_List = []
    clear_app(package_name)
    sleep(4)
    while (C < run_number):    
        # -----setUp-----
        # 启动app
        start_app(package_name)
        sleep(10)
        poco(package_name + ":id/" + title).wait_for_appearance()

        # 选择语言页——选择英语
        poco(package_name + ":id/" + txt_language_english)[0].click()
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
        try:
            test_case(songs_run_num)
        except:
            print("something is error")

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
#         print("执行次数")
#         print(C)
#         print("结束时间")
#         print(T)
        TimeEnd_List.append(T)
#     print("批次结束时间列表")
#     print(TimeEnd_List)
#     print("数据文件名列表")
#     print(Data_Name_List)
    print("录制视频recording 测试结束")
    
    return Data_Name_List

    
def test_case(songs_run_num):
        Count = 0
#         print("run test_case")
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
            sleep(10)

            poco(package_name + ":id/" + iv_camera_switchover_recorder_song_fragment_song_record).click()  
            sleep(10)

            # 点击Start录制按钮
            poco(package_name + ":id/" + rbtn_record_recorder_song_fragment_song_record).click()
            sleep(240)
            sleep(8)

            try:
                # 点击预览页post按钮
                poco(package_name + ":id/" + tv_next_baserecord_fragment_edit).click()
                sleep(8)
            except:
                touch((578,1215))

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








