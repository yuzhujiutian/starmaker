# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

dev = connect_device("android:///")
devs = device()


# video_marker = True  # False=recording/True=video
# cover = "com.starmakerinteractive.starmaker:id/ayc"
package_name = "com.starmakerinteractive.starmaker"
clear_app(package_name)
# iv_video = "av2"
# for i in range(1,6):
#     print("-----")
#     print(i)
#     if poco(cover)[i].child(package_name + ":id/" + iv_video).exists() == video_marker:
#         if video_marker:
#             print("video")
#         else:
#             print("record")
#         poco(cover)[i].click()

    
    
# b = poco(cover)[1].child(package_name + ":id/" + iv_video).exists()
# print(b)
# print("-----")
# c = poco(package_name + ":id/" + iv_video).exists()
# print(c)



