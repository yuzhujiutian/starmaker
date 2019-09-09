# coding=utf-8
import os
import re
import time


def TestLog_Processing():
    # 获取当前时间
    t = time.localtime(time.time())
    # 转化为8位年月日
    present_time = t.tm_year * 10000 + t.tm_mon * 100 + t.tm_mday
    # 获取当前路径
    log_path = os.getcwd() + "\\.logs"
    # print log_path
    # 获取当前路径下文件list
    log_list = os.listdir(log_path)
    # 处理log日志
    for i in log_list:
        logs = os.path.join(log_path, i)
        Suffix = os.path.splitext(i)[1]
        if Suffix == ".log":
            log_date = int(re.findall('(\\d+)', str(logs))[0])
            # 第一步：如果日志超过3天则清理
            if log_date <= present_time-3:
                os.remove(logs)
                continue
            # 第二步：非当天的日志超过10MB则清理
            if log_date != present_time:
                log_size_b = os.path.getsize(logs)
                log_size_mb = round(log_size_b/float(1024*1024), 2)
                if log_size_mb >= 10:
                    os.remove(logs)
                    continue
            # 第三步：当天的日志超过100MB则清理
            # if log_date == present_time:
            #     log_size_b = os.path.getsize(logs)
            #     log_size_mb = round(log_size_b/float(1024*1024), 2)
            #     if log_size_mb >= 100:
            #         os.remove(logs)
            #         continue


if __name__ == '__main__':
    TestLog_Processing()
