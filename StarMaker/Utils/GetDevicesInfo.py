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
            # 检查已连接设备数
            global deviceCount
            deviceCount = len(self.deviceInfo)-3
            # 如果没有连接设备或设备读取失败
            if deviceCount == 0:
                self.GetDevicesInfo = 0
            elif deviceCount == 1:
                self.GetDevicesInfo = 1
            else:
                self.GetDevicesInfo = deviceCount
            # print("当前已连接设备数:" + str(deviceCount))
            # 过滤deviceInfo
            deviceList = []
            for i in self.deviceInfo:
                if i != "List of devices attached " and i:
                    # rstrip() 为去掉字符串中的空格
                    i = i[:-6].rstrip()
                    deviceList.append(i)
            # 设备序列号
            self.serialNumbers = deviceList
        # 捕获异常
        except Exception as e:
            print("Device Connect Fail:", e)

    # 获取系统、设备信息
    def GetAndroidVersion(self):
        try:
            if self.GetDevicesInfo == 1:
                # 获取系统设备信息，并将比特流类型转为str类型：decode
                sysInfo = subprocess.check_output("adb shell cat /system/build.prop").decode("utf-8", "ignore")
                # 获取Android版本号
                androidVersion = re.findall("version.release=(\\d\\.\\d)", sysInfo, re.S)[0]
                return androidVersion
            elif self.GetDevicesInfo > 1:
                devicesCount = self.GetDevicesInfo
                androidVersion = []
                while devicesCount:
                    devicesCount -= 1
                    # 获取系统设备信息，并将比特流类型转为str类型：decode
                    serialNumber = self.serialNumbers
                    sysInfo = subprocess.check_output("adb -s %s shell cat /system/build.prop" % serialNumber[devicesCount]).decode("utf-8", "ignore")
                    # 获取Android版本号
                    androidVersion.insert(0, re.findall("version.release=(\\d\\.\\d)", sysInfo, re.S)[0])
                    if not devicesCount:
                        return androidVersion
            else:
                return "Connect Fail,Please reconnect Device..."
        # 捕获异常
        except Exception as e:
            print("Get Android Version:", e)

    # 获取设备型号
    def GetDevice(self):
        try:
            if self.GetDevicesInfo == 1:
                # 获取设备型号
                deviceInfo = subprocess.check_output("adb devices -l").decode("utf-8", "ignore")
                deviceModel = re.findall(r"model:(.*)\sdevice", deviceInfo, re.S)[0]
                return deviceModel
            elif self.GetDevicesInfo > 1:
                # 获取设备型号
                deviceInfo = subprocess.check_output("adb devices -l").decode("utf-8", "ignore")[27:]
                deviceModels = [i[6:] for i in deviceInfo.split(" ") if "model:" in i]
                return deviceModels
            else:
                return "Connect Fail,Please reconnect Device..."
        # 捕获异常
        except Exception as e:
            print("Get Device:", e)

    # 获取设备名
    def GetDeviceName(self):
        try:
            if self.GetDevicesInfo == 1:
                # 获取设备名
                deviceInfo = subprocess.check_output("adb devices -l").decode("utf-8", "ignore")
                deviceName = re.findall(r"device:(.*)", deviceInfo, re.S)[0]
                return deviceName
            elif self.GetDevicesInfo > 1:
                # 获取设备名
                deviceInfo = subprocess.check_output("adb devices -l").decode("utf-8", "ignore")[27:]
                deviceName_list = [i[7:].strip(" ") for i in deviceInfo.split(" ") if "device:" in i]
                deviceName = []
                for i in deviceName_list:
                    deviceName.append(re.findall(r"(.*)\r\n", i, re.S)[0].strip())
                return deviceName
            else:
                return "Connect Fail,Please reconnect Device..."
        # 捕获异常
        except Exception as e:
            print("Get Device Name:", e)

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


class DevicesInfo(object):
    # AppPackage 用于初始化
    @staticmethod
    def AppPackage():
        # GetPackages = GetDevicesInfo().GetPackages()[0]
        # 调试使用
        GetPackages = "com.ushow.android.jalebee"
        return GetPackages

    # package拼接 用于元素定位使用
    @staticmethod
    def package():
        setUp_package = DevicesInfo().AppPackage()
        element_package = "%s:id/" % setUp_package
        return element_package

if __name__ == '__main__':
    print("将以下信息复制到Utils/Setting下")
    print("DeviceCount = " + str(len(GetDevicesInfo().GetAndroidVersion())))
    print("PlatformVersion = " + str(GetDevicesInfo().GetAndroidVersion()))
    print("Device = " + str(GetDevicesInfo().GetDevice()))
    print("DeviceName = " + str(GetDevicesInfo().GetDeviceName()))




