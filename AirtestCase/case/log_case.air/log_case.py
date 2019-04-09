# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"


图像识别：唯一且固定
元素识别：位置不变内容变




from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
keyevent("BACK")
keyevent("POWER")
poco("com.android.systemui:id/keyguard_indication_text").click()
poco("com.android.systemui:id/keyguard_indication_text").swipe([-0.0067, -0.3934])
poco("com.android.systemui:id/notification_stack_scroller").swipe([0.4766, 0.2969])

home()

poco("com.starmakerinteractive.thevoice:id/arn").child("android.widget.LinearLayout").child("android.support.v7.app.a$c")[4].child("android.widget.FrameLayout").child("android.widget.ImageView").click()
poco("com.starmakerinteractive.thevoice:id/a3p").click()
poco(text="Log In").click()
text("cyl@22.cn")
poco("com.starmakerinteractive.thevoice:id/sk").child("android.widget.RelativeLayout").child("com.starmakerinteractive.thevoice:id/afa").child("com.starmakerinteractive.thevoice:id/af9").child("android.widget.FrameLayout").child("com.starmakerinteractive.thevoice:id/sm")

text("000000")
poco("locale-selector").swipe([0.0312, 0.0251])

poco("com.starmakerinteractive.thevoice:id/j5").click()
sleep(2.0)
if exists(Template(r"tpl1542076690434.png", record_pos=(-0.001, 0.627), resolution=(1440, 2560))):
    touch(Template(r"tpl1542076708147.png", record_pos=(0.44, 0.44), resolution=(1440, 2560)))
assert_exists(Template(r"tpl1542076787820.png", threshold=0.49999999999999983, target_pos=5, rgb=False, record_pos=(-0.377, 0.431), resolution=(1440, 2560)), "登陆成功")



