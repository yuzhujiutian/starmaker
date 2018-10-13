# coding:UTF-8
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.Tools import Tools
from appium.webdriver.webdriver import WebDriverWait


# 查找元素，如果存在返回元素，否则截图
class find_element(object):
    def __init__(self):
        self.driver = GetAppiumDeriver().driver

    # 特殊：查找元素，如果存在返回True，否则False
    def Find(self, **elements):
        try:
            if elements:
                return True
            else:
                WebDriverWait(elements, 10)
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def ID(self, ID):
        try:
            element_id = self.driver.find_element_by_id(ID)
            return element_id
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def IDS(self, ID, num):
        try:
            elements_ids = self.driver.find_elements_by_id(ID)[num]
            return elements_ids
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def Cla(self, Cla):
        try:
            element_Cla = self.driver.find_element_by_class_name(Cla)
            return element_Cla
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def ClaS(self, Cla, num):
        try:
            elements_Cla = self.driver.find_elements_by_class_name(Cla)[num]
            return elements_Cla
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def Xpa(self, Xpath):
        try:
            element_Xpath = self.driver.find_element_by_xpath(Xpath)
            return element_Xpath
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def XpaS(self, Xpath, num):
        try:
            elements_Xpath = self.driver.find_elements_by_xpath(Xpath)[num]
            return elements_Xpath
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def AID(self, AID):
        try:
            elements_AID = self.driver.find_element_by_accessibility_id(AID)
            return elements_AID
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def AU(self, AU):
        try:
            elements_AU = self.driver.find_element_by_android_uiautomator(AU)
            return elements_AU
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False

    def AUS(self, AU, num):
        try:
            elements_AUS = self.driver.find_elements_by_android_uiautomator(AU)[num]
            return elements_AUS
        except:
            # 截图并上报
            print("As shown, the element is not found.")
            Tools().get_element_error_images()
            return False
