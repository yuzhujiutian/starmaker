# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"

from airtest.core.api import *

auto_setup(__file__)
# ----- 以上为初始化默认填入 -----

# 一、连接设备
#   1.使用默认参数连接本地adb设备
connect_device("android:///")
#   2.连接指定设备，当连接了多台设备或有远程设备时，使用该方法(<number> = Android 设备序列号)
connect_device("android://adbhost:adbport/<number>?cap_method=javacap&touch_method=adb")

# 二、安装待测APK
install("C:/Users/cucumber/Desktop/7.2.4 thevoiceDebug-minApi21-armeabi-v7a (1).apk")

# 三、启动APP
#   "adb logcat | findstr Displayed"查看当前运行app package/activity
start_app(package="com.starmakerinteractive.thevoice",activity="com.ushowmedia.starmaker.activity.SplashActivity")

from airtest.cpre.android.android import module
path_app("com.starmakerinteractive.thevoice")

# 四、用例+断言
pass

# 五、删除APK
home()
package_name = "com.starmakerinteractive.thevoice"
uninstall(package_name)

# 六、API支持
#   1.airtest.core.android package
    "https://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.android.html"
#   2.airtest.core.api module
    "https://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.api.html"