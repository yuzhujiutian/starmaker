# coding=utf-8
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_caps = {
               'platformName': 'Android',
               'deviceName': 'c9ltechn',
               'platformVersion': '8.0',
               'appPackage': 'com.starmakerinteractive.starmaker',
               'appActivity': 'com.ushowmedia.starmaker.activity.SplashActivity',
               'noReset': 'true',
               'automationName': 'uiautomator2'
               }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def test():
    time.sleep(8)
    driver.find_element_by_id("com.starmakerinteractive.starmaker:id/close_tweet").click()
    time.sleep(2)
    driver.find_element_by_id("com.starmakerinteractive.starmaker:id/tv_dislike").click()
    time.sleep(2)
    toast_loc = ("xpath", ".//*[contains(@text,'You will see fewer similar posts.')]")
    t = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc),"Toast Not Found")
    print(t)
    print("OK")
    toast_text = driver.find_element("xpath", ".//*[contains(@text,'You will see fewer similar posts.')]").text
    print(toast_text)






if __name__ == '__main__':
    test()


