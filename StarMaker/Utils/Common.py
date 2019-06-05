# coding=utf-8


# 单例模式函数
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton
# 单例模式是一种常用的软件设计模式。
# 在它的核心结构中只包含一个被称为单例类的特殊类。
# 通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源


import warnings


# 重置警告过滤器
def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test
# 自Python 3.2以来，unittest模块已更新为将警告过滤器设置为默认值
# 基本上，unittest在完成模块导入后，会覆盖警告过滤器首选项
# 因此，在每次测试开始时清除过滤器。可能最好使用装饰器来包装您的测试功能
