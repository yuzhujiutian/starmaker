# encoding=utf-8
import time


def qmMethodLog(fun):
    def wrap(self, *arg, **kwargs):
        funcName = fun.__name__
        className = self.__class__.__name__
        ts = time.strftime('%m-%d %H:%M:%S')
        print('<%s>: %s.%s with' % (ts, className, funcName), arg, kwargs)
        result = fun(self, *arg, **kwargs)
        return result
    return wrap


# 修饰器，把类实现的方法调用都打印出来，方便debug
class QmClassMethodLog(type):
    def __new__(mcs, class_name, class_parents, class_attr):
        attrs = ((name, value) for name, value in list(class_attr.items()) if not name.startswith('__'))

        for name, value in attrs:
            if 'log' in name:
                continue

            if callable(value):
                class_attr[name] = qmMethodLog(value)

        return super(QmClassMethodLog, mcs).__new__(mcs, class_name, class_parents, class_attr)
