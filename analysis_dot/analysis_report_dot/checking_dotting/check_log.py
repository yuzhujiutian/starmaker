# coding=utf-8
import os
import re
import time


# 读取日志
def check_log():
    t = time.strftime("%Y%m%d", time.localtime(time.time())).__str__()
    log_path = "../../analysis_dot/analysis_report_dot/.logs"
    log_list = os.listdir(log_path)
    # 处理log日志
    for i in log_list:
        logs = os.path.join(log_path, i)
        Suffix = os.path.splitext(i)[0]
        if Suffix == "events-logs-" + t:
            with open(logs, 'r') as f:
                return f.read()


# 校验打点
def check_dotting(key, T):
    type = key[0]
    page = key[1]
    obj = key[2]
    log = check_log()
    dotting_list = re.findall('{'"(.*)"'}', log)
    dotting_keyword = r"'type': '%s', 'page': '%s', 'obj': '%s'" % (type, page, obj)
    for i in dotting_list:
        if re.findall(dotting_keyword, i):
            if abs(int(re.findall(r"'timestamp': ""(\\d+)", i)[0]) - T) <= 10000:
                return True


# 获取时间
def check_time():
    T = int(round(time.time() * 1000))
    return T
