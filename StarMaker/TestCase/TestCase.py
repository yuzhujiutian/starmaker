# coding=utf-8
import time
from Utils.Tools import RegionalSliding, Screen
from Utils.GetAppiumDeriver import GetAppiumDeriver
from CommonView.Home import Home


def test():
    a = GetAppiumDeriver().driver
    time.sleep(5)
    Home().HomeTab_Profile().click()
    time.sleep(2)
    b = a.find_element_by_id("com.starmakerinteractive.starmaker:id/new_entrance_layout")
    print("滑动前")
    time.sleep(3)
    RegionalSliding(b).Transverse()
    print("滑动后")
    time.sleep(3)
    Screen().DIYSwipe_Percentage(0.5, 0.75, 0.5, 0.5, 500)
    d = a.find_element_by_id("com.starmakerinteractive.starmaker:id/vtb_pager")
    print("滑动前")
    time.sleep(3)
    RegionalSliding(d).Transverse()
    print("滑动后")
    time.sleep(3)


if __name__ == '__main__':
    test()


