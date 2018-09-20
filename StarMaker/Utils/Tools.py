# coding=utf-8
# ----------
# 通用工具封装
# ----------
import re
import time
import datetime
from Utils.GetAppiumDeriver import GetAppiumDeriver


# ----------
# 常用工具
# ----------
class Tools:
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
    def Popup_GeneralMethod(self, **elements):
        # **为可传项；如果该元素有text属性，传入**text时会判断精确符合。
        for key in elements:
            global element
            element = elements.get(key)
            if key == "ID":
                PopupProcessing().ID()
                return True
            elif key == "IDS":
                PopupProcessing().IDS()
                return True
            elif key == "Cla":
                PopupProcessing().Cla()
                return True
            elif key == "ClaS":
                PopupProcessing().ClaS()
                return True
            elif key == "AID":
                PopupProcessing().AID()
                return True
            elif key == "AIDS":
                PopupProcessing().AIDS()
                return True
            elif key == "AU":
                PopupProcessing().AU()
                return True
            elif key == "AUS":
                PopupProcessing().AUS()
                return True
            elif key == "Xpa":
                PopupProcessing().Xpa()
                return True
            elif key == "XpaS":
                PopupProcessing().XpaS()
                return True
            else:
                print(key)
                return False

    # 1.ID = [ID, **text]
    def ID(self):
        # 提取键值
        ID = element
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
                print("弹窗未找到:", ID)
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
                print("弹窗未找到:", ID)
                return False
        # 否则返回值的属性
        else:
            print(type(ID))
            return False

    # 2.IDS = [IDS, index, **text]
    def IDS(self):
        # 提取键值
        IDS = element
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
                    print("弹窗未找到:", IDS)
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
                    print("弹窗未找到:", IDS)
                    return False
            # 否则返回值个数
            else:
                print(len(IDS))
                return False
        # 否则返回值类型
        else:
            print(type(IDS))
            return False

    # 3.Cla = [Cla, **text]
    def Cla(self):
        # 提取键值
        Cla = element
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
                print("弹窗未找到:", Cla)
                return False
        # 如果值是列表
        elif isinstance(Cla, list):
            # 提取值
            element_cla = Cla[0]
            element_cla_text = Cla[1]
            # 查找元素，存在则返回True
            try:
                Ele_text = self.driver.find_element_by_class_name(element_cla).text
                if Ele_text == element_cla_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", Cla)
                return False
        # 否则返回值类型
        else:
            print(type(Cla))
            return False

    # 4.ClaS = [ClaS, index, **text]
    def ClaS(self):
        # 提取键值
        ClaS = element
        # 如果值是列表
        if isinstance(ClaS, list):
            # 且有两个值
            if len(ClaS) == 2:
                # 提取值
                element_clas = ClaS[0]
                element_clas_number = ClaS[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_class_name(element_clas)[element_clas_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", ClaS)
                    return False
            # 或有三个值
            elif len(ClaS) == 3:
                # 提取值
                element_clas = ClaS[0]
                element_clas_number = ClaS[1]
                element_clas_text = ClaS[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_class_name(element_clas)[element_clas_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_clas_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", ClaS)
                    return False
            # 否则返回值个数
            else:
                print(len(ClaS))
                return False
        # 否则返回值类型
        else:
            print(type(ClaS))
            return False

    # 5.AID = [AID, **text]
    def AID(self):
        # 提取键值
        AID = element
        # 如果值是字符串
        if isinstance(AID, str):
            # 提取值
            element_aid = AID
            # 查找元素，存在返回True
            try:
                self.driver.find_element_by_accessibility_id(element_aid)
                return True
            # 否则返回False
            except:
                print("弹窗未找到:", AID)
                return False
        # 如果值是列表
        elif isinstance(AID, list):
            # 提取值
            element_aid = AID[0]
            element_aid_text = AID[1]
            # 查找元素，存在且文案相符返回True
            try:
                Ele_text = self.driver.find_element_by_accessibility_id(element_aid).text
                # 精准匹配，如果文案相符
                if Ele_text == element_aid_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", AID)
                return False
        # 否则返回值的属性
        else:
            print(type(AID))
            return False

    # 6.AIDS = [AIDS, index, **text]
    def AIDS(self):
        # 提取键值
        AIDS = element
        # 如果值是列表
        if isinstance(AIDS, list):
            # 且有两个值
            if len(AIDS) == 2:
                # 提取值
                element_aids = AIDS[0]
                element_aids_number = AIDS[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_accessibility_id(element_aids)[element_aids_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", AIDS)
                    return False
            # 或有三个值
            elif len(AIDS) == 3:
                # 提取值
                element_aids = AIDS[0]
                element_aids_number = AIDS[1]
                element_aids_text = AIDS[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_accessibility_id(element_aids)[element_aids_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_aids_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", AIDS)
                    return False
            # 否则返回值个数
            else:
                print(len(AIDS))
                return False
        # 否则返回值类型
        else:
            print(type(AIDS))
            return False

    # 7.AU = [AU, **text]
    def AU(self):
        # 提取键值
        AU = element
        # 如果值是字符串
        if isinstance(AU, str):
            # 提取值
            element_au = AU
            # 查找元素，存在返回True
            try:
                self.driver.find_element_by_android_uiautomator(element_au)
                return True
            # 否则返回False
            except:
                print("弹窗未找到:", AU)
                return False
        # 如果值是列表
        elif isinstance(AU, list):
            # 提取值
            element_au = AU[0]
            element_au_text = AU[1]
            # 查找元素，存在且文案相符返回True
            try:
                Ele_text = self.driver.find_element_by_android_uiautomator(element_au).text
                # 精准匹配，如果文案相符
                if Ele_text == element_au_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", AU)
                return False
        # 否则返回值的属性
        else:
            print(type(AU))
            return False

    # 8.AUS = [AUS, index, **text]
    def AUS(self):
        # 提取键值
        AUS = element
        # 如果值是列表
        if isinstance(AUS, list):
            # 且有两个值
            if len(AUS) == 2:
                # 提取值
                element_aus = AUS[0]
                element_aus_number = AUS[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_android_uiautomator(element_aus)[element_aus_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", AUS)
                    return False
            # 或有三个值
            elif len(AUS) == 3:
                # 提取值
                element_aus = AUS[0]
                element_aus_number = AUS[1]
                element_aus_text = AUS[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_android_uiautomator(element_aus)[element_aus_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_aus_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", AUS)
                    return False
            # 否则返回值个数
            else:
                print(len(AUS))
                return False
        # 否则返回值类型
        else:
            print(type(AUS))
            return False

    # 9.Xpa = [Xpa, **text]
    def Xpa(self):
        # 提取键值
        Xpa = element
        # 如果值是字符串
        if isinstance(Xpa, str):
            # 提取值
            element_xpa = Xpa
            # 查找元素，存在返回True
            try:
                self.driver.find_element_by_xpath(element_xpa)
                return True
            # 否则返回False
            except:
                print("弹窗未找到:", Xpa)
                return False
        # 如果值是列表
        elif isinstance(Xpa, list):
            # 提取值
            element_xpa = Xpa[0]
            element_xpa_text = Xpa[1]
            # 查找元素，存在且文案相符返回True
            try:
                Ele_text = self.driver.find_element_by_xpath(element_xpa).text
                # 精准匹配，如果文案相符
                if Ele_text == element_xpa_text:
                    return True
                # 否则返回当前文案
                else:
                    print(Ele_text)
                    return False
            # 否则返回False
            except:
                print("弹窗未找到:", Xpa)
                return False
        # 否则返回值的属性
        else:
            print(type(Xpa))
            return False

    # 10.XpaS = [XpaS, index, **text]
    def XpaS(self):
        # 提取键值
        Xpas = element
        # 如果值是列表
        if isinstance(Xpas, list):
            # 且有两个值
            if len(Xpas) == 2:
                # 提取值
                element_xpas = Xpas[0]
                element_xpas_number = Xpas[1]
                # 查找元素，存在则返回True
                try:
                    Ele_text = self.driver.find_elements_by_xpath(element_xpas)[element_xpas_number].text
                    print(Ele_text)
                    return True
                # 否则返回False
                except:
                    print("弹窗未找到:", Xpas)
                    return False
            # 或有三个值
            elif len(Xpas) == 3:
                # 提取值
                element_xpas = Xpas[0]
                element_xpas_number = Xpas[1]
                element_xpas_text = Xpas[2]
                # 查找元素，存在且文案相符返回True
                try:
                    Ele_text = self.driver.find_elements_by_xpath(element_xpas)[element_xpas_number].text
                    # 精准匹配，如果文案相符
                    if Ele_text == element_xpas_text:
                        return True
                    # 否则返回当前文案
                    else:
                        print(Ele_text)
                        return False
                # 否则返回False
                except:
                    print("弹窗未找到:", Xpas)
                    return False
            # 否则返回值个数
            else:
                print(len(Xpas))
                return False
        # 否则返回值类型
        else:
            print(type(Xpas))
            return False


# ----------
# 页面元素校验
# ----------
# 提取该页面同一类型下的所有元素text
class Page_Element_Verification(object):
    def __init__(self):
        self.driver = GetAppiumDeriver().driver
        time.sleep(5)

    # 适用进入页面时校验页面元素加载正确，且这些元素具备同ID/Class或其他
    def PEV_IDS(self, IDS, TextList):
        Pe = self.driver.find_elements_by_id(IDS)
        ExpectText = TextList
        TextList = []
        for index in range(len(Pe)):
            TextList.append(Pe[index].text)
            time.sleep(1)
        if ExpectText == TextList:
            return True
        else:
            LessThanExpected = [i for i in ExpectText if i not in TextList]
            MoreThanExpected = [i for i in TextList if i not in ExpectText]
            # 比预期少了
            if LessThanExpected:
                return False, LessThanExpected
            # 比预期多了
            elif MoreThanExpected:
                return False, MoreThanExpected
            # 排序不正确或未取到
            else:
                print("预期结果:", ExpectText)
                print("实际结果:", TextList)
                return False

    def PEV_ClaS(self, ClaS, TextList):
        Pe = self.driver.find_elements_by_class_name(ClaS)
        ExpectText = TextList
        TextList = []
        for index in range(len(Pe)):
            TextList.append(Pe[index].text)
            time.sleep(1)
        if ExpectText == TextList:
            return True
        else:
            LessThanExpected = [i for i in ExpectText if i not in TextList]
            MoreThanExpected = [i for i in TextList if i not in ExpectText]
            # 比预期少了
            if LessThanExpected:
                return False, LessThanExpected
            # 比预期多了
            elif MoreThanExpected:
                return False, MoreThanExpected
            # 排序不正确或未取到
            else:
                print("预期结果:", ExpectText)
                print("实际结果:", TextList)
                return False





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
