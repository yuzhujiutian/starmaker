#encoding=utf-8
import sys; 
sys.path.append('..')

import unittest

from common.home import Home
from base.base import BaseTestCase
from common.activity import Activity

'''
1.  可能先进入语言选择activity
2.  进入main activity
'''
class LoginTestCase(BaseTestCase):

    def capsSetup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'fe5bb46e'
        desired_caps['appPackage'] = 'com.starmakerinteractive.starmaker'
        desired_caps['appActivity'] = 'com.ushowmedia.starmaker.activity.SplashActivity'
        desired_caps['appWaitActivity'] = ','.join([Activity.Main, Activity.Nux_Language])
        # desired_caps['noReset'] = 'true'
        # desired_caps['automationName'] = 'UiAutomator2'
        return desired_caps

    def _enter_main_activity(self):
        # 如果是语言选择页面
        if self.driver.current_activity == Activity.Nux_Language:
            self.log('enter ' + Activity.Nux_Language)

            # 默认选择英语
            el = self.findElementByAId('nux_language_English')
            el.click()
            self.log('choose English language...')

        # 等待进入主页
        index = 0
        while not self.waitActivity(Activity.Main):
            # 如果还没有进入主页面，有可能语言选择页面，点击事件没发生
            try:
                el.click()
            except Exception as e:
                self.log(e)
            
            index += 1
            if index > 5:
                print 'error: can\'t enter main activity...'
        self.log('enter ' + Activity.Main)

        # 等待是否有弹窗，如果有弹窗，关闭弹窗
        el = self.findElementById('com.starmakerinteractive.starmaker:id/open_promotion_iv_close', wait=False)
        if el != None:
            el.click()

    def test_google_login(self):
        print dir(self.driver)
        self._enter_main_activity()

        # 切换到me页面，会弹出登录框
        home = Home(self.driver)
        home.switch_tab(Home.Me)

        # 找到Google登录按钮
        el = None
        while el is None:
            el = self.findElementById('com.starmakerinteractive.starmaker:id/img_login_google')

            if el is None:
                home.switch_tab(Home.Me)

        el.click()

        self.log('open google login dialog...')

        # 找到google账号名
        el = self.findElementById('com.google.android.gms:id/account_display_name', wait=True)
        self.actionSleep(1)
        el.click()
        print 'click to google login...'
        while not self.waitActivity(Activity.Main):
            self.actionSleep(1)
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)





