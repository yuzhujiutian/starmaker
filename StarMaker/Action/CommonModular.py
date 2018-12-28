# coding=utf-8
import time
import unittest
from Utils.Tools import Tools
from Utils.GetAppiumDeriver import GetAppiumDeriver


# 通用操作，用于DIY拼接用例
class CommonModular(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetAppiumDeriver().driver
        time.sleep(5)

    def setUp(self):
        pass

    def tearDown(self):
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        pass

    # 返回
    def Back(self):
        self.driver.back()
        time.sleep(2)
