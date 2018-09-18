# coding=utf-8
import re
import subprocess
from Utils.Common import singleton
# ----------
# 自动获取工具
# ----------


@singleton
class GetDevicesInfo(object):
    # 检查设备是否连接成功，如果成功返回True，否则返回False
    def __init__(self):
        # 检查设备连接状态
        try:
            # 获取设备列表信息，并将比特流类型转为str类型：decode，并用‘\r\n’拆分,
            self.deviceInfo = subprocess.check_output("adb devices").decode("utf-8", "ignore").split("\r\n")
            # 如果没有连接设备或设备读取失败，则第二个元素为空
            if self.deviceInfo[1] is not None:
                self.GetDevicesInfo = True
            else:
                self.GetDevicesInfo = False
        # 捕获异常
        except Exception as e:
            print("Device Connect Fail:", e)

    # 获取系统、设备信息

    def GetAndroidVersion(self):
        try:
            if self.GetDevicesInfo:
                # 获取系统设备信息，并将比特流类型转为str类型：decode
                # sysInfo = subprocess.check_output(str(os.system("adb shell cat /system/build.prop"))).decode()
                sysInfo = subprocess.check_output("adb shell cat /system/build.prop").decode("utf-8", "ignore")
                # 获取Android版本号
                androidVersion = re.findall("version.release=(\d\.\d)", sysInfo, re.S)[0]
                return androidVersion
            else:
                return "Connect Fail,Please reconnect Device..."
        # 捕获异常
        except Exception as e:
            print("Get Android Version:", e)

    # 获取设备名
    def GetDeviceName(self):
        try:
            if self.GetDevicesInfo:
                # 获取设备名
                # deviceInfo = subprocess.check_output(str(os.system("adb devices -l"))).decode("utf-8", "ignore")
                deviceInfo = subprocess.check_output("adb devices -l").decode("utf-8", "ignore")
                deviceName = re.findall(r"device product:(.*)\smodel", deviceInfo, re.S)[0]
                return deviceName
            else:
                return "Connect Fail,Please reconnect Device..."
        # 捕获异常
        except Exception as e:
            print("Get Device Name:", e)

    # 获取设备型号，用于报告中描述问题来源
    def GetDevice(self):
        try:
            if self.GetDevicesInfo:
                # 获取Android版本号
                deviceInfo = subprocess.check_output("adb devices -l").decode("utf-8", "ignore")
                deviceModel = re.findall(r"model:(.*)\sdevice", deviceInfo, re.S)[0]
                return deviceModel
            else:
                return "Connect Fail,Please reconnect Device..."
        # 捕获异常
        except Exception as e:
            print("Get Device:", e)

    # 获取当前设备已安装包名
    def GetPackages(self):
        # sm:com.starmakerinteractive.starmaker
        # tvp:com.starmakerinteractive.thevoice
        # sa:com.horadrim.android.sargam
        # su:com.windforce.android.suaraku
        try:
            if self.GetDevicesInfo:
                all_packages = subprocess.check_output("adb shell pm list packages").decode("utf-8", "ignore")
                list_packages = re.findall(r"package:(.*)", all_packages, re.S)[0]
                our_packages = ["com.starmakerinteractive.starmaker", "com.starmakerinteractive.thevoice",
                                "com.horadrim.android.sargam", "com.windforce.android.suaraku"]
                f = [c for c in our_packages if c in list_packages]
                if len(f):
                    return f  # AppPackage = "com.starmakerinteractive.starmaker"
                else:
                    return "当前设备未安装sm/tvp/sa/su..."
            else:
                return "Connect Fail,Please reconnect Device..."
        except Exception as e:
            print("GetPackages:", e)


# if __name__ == '__main__':
#     print(GetDevicesInfo().GetAndroidVersion())
#     print(GetDevicesInfo().GetDeviceName())
#     print(GetDevicesInfo().GetDevice())
#     print(GetDevicesInfo().GetPackages()[0])



