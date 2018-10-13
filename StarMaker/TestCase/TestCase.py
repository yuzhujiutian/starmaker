# coding=utf-8
import time
from Utils.Tools import RegionalSliding, Screen
from Utils.GetAppiumDeriver import GetAppiumDeriver
from CommonView.Home import Home


def test():
    a = GetAppiumDeriver().driver
    time.sleep(20)
    mode = a.find_elements_by_class_name("android.widget.TextView")
    TextList = []
    for index in range(len(mode)):
        TextList.append(mode[index].text)
    if len(mode) == 3 and TextList == ['Solo', 'Join Collab', 'Start Collab']:
        print("不支持Chorus")
    elif len(mode) == 4 and TextList == ['Solo', 'Join Collab', 'Start Collab', 'Chorus']:
        print("支持Chorus")



if __name__ == '__main__':
    test()


