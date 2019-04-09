# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
touch(Template(r"tpl1542077116300.png", record_pos=(-0.406, 0.811), resolution=(1440, 2560)))

poco("com.starmakerinteractive.thevoice:id/bk2").click()
poco("com.starmakerinteractive.thevoice:id/bhq").swipe([0.0588, -0.943])
touch(Template(r"tpl1542077300766.png", record_pos=(0.006, 0.817), resolution=(1440, 2560)))
assert_exists(Template(r"tpl1542077252072.png", record_pos=(-0.438, 0.784), resolution=(1440, 2560)), "点击comment,输入栏左边显示评论者头像")
poco("com.starmakerinteractive.thevoice:id/ow").click()
poco("com.starmakerinteractive.thevoice:id/b9i").child("android.widget.RelativeLayout")[0].child("android.widget.LinearLayout").child("com.starmakerinteractive.thevoice:id/an_").child("com.starmakerinteractive.thevoice:id/ac4").click()
assert_exists(Template(r"tpl1542077252072.png", record_pos=(-0.438, 0.784), resolution=(1440, 2560)), "点击A用户的comment评论进行回复,输入栏左边显示评论者头像")
poco("com.starmakerinteractive.thevoice:id/ow").click()




