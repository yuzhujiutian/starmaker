# encoding=utf-8
import sys
import unittest

from automation.base.base import BaseAction
from automation.base.base import BaseTestCase
from automation.common.activity import Activity
from automation.home.launch import LaunchAction

sys.path.append('..')


# 封装的登录相关的操作
class LoginAction(BaseAction):

    # 检查是否已经登录，如果没有登录，触发登录操作
    def checkToLogin(self, preActivity=None):
        # 找到Google登录按钮
        el = self.findElementById('img_login_google')
        if el is None:
            # 没有找到登录按钮，认为不需要登录
            pass
        else:
            self.googleLogin(el, waitActivity=preActivity)

    # googleLoginBtn是google登录按钮，通过点击登录按钮，触发登录逻辑
    def googleLogin(self, googleLoginBtn, waitActivity=Activity.Main):
        if googleLoginBtn is not None:
            googleLoginBtn.click()
        else:
            return

        self.log('open google login dialog...')

        # 找到google账号名, TODO: 需要丰满细节
        el = self.findElementById('com.google.android.gms:id/account_display_name', wait=True)
        self.actionSleep(1)
        el.click()
        print 'click to google login...'
        index = 0
        while not self.waitActivity(waitActivity):
            self.actionSleep(1)
            index += 1
            if index > 10:
                self.log('warning: google login status unknown...')
                break

        # 检查登录成功toast


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

    def test_google_login(self):
        launch = LaunchAction(self)

        launch.launch()

        # 切换到me页面，会弹出登录框
        launch.toTab(LaunchAction.Me)

        # 找到Google登录按钮
        el = None
        index = 0
        while el is None:
            el = self.findElementById('img_login_google')

            if el is None:
                launch.toTab(LaunchAction.Me)

            index += 1
            if index > 5:
                self.log('error: can not find google login botton...')
                break

        loginAction = LoginAction(self)
        loginAction.googleLogin(el)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
