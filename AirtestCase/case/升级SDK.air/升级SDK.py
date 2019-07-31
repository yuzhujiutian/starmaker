# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"

from airtest.core.android.android import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# ----- 初始化 -----
# 连接设备
dev = connect_device("android:///")
devs = device()
# 安装包
install("C:/Users/cucumber/Desktop/thevoiceRelease-minApi21-armeabi-v7a-82727000-2018-11-30-02-25.apk")
# 启动app
start_app("com.starmakerinteractive.thevoice")
sleep(5)
# ----- 用例部分 -----
# 选择语言
poco(text="हिन्दी").click()
sleep(5)

count = 0
picture = 0
video = 0
while (count < 300):
    swipe((360,1088),(360,92))
    try:
        # 图片
        poco(FindSource("y5")).click()
        poco("com.starmakerinteractive.thevoice:id/y5").click()
        sleep(2)
        keyevent("BACK")
        picture = picture + 1
    except:
        try:
            # 视屏
            poco("com.starmakerinteractive.thevoice:id/aa6").click()
            sleep(5)
            keyevent("BACK")
            video = video + 1
        # 其他错误忽略(此处可能遇到屏幕中仅有一个广告，忽略错误后继续执行滑动)
        except:
            pass  
    finally:
        # 划掉已消费内容
        swipe((360,1088),(360,92))
        sleep(1)
        # 尝试次数+1
        count = count + 1
        # 打印测试数据统计
        print("图片",picture)
        print("视频",video)
        print("尝试次数",count)
        print("----------")
        
        # 异常处理以及脚本恢复
        # 数据校验：如果图片+视屏比尝试次数少
        if picture + video < count:
            # 截图，用于人工定位问题
            snapshot(msg="feed流内容错误.")
            try:
                # 尝试关闭app，重新打开
                stop_app("com.starmakerinteractive.thevoice")
                start_app("com.starmakerinteractive.thevoice")
                sleep(5)
                # 如果关闭/打开错误，则卸载重装
            except:
                uninstall("com.starmakerinteractive.thevoice")
                install("com.starmakerinteractive.thevoice")
                start_app("com.starmakerinteractive.thevoice")
                # 选择语言
                poco(text="हिन्दी").click()
                

        


        
        

# ----- 结束清理 -----

# 清除数据
# Android().clear_app("com.starmakerinteractive.thevoice")
# 卸载包
# uninstall("com.starmakerinteractive.thevoice")
