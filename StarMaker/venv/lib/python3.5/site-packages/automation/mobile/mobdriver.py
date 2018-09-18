#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from collections import namedtuple

import time
from appium import webdriver
from selenium.webdriver.common.by import By

from automation.mobile.platforms import Platform
from automation.mobile.uicomponents import UIComponents

import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def collect_prerequisites():
    """
    Collects all prerequisites required to run the UIAutomation test case.
    :return: 
    """
    print("1 - iOS")
    print("2 - Android")
    platform = int(input("Choose platform:"))
    if 1 < platform > 2:
        print('You have selected an invalid platform')
        exit(1)
    app_bundle = input("Enter path to app bundle:")
    if app_bundle.__len__() == 0:
        print('Can not test an app which does not exist ;)')
        exit(1)
    return {
        "platform": platform,
        "app_bundle": app_bundle
    }


class MobDriver(webdriver.Remote):
    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
                 desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False):
        super(MobDriver, self).__init__(command_executor, desired_capabilities, browser_profile, proxy,
                                        keep_alive)
        # get copy of desired_capabilities dict
        self.desired_caps = desired_capabilities
        # identify platform
        if self.desired_caps['platformName'] == "Android":
            self.platform = Platform.ANDROID
        elif self.desired_caps['platformName'] == "iOS":
            self.platform = Platform.IOS
        else:
            self.platform = Platform.UNKNOWN

    def find_alert(self):
        """
        Finds alert and return it as named tuple 'Alert(alert=alrt, text=text, btns=btns)'
        This is just a temporary workaround till Appium solves swith_to.alert issue.
        :return: 
        """
        Alert = namedtuple('Alert', ['alert', 'text', 'btns'])
        if self.platform == Platform.IOS:
            lookup_xpath = UIComponents.ALERT.iOS
            alrt = self.find_element_by_xpath(lookup_xpath)
            text = alrt.find_element_by_xpath(UIComponents.LABEL.iOS.format('@*')).text
            btns = alrt.find_elements_by_xpath(UIComponents.BUTTON.iOS.format('@*'))
        elif self.platform == Platform.ANDROID:
            lookup_xpath = UIComponents.ALERT.Android
            alrt = self.find_element_by_xpath(lookup_xpath)
            text = alrt.find_element_by_xpath(UIComponents.LABEL.Android.format('@*')).text
            btns = alrt.find_elements_by_xpath(UIComponents.BUTTON.Android.format('@*'))

        alert = Alert(alert=alrt, text=text, btns=btns)
        return alert

    def check_alert(self, msg=None, btn_index=0):
        """
        This method will check alert and compare the message
        :param msg: If provided, will be compared with alert message. Will return false if msg does not match
        :param btn_index:  If provided, will be clicked to dismissed alert.
        :return: Will return named tuple 'Result'. Which as two params, 'result':bool and 'msg':str.
        """
        time.sleep(2)
        Result = namedtuple('Result', ['result', 'msg'])
        try:
            alert = self.find_alert()
            if alert is not None:
                alert.btns[btn_index].click()
                if msg is not None:
                    success = (alert.text == msg)
                    return Result(result=success, msg='Wrong alert msg')
                else:
                    alert.btns[btn_index].click()
                    return Result(result=True, msg='No alert msg')
            else:
                return Result(result=False, msg='No alert found')
        except:
            return Result(result=False, msg='There is some error')

    def find_by_name(self, widget_type, name):
        """ 
        :param name: Name of the component
        :param widget_type: Type of widget
        :return: returns labeled element of type 
        """
        time.sleep(2)
        if self.platform == Platform.IOS:
            lookup_xpath = widget_type.iOS.format("@hint='{0}' or @value='{0}' or @label='{0}' or @name='{0}'")
        elif self.platform == Platform.ANDROID:
            lookup_xpath = widget_type.Android.format("@text='{0}'")

        lookup_xpath = lookup_xpath.format(name)
        return self.find_element_by_xpath(lookup_xpath)

    def find_by_index(self, widget_type, index):
        """
        :param index: Index of component to return from list of found elements
        :param widget_type: Type of widget
        :return: returns element of type at index
        """

        time.sleep(2)
        if self.platform == Platform.IOS:
            lookup_xpath = widget_type.iOS
        elif self.platform == Platform.ANDROID:
            lookup_xpath = widget_type.Android

        return self.find_element_by_xpath(lookup_xpath.format(index))
