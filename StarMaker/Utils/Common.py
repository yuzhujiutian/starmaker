#coding=utf-8

111
#单例模式函数，用来修饰类
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton
#单例模式是一种常用的软件设计模式。
#在它的核心结构中只包含一个被称为单例类的特殊类。
#通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源
