# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1542177688468.png", record_pos=(0.398, 0.815), resolution=(1440.0, 2560.0)))
sleep(1.0)
touch(Template(r"tpl1542177694044.png", record_pos=(-0.126, 0.631), resolution=(1440.0, 2560.0)))

sleep(1.0)
touch(Template(r"tpl1542177769299.png", record_pos=(-0.301, 0.031), resolution=(1440, 2560)))

text("cyl@22.cn")
touch(Template(r"tpl1542177712425.png", record_pos=(-0.351, -0.296), resolution=(1440.0, 2560.0)))
text("000000")
swipe(Template(r"tpl1542177724751.png", record_pos=(-0.018, -0.137), resolution=(1440.0, 2560.0)), vector=[0.0032, 0.0])
sleep(3.0)
if exists(Template(r"tpl1542177874735.png", record_pos=(-0.004, 0.622), resolution=(1440, 2560))):
    touch(Template(r"tpl1542177916401.png", record_pos=(0.434, 0.435), resolution=(1440, 2560)))
assert_exists(Template(r"tpl1542178026684.png", record_pos=(-0.34, -0.09), resolution=(1440, 2560)), "输入正确帐号密码，登陆成功")
home()


