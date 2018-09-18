# coding=utf-8
# ----------
# 通用工具封装
# ----------
import re
import time
import datetime
from Utils.GetAppiumDeriver import GetAppiumDeriver
from Utils.GetDevicesInfo import GetDevicesInfo
from Utils.Common import singleton


# ----------
# 常用工具
# ----------
class Tools:
    # AppPackage 用于初始化
    @singleton
    def AppPackage(self):
        GetPackages = GetDevicesInfo().GetPackages()[0]
        return GetPackages

    # package拼接 用于元素定位使用
    @singleton
    def package(self):
        setUp_package = Tools().AppPackage()
        element_package = "%s:%s" % (setUp_package, "id/")
        return element_package

    # 截取图片,并保存在images文件夹
    @staticmethod
    def get_images():
        driver = GetAppiumDeriver().driver
        # 定义路径
        png_file = "../TestReport/images/"
        # 获取当前时间
        nowtime = time.strftime('%Y%m%d_%H.%M.%S', time.localtime(time.time()))
        # 定义图片名称
        img_name = nowtime + '.png'
        # 截图
        driver.get_screenshot_as_file('%s%s' % (png_file, img_name))
        print('screenshot:', nowtime, '.png')

    # 元素未找到截图,并保存在images文件夹
    @staticmethod
    def get_element_error_images():
        driver = GetAppiumDeriver().driver
        # 定义路径
        png_file = "../TestReport/images/"
        # 获取当前时间，且days+1，以展示在报告截图最上方
        nowtime = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y%m%d_%H.%M.%S')
        # 定义图片名称
        img_name = nowtime + '.png'
        # 截图
        driver.get_screenshot_as_file('%s%s' % (png_file, img_name))
        print('screenshot:', nowtime, '.png')

    # 动态元素转换
    @staticmethod
    def FindSource(Source_ID):
        global ReadMappingTable
        try:
            ReadMappingTable = open("../bin/resource_mapping.txt", "r")
            Result_ID = re.findall("R.id." + "(.*)""'", re.findall(
                "R.id." + Source_ID + " -> " + "(.*)", ReadMappingTable.read()).__str__())[0]
            return Result_ID
        except:
            return Source_ID
        finally:
            if ReadMappingTable:
                ReadMappingTable.close()


# ----------
# 弹窗处理工具
# ----------
class PopupProcessing(object):
    def __init__(self):
        self.driver = GetAppiumDeriver().driver
        time.sleep(5)

    # 查找弹窗，如果存在则返回True
    def Popup_GeneralMethod(self, **element):
        # 传参规则：**为可传项；如果该元素有text属性，传入**text时会判断精确符合。
        # 1.ID=[ID, **text]
        # 2.IDS=[IDS, index, **text]
        # 3.Cla=[Cla, **index, **text]
        # 接收参数
        for key in element:
            # 如果key是ID
            if key == "ID":
                # 提取键值
                ID = element.get(key)
                # 如果值是字符串
                if isinstance(ID, str):
                    # 提取值
                    element_id = ID
                    # 查找元素，存在返回True
                    try:
                        self.driver.find_element_by_id(element_id)
                        return True
                    # 否则返回False
                    except:
                        return False
                # 如果值是列表
                elif isinstance(ID, list):
                    # 提取值
                    element_id = ID[0]
                    element_id_text = ID[1]
                    # 查找元素，存在且文案相符返回True
                    try:
                        Ele_text = self.driver.find_element_by_id(element_id).text
                        # 精准匹配，如果文案相符
                        if Ele_text == element_id_text:
                            return True
                        # 否则返回当前文案
                        else:
                            print(Ele_text)
                            return False
                    # 否则返回False
                    except:
                        return False
                # 否则返回值的属性
                else:
                    print(type(ID))
                    return False
            # 如果key是IDS
            elif key == "IDS":
                # 提取键值
                IDS = element.get(key)
                # 如果值是列表
                if isinstance(IDS, list):
                    # 且有两个值
                    if len(IDS) == 2:
                        # 提取值
                        element_ids = IDS[0]
                        element_ids_number = IDS[1]
                        # 查找元素，存在则返回True
                        try:
                            Ele_text = self.driver.find_elements_by_id(element_ids)[element_ids_number].text
                            print(Ele_text)
                            return True
                        # 否则返回False
                        except:
                            return False
                    # 或有三个值
                    elif len(IDS) == 3:
                        # 提取值
                        element_ids = IDS[0]
                        element_ids_number = IDS[1]
                        element_ids_text = IDS[2]
                        # 查找元素，存在且文案相符返回True
                        try:
                            Ele_text = self.driver.find_elements_by_id(element_ids)[element_ids_number].text
                            # 精准匹配，如果文案相符
                            if Ele_text == element_ids_text:
                                return True
                            # 否则返回当前文案
                            else:
                                print(Ele_text)
                                return False
                        # 否则返回False
                        except:
                            return False
                    # 否则返回值个数
                    else:
                        print(len(IDS))
                        return False
                # 否则返回值类型
                else:
                    print(type(IDS))
                    return False
            # 如果key是Cla
            elif key == "Cla":
                # 提取键值
                Cla = element.get(key)
                # 如果值是字符串
                if isinstance(Cla, str):
                    # 提取值
                    element_cla = Cla
                    # 查找元素，存在则返回True
                    try:
                        self.driver.find_element_by_class_name(element_cla)
                        return True
                    # 否则返回False
                    except:
                        return False
                # 如果值是列表
                elif isinstance(Cla, list):
                    # 且有两个值
                    if len(Cla) == 2:
                        # 提取值
                        element_cla = Cla[0]
                        element_cla_number = Cla[1]
                        # 查找元素，存在则返回True
                        try:
                            Ele_text = self.driver.find_elements_by_class_name(element_cla)[element_cla_number].text
                            print(Ele_text)
                            return True
                        # 否则返回False
                        except:
                            return False
                    # 或有三个值
                    elif len(Cla) == 3:
                        # 提取值
                        element_cla = Cla[0]
                        element_cla_number = Cla[1]
                        element_cla_text = Cla[2]
                        # 查找元素，存在且文案相符返回True
                        try:
                            Ele_text = self.driver.find_elements_by_class_name(element_cla)[element_cla_number].text
                            # 精准匹配，如果文案相符
                            if Ele_text == element_cla_text:
                                return True
                            # 否则返回当前文案
                            else:
                                print(Ele_text)
                                return False
                        # 否则返回False
                        except:
                            return False
                    # 否则返回值个数
                    else:
                        print(len(Cla))
                        return False
                # 否则返回值类型
                else:
                    print(type(Cla))
                    return False
            # 否则返回键值
            else:
                print(key)
                return False
        # 返回
        return


