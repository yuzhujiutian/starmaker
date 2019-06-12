#encoding=utf-8
from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

# 首页相关操作
class Home(object):
    Trend = 'main_tab_trend'
    Discovery = 'main_tab_discovery'
    Sing = 'main_tab_sing'
    Message = 'main_tab_message'
    Me = 'main_tab_me'

    _tabs = [Trend, Discovery, Sing, Message, Me]

    def __init__(self, driver):
        self.driver = driver
        self.wait5 = WebDriverWait(self.driver, 5, 1);
        self.wait15 = WebDriverWait(self.driver, 15, 1);

    # 切换tab
    def switch_tab(self, tab):
        if tab not in Home._tabs:
            print 'can\'t switch tab, tab parameter %s is wrong...'
            return

        el = self.wait5.until(lambda driver: driver.find_element_by_accessibility_id(tab))

        el.click()


if __name__ == '__main__':
    import sys; 
    sys.path.append('..')

    import random

    import unittest
    from base.base import BaseTestCase
    class SimpleAndroidTests(BaseTestCase):

        def test_1(self):
            home = Home(self.driver)

            elements = None

            while elements is None:
                home.switch_tab(Home.Trend)
                elements = self.wait15.until(lambda driver: driver.find_elements_by_accessibility_id('popular_content_item'))

            count = 0
            threshold = 5
            while count < threshold:
                count += 1
                self.swipeUp()

    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)











