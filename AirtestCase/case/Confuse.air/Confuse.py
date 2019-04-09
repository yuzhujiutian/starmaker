# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)
auto_setup(__file__)
# ---- Setting -----
# 包地址
package_path = "http://119.28.249.120:8080/job/StarMaker-Android-Feture/603/"
jenkins_user = "yaoliang.cui"
jenkins_pwd = "Cui18636499698"
# 17/21
minApi_num = "17"
# arm/x86
cpu_type = "arm"
# app名称
package_name = "com.starmakerinteractive.thevoice"
# ---- 初始化 -----
# 打开打包地址
driver.get(package_path)
# 登陆
driver.find_element_by_name("j_username").send_keys(jenkins_user)
driver.find_element_by_name("j_password").send_keys(jenkins_pwd)
driver.find_element_by_name("Submit").click()
# 

for link in driver.find_elements_by_xpath("//a[@href]"):
    href = link.get_attribute('href')
    if re.search("minApi" + minApi_num + "-" + cpu_type + "(.*)"".txt",href):
        link.click()
        break

resource_mapping = driver.find_element_by_xpath("/html/body/pre").text
# print(resource_mapping)

def FindSource(Source_ID):
    try:
        Result_ID = re.findall("R.id." + "(.*)""'", re.findall(
                    "R.id." + Source_ID + " -> " + "(.*)", resource_mapping).__str__())[0]
        ID = package_name + ":id/" + Result_ID
        print(ID)
        return ID
    
    except:
        return Source_ID

FindSource("layout_find_friend")
driver.quit()

# -----------------------------------------------------------




    
    

