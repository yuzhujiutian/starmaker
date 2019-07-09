# encoding=utf-8
import sys
import unittest

from automation_3.base.base import BaseAction
from automation_3.common.activity import Activity

sys.path.append('..')


# 封装启动相关的操作
class LaunchAction(BaseAction):

    Trend = 'main_tab_trend'
    Discovery = 'main_tab_discovery'
    Sing = 'main_tab_sing'
    Message = 'main_tab_message'
    Me = 'main_tab_me'

    _tabs = [Trend, Discovery, Sing, Message, Me]

    # 默认选择英语
    def _choose_language(self, language='English'):
        # 默认选择英语
        el = self.findElementByAId('nux_language_' + language)
        self.singleTap(el)
        self.log('choose %s language...' % language)
        self.actionSleep(5)

    # 启动到某个tab
    def toTab(self, tab):
        if tab not in LaunchAction._tabs:
            self.log('can\'t switch tab, tab parameter %s is wrong...')
            return

        try:
            el = self.findElementByAId(tab)
            if el:
                self.singleTap(el)
                self.actionSleep(5)
                selected_status = el.get_attribute("selected")
                # 确定切换到某个tab
                if selected_status:
                    self.log('switch to' + tab)
        except Exception as e:
            self.get_error_screenshot()
            self.log('Exception：%s' % e)

        # TODO: 清理弹窗
        
        # 完成切换

    # 登录
    def login(self):
        self.findElementById("img_login_email").click()
        self.actionSleep()
        self.findElementById("txt_login").click()
        self.actionSleep()
        self.findElementsById("et_input", 0).send_keys("cyl@26.cn")
        self.findElementsById("et_input", 1).send_keys("000000")
        self.findElementById("btw_email_confirm").click()
        self.actionSleep(5)

    # 启动
    def launch(self):
        # 清理测试图片
        self.TestPicture_Processing()

        result = True
        # 如果是设置语言页面
        if self.waitActivity(Activity.Nux_Language, timeout=9):
            self.log('enter ' + Activity.Nux_Language)
            self._choose_language()

        # 处理Made For You
        if self.findElementById("tv_guide_title"):
            self.findElementById("iv_close").click()
            self.actionSleep()

        # 等待进入主页面
        index = 0
        threshold = 5
        while not self.waitActivity(Activity.Main):
            # 如果还没有进入主页面，有可能语言选择页面，点击事件没发生
            try:
                self._choose_language()
            except Exception as e:
                self.log(e)
            
            index += 1
            if index > threshold:
                print('error: can\'t enter main activity...')
                break
        self.log('enter ' + Activity.Main + ' ' + str(index))

        if index > threshold:
            # 出错了，启动出错
            self.log('launch to main error, quit test case...')
            result = False
        else:
            # 检查是否有弹窗, 并清理弹窗
            self.clearDialog()
            
            # 启动到主页面，查找tab是否已经存在
            el = None
            try:
                el = self.findElementByAId(LaunchAction.Trend)
            except Exception as e:
                print('Exception:', e)

            if el is None:
                result = False

        self.log('launch: ' + str(result))

        return result
        

if __name__ == '__main__':
    from automation_3.base.base import BaseTestCase

    class LaunchTestCase(BaseTestCase):

        def test_to_trend(self):
            launch = LaunchAction(self)
            # 首先启动
            launch.launch()

            launch.toTab(LaunchAction.Trend)
    suite = unittest.TestLoader().loadTestsFromTestCase(LaunchTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
