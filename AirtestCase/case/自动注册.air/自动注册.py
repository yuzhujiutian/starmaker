# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
import re
from airtest.core.api import *
from airtest.core.android.android import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)
auto_setup(__file__)
# ---- Setting -----

# ---- 获取邮箱 -----
driver.get("https://10minutemail.net/")
A = driver.find_element_by_id("fe_text").get_attribute("value")
print(A)
# ---- 注册输入邮箱 -----
Android().start_app("com.starmakerinteractive.starmaker")
poco("android.support.v7.app.ActionBar$Tab")[4].click()
poco("com.starmakerinteractive.starmaker:id/img_login_left").click()
poco("com.starmakerinteractive.starmaker:id/txt_sign_up").click()
if poco("com.google.android.gms:id/cancel").exists():
    poco("com.google.android.gms:id/cancel").click()
poco("com.starmakerinteractive.starmaker:id/com_accountkit_email").set_text(A)
poco("com.starmakerinteractive.starmaker:id/com_accountkit_next_button").click()
# ---- 邮箱确认 -----
driver.find_element_by_class_name("fa fa-refresh fa-fw fa-lg ").click()
driver.find_element_by_name("登录 StarMaker").wait(10)
driver.find_element_by_name("登录 StarMaker").click()
driver.find_element_by_class_name("-cx-PRIVATE-developerAccountKit__button _3u88").click()
driver.find_element_by_class_name("_uo2").click()
# ---- 客户端注册账号 -----
poco("com.starmakerinteractive.starmaker:id/et_input").set_text("000000")
poco("com.starmakerinteractive.starmaker:id/btw_email_confirm").click()
poco("com.starmakerinteractive.starmaker:id/gender_secret").click()
poco("com.starmakerinteractive.starmaker:id/tv_save").click()
poco("com.starmakerinteractive.starmaker:id/btn_next").click()
poco("com.starmakerinteractive.starmaker:id/imb_settings").click()
poco("android.widget.ScrollView").swipe([0.0327, -0.598])
poco("com.starmakerinteractive.starmaker:id/btn_settings_logout").click()
poco("com.starmakerinteractive.starmaker:id/md_buttonDefaultPositive").click()








