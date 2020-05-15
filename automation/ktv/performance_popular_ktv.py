# encoding=utf-8

from automation.base.base import BaseTestCase
from automation.base.launch import LaunchAction

# sys.path.append('..')



class PerformanceMoment(BaseTestCase):

    # 内容卡片
    AID_Popular_Content_Item = 'popular_content_item'

    # Recording
    Activity_Recording = 'com.ushowmedia.starmaker.playdetail.PlayDetailActivity'

    # 主activity
    Activity_Main = 'com.ushowmedia.starmaker.activity.MainActivity'

    '''
    测试首页的内存占用情况
    1.  切换到首页
    2.  等待卡片内容展示出来
    3.  随机点击一张卡片，进入播放详情页，观看10秒，退出播放详情页，
    4.  退回到首页，首页向下浏览，再重复动作3，反复执行n次
    '''
    def test_case001_performance(self):
        # 启动
        LaunchAction(self).launch()

        # # 处理轮盘弹窗
        # if self.findElementById("open_promotion_iv_close"):
        #     self.findElementById("open_promotion_iv_close").click()

        # 切换到trend tab
        LaunchAction(self).toTab(LaunchAction.Trend)
        els = None

        # 开始统计memory
        self.startMemoryProfile()