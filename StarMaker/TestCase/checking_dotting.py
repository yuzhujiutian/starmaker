# coding=utf-8
import os
import time
import unittest

from StarMaker.CommonView.Home import Home
from StarMaker.CommonView.Library import Library
from StarMaker.CommonView.Parties import Parties
from StarMaker.CommonView.PlaybackDetails import PlaybackDetails
from StarMaker.CommonView.Popup import Popup
from StarMaker.CommonView.Search import Search
from StarMaker.Utils.GetAppiumDeriver import GetAppiumDeriver
from StarMaker.Utils.Tools import AssertReportManage
from StarMaker.Utils.Tools import TestData_Processing
from StarMaker.Utils.Tools import Tools
from analysis_dot.analysis_report_dot.checking_dotting import check_log

P = AssertReportManage().Pass
E = AssertReportManage().Error


# 自动化校验基础打点
class checking_dotting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # >>>初始化app<<<
        cls.driver = GetAppiumDeriver().driver
        # 处理上次运行留下的测试数据
        TestData_Processing().TestPicture_Processing()
        time.sleep(8)

    def setUp(self):
        time.sleep(5)

    def tearDown(self):
        # 记录测试数据
        T = check_log.check_time()
        if self.exp_dot:
            check_log.write(self.exp_dot, T)
        # 截图
        Tools().get_images()

    @classmethod
    def tearDownClass(cls):
        print("tearDown")
        path = os.getcwd()
        print(path)
        time.sleep(10)
        if check_log.check_dotting():
            print("错误打点如下")
            print('\n''------------')
            for i in check_log.check_dotting():
                print(i)
            print('------------''\n')
        else:
            print("T44069 打点校验全部通过")

    # ----------
    # 工具-点唱台
    # ----------
    # 展示-Recommend-歌曲展示
    def test_Case1101_ShowLibraryRecommendSongShow(self):
        # 处理Made For You弹窗
        Popup().HomePopup_MadeForYou_Close_LiveClick()
        self.exp_dot = "show,library:Recommend,song_show"

    # 点击-Recommend-歌曲信息
    def test_Case1102_ClickLibraryRecommendSongDetail(self):
        # 点击首页第一首歌曲的歌曲封面图
        Home().SingPage_CommonTab_FirstSongImgCover().click()
        self.exp_dot = "click,library:Recommend,song_detail"
        time.sleep(2)
        self.driver.back()

    # 点击-Recommend-歌曲的Sing按钮
    def test_Case1103_ClickLibraryRecommendSingButton(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        self.exp_dot = "click,library:Recommend,sing_button"

    # 点击-Recommend-点唱类型弹窗的Solo
    def test_Case1104_ClickLibraryRecommendSolo(self):
        # 点击点唱类型弹窗的Solo
        Home().SingPage_SingRecommend_SingType_Solo().click()
        self.exp_dot = "click,library:Recommend,solo"
        time.sleep(2)
        self.driver.back()

    # 点击-Recommend-点唱类型弹窗的JoinCollab
    def test_Case1105_ClickLibraryRecommendJoinCollab(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的JoinCollab
        Home().SingPage_SingRecommend_SingType_JoinCollab().click()
        self.exp_dot = "click,library:Recommend,join_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-Recommend-点唱类型弹窗的StartCollab
    def test_Case1106_ClickLibraryRecommendStartCollab(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的StartCollab
        Home().SingPage_SingRecommend_SingType_StartCollab().click()
        self.exp_dot = "click,library:Recommend,start_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-Recommend-点唱类型弹窗的Chorus
    def test_Case1107_ClickLibraryRecommendChorus(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的Chorus
        if Home().SingPage_SingRecommend_SingType_Chorus():
            Home().SingPage_SingRecommend_SingType_Chorus().click()
            self.exp_dot = "click,library:Recommend,hook"
            time.sleep(2)
            self.driver.back()
        else:
            self.exp_dot = ""
            time.sleep(2)
            self.driver.back()
            self.skipTest("歌曲不支持Chorus")

    # 展示-Trending-歌曲展示
    def test_Case1108_ShowLibraryTrendingSongShow(self):
        # 点击Trending
        Home().SingPage_SingHeat_Trending().click()
        self.exp_dot = "show,library:Trending,song_show"

    # 点击-Trending-歌曲信息
    def test_Case1109_ClickLibraryTrendingSongDetail(self):
        # 点击首页第一首歌曲的歌曲封面图
        Home().SingPage_CommonTab_FirstSongImgCover().click()
        self.exp_dot = "click,library:Trending,song_detail"
        time.sleep(2)
        self.driver.back()

    # 点击-Trending-歌曲的Sing按钮
    def test_Case1110_ClickLibraryTrendingSingButton(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        self.exp_dot = "click,library:Trending,sing_button"

    # 点击-Trending-点唱类型弹窗的Solo
    def test_Case1111_ClickLibraryTrendingSolo(self):
        # 点击点唱类型弹窗的Solo
        Home().SingPage_SingRecommend_SingType_Solo().click()
        self.exp_dot = "click,library:Trending,solo"
        time.sleep(2)
        self.driver.back()

    # 点击-Trending-点唱类型弹窗的JoinCollab
    def test_Case1112_ClickLibraryTrendingJoinCollab(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的JoinCollab
        Home().SingPage_SingRecommend_SingType_JoinCollab().click()
        self.exp_dot = "click,library:Trending,join_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-Trending-点唱类型弹窗的StartCollab
    def test_Case1113_ClickLibraryTrendingStartCollab(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的StartCollab
        Home().SingPage_SingRecommend_SingType_StartCollab().click()
        self.exp_dot = "click,library:Trending,start_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-Trending-点唱类型弹窗的Chorus
    def test_Case1114_ClickLibraryTrendingChorus(self):
        # 点击首页sing_button
        Home().SingPage_SingRecommend_SelectSing().click()
        # 点击点唱类型弹窗的Chorus
        if Home().SingPage_SingRecommend_SingType_Chorus():
            Home().SingPage_SingRecommend_SingType_Chorus().click()
            self.exp_dot = "click,library:Trending,hook"
            time.sleep(2)
            self.driver.back()
        else:
            self.exp_dot = ""
            time.sleep(2)
            self.driver.back()
            self.skipTest("歌曲不支持Chorus")

    # ----------
    # 工具-搜索
    # ----------
    # 展示-搜索结果-歌曲展示
    def test_Case1201_ShowSearchResultSongShow(self):
        time.sleep(10)
        # 点击Sing页面搜索框
        Home().SingPage_Common_Search().click()
        time.sleep(2)
        # 搜索页输入框输入内容
        Library().SearchPage_InputBox().send_keys("love")
        time.sleep(5)
        # 点击第一个联想结果
        Library().SearchPage_RelevantRelevant(2).click()
        time.sleep(2)
        self.exp_dot = "show,search_result,song_show"

    # 点击-搜索结果-歌曲信息
    def test_Case1202_ClickSearchResultSearchItemSong(self):
        # 切换到Songs Tab下
        Search().SearchPage_Search_SongsType().click()
        time.sleep(2)
        # 点击第一首歌曲名
        Search().SearchPage_SongsSearchResult_FirstSongName().click()
        self.exp_dot = "click,search_result,search_item_song"
        time.sleep(2)
        self.driver.back()

    # 点击-搜索结果-歌曲点唱
    def test_Case1203_ClickSearchResultSearchItemSongSing(self):
        # 点击第一首歌曲点唱按钮
        Search().SearchPage_SongsSearchResult_FirstSongSingBtn().click()
        self.exp_dot = "click,search_result,search_item_song_sing"

    # 点击-搜索结果-Solo
    def test_Case1204_ClickSearchResultSolo(self):
        # 点击点唱类型弹窗的Solo
        Home().SingPage_SingRecommend_SingType_Solo().click()
        self.exp_dot = "click,search_result,solo"
        time.sleep(2)
        self.driver.back()

    # 点击-搜索结果-join_collab
    def test_Case1205_ClickSearchResultJoinCollab(self):
        # 点击第一首歌曲点唱按钮
        Search().SearchPage_SongsSearchResult_FirstSongSingBtn().click()
        # 点击点唱类型弹窗的join_collab
        Home().SingPage_SingRecommend_SingType_JoinCollab().click()
        self.exp_dot = "click,search_result,join_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-搜索结果-start_collab
    def test_Case1206_ClickSearchResultStartCollab(self):
        # 点击第一首歌曲点唱按钮
        Search().SearchPage_SongsSearchResult_FirstSongSingBtn().click()
        # 点击点唱类型弹窗的start_collab
        Home().SingPage_SingRecommend_SingType_StartCollab().click()
        self.exp_dot = "click,search_result,start_collab"
        time.sleep(2)
        self.driver.back()

    # 点击-搜索结果-Chorus
    def test_Case1207_ClickSearchResultChorus(self):
        # 点击第一首歌曲点唱按钮
        Search().SearchPage_SongsSearchResult_FirstSongSingBtn().click()
        # 点击点唱类型弹窗的Chorus
        if Home().SingPage_SingRecommend_SingType_Chorus():
            Home().SingPage_SingRecommend_SingType_Chorus().click()
            self.exp_dot = "click,search_result,hook"
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.driver.back()
        else:
            self.exp_dot = ""
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.driver.back()
            self.skipTest("歌曲不支持Chorus")

    # ----------
    # 首页-Popular
    # ----------
    # 展示-popular-卡片
    def test_Case2101_ShowPopularCard(self):
        # 点击Moment
        Home().HomePage_MainTab_MomentTab().click()
        self.exp_dot = "show,popular,card"

    # 点击-popular-删除卡片
    def test_Case2102_ClickPopularDelete(self):
        # 删除首个卡片
        Home().HomePage_FeedCard_Delete().click()
        time.sleep(2)
        self.exp_dot = "click,popular,delete"

    # 点击-popular-卡片
    def test_Case2103_ClickPopularCard(self):
        # 点击首个作品卡片
        Home().HomePage_FeedCard_Img().click()
        self.exp_dot = "click,popular,card"

    # ----------
    # 详情页
    # ----------
    # 播放-详情页-start
    def test_Case2201_PlayPlayDetailStart(self):
        self.exp_dot = "play,playdetail,start"

    # 播放-详情页-loadtime
    def test_Case2202_PlayPlayDetailLoadTime(self):
        self.exp_dot = "play,playdetail,loadtime"
        self.driver.back()

    # 播放-详情页-finish
    def test_Case2203_PlayPlayDetailFinish(self):
        # 点击第二个作品卡片
        Home().HomePage_FeedCard_DIY_Img(1).click()
        self.exp_dot = "play,playdetail,finish"

    # 点击-详情页-follow
    def test_Case2204_ClickPlayDetailFollow(self):
        # 点击Follow
        time.sleep(2)
        if Home().HomePage_FeedCard_Follow().text == "FOLLOW":
            Home().HomePage_FeedCard_Follow().click()
            self.exp_dot = "click,playdetail,follow"
        else:
            self.exp_dot = ""
            self.skipTest("歌手已Follow")

    # 点击-详情页评论-post
    def test_Case2205_ClickPlayDetailCommentsPost(self):
        # 点击Comment
        PlaybackDetails().PlaybackDetailsPage_Video_Comment().click()
        time.sleep(2)
        # 输入评论
        PlaybackDetails().PlaybackDetailsPage_Video_CommentSendBox().send_keys("nice")
        time.sleep(2)
        # 点击post发送
        PlaybackDetails().PlaybackDetailsPage_Video_CommentSendBtn().click()
        self.exp_dot = "click,playdetail:comments,post"

    # 点击-详情页-Like
    def test_Case2206_ClickPlayDetailLike(self):
        time.sleep(2)
        # 点击Like
        PlaybackDetails().PlaybackDetailsPage_Video_Like().click()
        self.exp_dot = "click,playdetail,like"

    # 点击-详情页-unLike
    def test_Case2207_ClickPlayDetailUNLike(self):
        # 点击UNLike
        PlaybackDetails().PlaybackDetailsPage_Video_Like().click()
        # 点击Like
        PlaybackDetails().PlaybackDetailsPage_Video_Like().click()
        self.exp_dot = "click,playdetail,unlike"

    # send-详情页-gift
    def test_Case2208_SendPlayDetailGift(self):
        # 点击Gift弹出礼物面板
        PlaybackDetails().PlaybackDetailsPage_Video_Gift().click()
        # 等待礼物加载完成
        time.sleep(7)
        # 寻找一个金币价值较小的礼物
        gift_num = 2
        while gift_num < 7:
            gift_value = PlaybackDetails().PlaybackDetailsPage_Video_GiftValue(gift_num).text
            try:
                gift_value = int(gift_value)
            except:
                gift_num += 1
                continue
            if int(gift_value) <= 10:
                PlaybackDetails().PlaybackDetailsPage_Video_GiftValue(gift_num).click()
                gift_num = 100
                break
            gift_num += 1
        # 如果没找到，就选择第二排首个（一般这个位置已避开免费、限定、特殊礼物）
        if gift_num != 100:
            PlaybackDetails().PlaybackDetailsPage_Video_GiftValue(4).click()
        # 点击Send按钮
        PlaybackDetails().PlaybackDetailsPage_Video_GiftDetailSendBtn().click()
        time.sleep(2)

        # 处理余额不足弹窗
        try:
            insufficient_funds_text = PlaybackDetails().Gift_SendGift_InsufficientFunds().text
            if insufficient_funds_text == "Insufficient Silvers! Finish the Tasks to get more Silvers.":
                self.driver.back()
            elif insufficient_funds_text == "Not enough storage":
                self.driver.back()
            time.sleep(2)
        # 送礼成功无弹窗
        except:
            # 收起礼物弹窗
            self.driver.back()
            time.sleep(2)
        if PlaybackDetails().PlaybackDetailsPage_Video_GiftDetailSendBtn():
            self.driver.back()
        self.exp_dot = "send,playdetail,gift"

    # 点击-分享面板-FB分享渠道
    def test_Case2209_ClickFunctionPanelShare(self):
        # 点击分享按钮
        PlaybackDetails().PlaybackDetailsPage_Video_Share().click()
        time.sleep(2)
        # 点击分享至FB
        PlaybackDetails().Share_ShareDetail_FB().click()
        time.sleep(3)
        # 返回至播放详情页
        self.driver.back()
        self.exp_dot = "click,function_panel,share"
        time.sleep(3)
        # 返回到popular页
        self.driver.back()

    # ----------
    # KTV
    # ----------
    # 展示-Solo-房间
    def test_Case3101_ShowSoloRoom(self):
        # 点击切换到Party页
        Home().HomePage_MainTab_PartyTab().click()
        time.sleep(4)
        self.exp_dot = "show,solo,room"

    # 点击-Solo-房间
    def test_Case3102_ClickSoloRoom(self):
        # 点击Solo首个房间
        Parties().KtvPage_RoomCard_Cover().click()
        time.sleep(4)
        # 处理排麦引导
        Popup().Popup_KTVPage_QueueUp_LiveClick()
        time.sleep(2)
        self.driver.back()
        Popup().Popup_KTVPage_MinimizeOption_RefuseBtn_LiveClick()
        self.exp_dot = "click,solo,room"

    # 展示-MultiGuest-房间
    def test_Case3103_ShowMultiGuestRoom(self):
        # 点击切换到MultiGuest
        Parties().KtvPage_Tab_MultiGuest().click()
        time.sleep(4)
        self.exp_dot = "show,multiguest,room"

    # 点击-MultiGuest-房间
    def test_Case3104_ClickMultiGuestRoom(self):
        # 点击MultiGuest首个房间
        Parties().KtvPage_RoomCard_Cover().click()
        time.sleep(4)
        self.driver.back()
        Popup().Popup_KTVPage_MinimizeOption_RefuseBtn_LiveClick()
        self.exp_dot = "click,multiguest,room"

    # ----------
    # Live
    # ----------
    # 展示-Live-房间
    def test_Case3201_ShowLiveRoom(self):
        # 点击切换到live
        Parties().KtvPage_Tab_LIVE().click()
        time.sleep(4)
        self.exp_dot = "show,live_hall_0,room"

    # 点击-Live-房间
    def test_Case3202_ClickLiveRoom(self):
        # 点击Live首个房间
        Parties().LivePage_RoomCard_Cover().click()
        time.sleep(4)
        # 处理滑动引导
        Popup().Popup_LivePage_Slide_LiveClick()
        time.sleep(2)
        # self.driver.back()
        # time.sleep(2)
        # Popup().Popup_LivePage_MinimizeOption_RefuseBtn_LiveClick()
        self.exp_dot = "click,live_hall_0,room"


if __name__ == '__main__':
    pass
