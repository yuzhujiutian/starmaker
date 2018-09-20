# coding=utf-8


# 调用
def Call():
    function_A()
    function_B()


def function_A():
    # 方法1，仅查看调用函数名
    import inspect
    print("方法一:")
    print('caller name:', inspect.stack()[1][3])


def function_B():
    # 方法2，查看详细调用信息
    import sys
    print("方法二:")
    print("--- current function is      ", sys._getframe().f_code.co_name)
    print("--- current function from    ", sys._getframe().f_code.co_filename)
    print("--- called by function       ", sys._getframe().f_back.f_code.co_name)
    print("--- called at line           ", sys._getframe().f_back.f_lineno)
    print("--- called from file         ", sys._getframe().f_back.f_code.co_filename)


if __name__ == '__main__':
    Call()
