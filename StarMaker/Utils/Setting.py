# coding=utf-8

# IP/端口
desired_IP = 4721

# 配置信息
PlatformName = "Android"
# uiautomator2 仅可以使用Android 5.0以上；5.0以下需要使用appium
AutomationName = "appium"
# AutomationName = "uiautomator2"
AutoGrantPermissions = True
UnicodeKeyboard = True
ResetKeyboard = True
NoReset = True
AppActivity = "com.ushowmedia.starmaker.activity.SplashActivity"

# 设备信息(数据来源：GetDevicesInfo)
DeviceCount = 2
PlatformVersion = ['5.1', '4.3']
Device = ['OPPO_A53m', 'SM_N9005']
DeviceName = ['A53m', 'hlte']
