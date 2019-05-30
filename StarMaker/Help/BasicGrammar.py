# coding=utf-8
# --------------
# 基础语法 Help
# --------------

import os
# 导入时间模块
import time


# 定义一个类，并继承 object 类属性
class A(object):
    # 定义类的构造函数，他类似于unittest框架下面的setUp
    def __init__(self):
        # 获取当前时间戳
        self.time = time.time()
        # 获取当前路径
        self.path = os.getcwd()

    # 定义方法，将时间转换为整形
    def a_time(self):
        # int() 函数，将其他类型转为整形
        a_time = int(self.time)
        print("%s:%s" % ("self.time", self.time))
        print("%s:%s" % ("a_time", a_time))

    # 定义方法，将时间详细打印
    def b_time(self):
        # 打印详细时间
        #    年            月        日          时          分         秒    一周中第几天 一年中第几天    夏令时
        #(tm_year=2018, tm_mon=9, tm_mday=18, tm_hour=10, tm_min=57, tm_sec=39, tm_wday=1, tm_yday=261, tm_isdst=0)"
        # tm_wday=1 一周中的第几天，从周一开始算(0-6)，1是周二
        b_time = time.localtime(self.time)
        print("%s:%s" % ("b_time", b_time))

    # 定义方法，将时间转换为特定格式
    def c_time(self):
        # 打印特定格式时间
        c_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.time))
        print("%s:%s" % ("c_time", c_time))

    # 获取当前路径
    def a_path(self):
        # 加self的变量，可供外部调用
        path = self.path
        print("%s:%s" % ("path", path))

    # 代码组
    def clause(self):
        # 如果有时间
        if self.time:
            print("OK")
        # 或者脚下有路
        elif self.path:
            print("Yes")
        # 或者这些都没有
        else:
            print("No")

    # 多个代码组嵌套
    def clauses(self):
        # 如果只是有时间
        if self.time:
            print("OK")
            # 如果有时间还有脚下的路
            if self.path:
                print("OK,Yes")
            # 如果没有时间没有路
            else:
                print("No,No")
        # 如果没有时间
        else:
            print("No")
            # 如果只是有路
            if self.path:
                print("No,Yes")
            # 如果路也没有
            else:
                print("No,No")

    @staticmethod
    def a_var():
        a = 1
        print(a)

    @staticmethod
    def b_var():
        global c
        a = b = c = 2
        print(a, b, c)

    @staticmethod
    def c_var():
        d = c + 1
        print(d)

    @staticmethod
    def d_var():
        a = 1  # 整形
        b = "一个"  # 字符串
        set.c = [1, "二"]  # 列表
        d = {"t": "time", "p": "path"}  # 字典
        e = (1, "二", "san")  # 元组
        print(a, b, c, d, e)  # 打印变量
        print(type(a), type(b), type(c), type(d), type(e))  # 打印变量类型


# 实例化方法
A().a_time()
A().b_time()
A().c_time()
A().a_path()
A().clause()
A().clauses()
A().a_var()
A().b_var()
A().c_var()
A().d_var()
# 主函数，点击绿色箭头可运行
if __name__ == '__main__':
    pass
