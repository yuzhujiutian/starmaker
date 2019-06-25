# coding=utf-8
import time

from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver
from StarMaker.Utils.GetDevicesInfo import DevicesInfo

# 启动
driver = GetAppiumDeriver().driver
driver.wait_activity("com.ushowmedia.starmaker.activity.MainActivity", 20)
# package
package = DevicesInfo().AppPackage()
CPUInfo_List = []
MemoryInfo_List = []
BatteryInfo_List = []
NetWorkInfo_List = []

# CPU、内存、电池、网络
# ['cpuinfo', 'memoryinfo', 'batteryinfo', 'networkinfo']
# types_list = driver.get_performance_data_types()
# print(types_list)
num = 0
while num < 3:
    num += 1
    try:
        print("第 %s 次数据" % num)
        print("-----cpu-----""\n")
        cpu_info = driver.get_performance_data(package, "cpuinfo", 5)
        print(cpu_info)
        CPUInfo_List.append(cpu_info)
        print("-----memory-----""\n")
        memory_info = driver.get_performance_data(package, "memoryinfo")
        print(memory_info)
        MemoryInfo_List.append(memory_info)
        print("-----battery-----""\n")
        battery_info = driver.get_performance_data(package, "batteryinfo")
        print(battery_info)
        BatteryInfo_List.append(battery_info)
        print("-----network-----""\n")
        network_info = driver.get_performance_data(package, "networkinfo")
        print(network_info)
        NetWorkInfo_List.append(network_info)

        time.sleep(10)
    except Exception as e:
        print(e)
print("结束")
print("----------""\n")
print(CPUInfo_List)
print("----------""\n")
print(MemoryInfo_List)
print("----------""\n")
print(BatteryInfo_List)
print("----------""\n")
print(NetWorkInfo_List)

driver.quit()




# CPUInfo_List = [[['user', 'kernel'], ['0', '0']], [['user', 'kernel'], ['53', '13']], [['user', 'kernel'], ['78', '22']]]
# m = CPUInfo_List
# totalPssIndex = m[0].index('totalPss')
#
# startMemory = CPUInfo_List[0][1][totalPssIndex]
# endMemory = CPUInfo_List[-1][1][totalPssIndex]
#
# totalMemory = 0
# maxMemory = 0
# for m in CPUInfo_List[1:-1]:
#     c = int(m[1][totalPssIndex])
#     totalMemory += c
#     if c > maxMemory:
#         maxMemory = c
#
# averageMemory = totalMemory/(len(CPUInfo_List) - 2)
#
# print('startMemory:', startMemory)
# print('endMemory:', endMemory)
# print('averageMemory:', averageMemory)
# print('maxMemory:', maxMemory)


if __name__ == '__main__':
    pass
