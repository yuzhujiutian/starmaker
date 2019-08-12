# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 点击个人页
poco("com.starmakerinteractive.thevoice:id/arn").child("android.widget.LinearLayout").child("android.support.v7.app.a$c")[4].child("android.widget.FrameLayout").child("android.widget.ImageView").click()
# 点击邮箱登陆
poco("com.starmakerinteractive.thevoice:id/a3p").click()
# 点击Log In
poco(text="Log In").click()
sleep(1.0)
# 输入帐号
text("cyl@22.cn")
# 点击密码输入框
poco("com.starmakerinteractive.thevoice:id/sk").child("android.widget.RelativeLayout").child("com.starmakerinteractive.thevoice:id/afa").child("com.starmakerinteractive.thevoice:id/af9").child("android.widget.FrameLayout").child("com.starmakerinteractive.thevoice:id/sm").click()
# 输入密码
text("000000")
# 点击登陆
poco("com.starmakerinteractive.thevoice:id/j5").click()
sleep(3.0)
if wait(Template(r"tpl1542181833632.png", record_pos=(-0.116, 0.163), resolution=(1440, 2560)),timeout=40):
    print("ok")
touch(Template(r"tpl1542182005575.png", record_pos=(0.004, -0.244), resolution=(1440, 2560)),duration=3)