# ----------
# 屏幕处理工具
# ----------
class Screen(object):
    def __init__(self):
        self.driver = GetAppiumDeriver().driver
        # 获取屏幕的size
        self.size = self.driver.get_window_size()
        print(self.size)
        # 获取屏幕宽度 width
        self.width = self.size['width']
        # 获取屏幕高度 height
        self.height = self.size['height']

    # 计算百分比(传参：本机屏幕上的x，y轴坐标；返回：该坐标的百分比)
    def CalculatedPercentage(self, x1N, y1N):
        x1P = x1N / self.width
        print("x1N:", x1N, "y1N:", y1N)
        y1P = y1N / self.height
        print("x1P:", x1P, "y1P:", y1P)
        return x1P, y1P

    # 滑动打开通知栏
    def SwipeOpen_NoticeBoard(self):
        # 执行滑屏操作,向下滑动(下拉),打开通知栏
        x1 = self.width * 0.5
        y1 = self.height * 0.01
        y2 = self.height * 0.5
        time.sleep(1)
        self.driver.swipe(x1, y1, x1, y2)

    # 滑动收起通知栏
    def SwipeClose_NoticeBoard(self):
        # 执行滑屏操作,向上滑动(收起)，收起通知栏
        x1 = self.width * 0.5
        y1 = self.height * 0.5
        y2 = self.height * 0.01
        time.sleep(1)
        self.driver.swipe(x1, y1, x1, y2)

    # 根据传值百分比，自定义滑动操作(传参：百分比)
    def DIYSwipe_Percentage(self, x1P, y1P, x2P, y2P, t):
        # 执行滑屏操作,接收参数(四个百分比+时间),运算后滑动
        x1 = self.width * x1P
        y1 = self.height * y1P
        x2 = self.width * x2P
        y2 = self.height * y2P
        time.sleep(1)
        self.driver.swipe(x1, y1, x2, y2, t)

    # 根据屏幕百分比，自定义点击操作(传参：百分比)
    def AccurateClicks_Percentage(self, x1P, y1P, t):
        # 执行滑屏操作,接收参数(两个百分比+时间),运算后滑动
        # 时间:点击(500)/长按3s(3000)
        x1 = self.width * x1P
        y1 = self.height * y1P
        time.sleep(1)
        self.driver.tap([(x1, y1)], t)

    # 多点触控(最多支持五点触控)
    def Multi_Touch_Percentage(self, x1P, y1P, x2P, y2P, x3P, y3P, x4P, y4P, x5P, y5P, t):
        # 执行滑屏操作,接收参数(最多十个百分比+时间),运算后滑动
        # 时间:点击(500)/长按3s(3000)
        # 第一个点
        x1 = self.width * x1P
        y1 = self.height * y1P
        # 第二个点
        x2 = self.width * x2P
        y2 = self.height * y2P
        # 第三个点
        x3 = self.width * x3P
        y3 = self.height * y3P
        # 第四个点
        x4 = self.width * x4P
        y4 = self.height * y4P
        # 第五个点
        x5 = self.width * x5P
        y5 = self.height * y5P
        time.sleep(1)
        self.driver.tap([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], t)
