# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
import time
from airtest.core.api import *
from airtest.core.api import using
from airtest.core.android.android import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

using("reSource.air")
from reSource import get_mapping_from_file
from reSource import get_package_name
mapping_dict = get_mapping_from_file()
packages = get_package_name()
package_name = packages["sa"]
dev = connect_device("android:///")
devs = device()
# ----------------------------------------------------------------------------------
# 逻辑混淆替换
title = mapping_dict["title"]  # 语言选择页title
txt_language_english = mapping_dict["txt_language_english"]  # 语言选择页语言项
iv_close = mapping_dict["iv_close"]  # TVC弹窗关闭按钮
tv_content = mapping_dict["tv_content"]  # feed流无内容缺省提示"No More Data"
# ----------------------------------------------------------------------------------
auto_setup(__file__)


# print("测试开始")
def feed_browse(run_number = 5, single_run_time = 600):
    C = 0
    language_index = 0  # 初始语言
    language_list = []
    TimeEnd_List = []
    Count_List = []
    Data_Name_List = []
    # 清理app
    clear_app(package_name)
    sleep(4)
    while (C < run_number):    
        # -----setUp-----
        # 隐藏性能浮窗
        touch((55,100))
        sleep(2)

        # 启动app
        start_app(package_name)
        sleep(10)
        poco(package_name + ":id/" + title).wait_for_appearance()

        # 预期本次使用语言
        language = poco(package_name + ":id/" + txt_language_english)[language_index].get_text()
#         print(language)
        sleep(3)

        # 选择语言页——选择语言
        poco(package_name + ":id/" + txt_language_english)[language_index].click()
        sleep(3)

        # 处理TVC弹窗
        poco(package_name + ":id/" + iv_close).click()
        sleep(3)

        # 点击Moment Tab
        poco("main_tab_trend").click()
        sleep(5)

        # 点击开始录制
        touch((55,100))
        sleep(2)
        touch((395,99))
        sleep(2)
        touch((55,100))
        sleep(2)


        # -----测试脚本-----
        try:
            test_case(single_run_time)
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

        # 如果数据量足够，则记录数据
        if poco(package_name + ":id/" + tv_content).exists() == False:
            C = C + 1
            T = time.strftime('%H.%M.%S',time.localtime(time.time()))
#             print("执行次数")
#             print(C)
#             print("结束时间")
#             print(T)
#             print("使用语言")
#             print(language)
            
            TimeEnd_List.append(T)
            language_list.append(language)

        # 否则
        elif poco(package_name + ":id/" + tv_content).exists() == True:
            # 更换语言
            language_index += 1
            print("No More Data,Trying again")

        # 清理app
        clear_app(package_name)
        sleep(5)


    
#     print("批次结束时间列表")
#     print(TimeEnd_List)
#     print("数据文件名列表")
#     print(Data_Name_List)
#     print("内容语言列表")
#     print(language_list)
#     print("feed浏览 测试结束")
    
    return Data_Name_List


def test_case(single_run_time):
    A = 0
    Count = 0
#     print("run test_case")
    time_start = time.time()
    while (A < single_run_time):
        try:
            swipe((360,1050),(360,90))
            sleep(2)
            Count += 1
        except:
            print("something is error,in ‘test_case’")
        finally:
            time_end = time.time()
            A = time_end - time_start
            print(A)
    





