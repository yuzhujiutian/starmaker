# coding=utf-8
import os
import re
import time


# from StarMaker.Utils.ReadXMLData import ReadXMLData


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
            with open(logs, 'r') as f1:
                return f1.read()


# 校验打点
def check_dotting():
    with open('../../analysis_dot/analysis_report_dot/dot_data.txt', 'r') as f2:
        log = re.findall("key=""(.*)", f2.read())
    for i1 in log:
        key = i1.split(",")
        type = key[0]
        page = key[1]
        obj = key[2]
        T = key[3]
        log = check_log()
        dotting_list = re.findall('{'"(.*)"'}', log)
        dotting_keyword = r"'type': '%s', 'page': '%s', 'obj': '%s'" % (type, page, obj)
        for i2 in dotting_list:
            if re.findall(dotting_keyword, i2):
                if abs(int(re.findall(r"'timestamp': ""(\\d+)", i2)[0]) - int(T)) <= 10000:
                    return True


# 获取时间
def check_time():
    T = int(round(time.time() * 1000))
    return T


# 写入文件
def write(exp_dot, T):
    path = "../../analysis_dot/analysis_report_dot/checking_dotting/"
    # page_name = label[0]
    # action_name = label[1]
    # exp_dot = ReadXMLData().returnXMLFile("dot_keys.xml", page_name, action_name, path=path)
    with open(path + 'dot_data.txt', 'a+') as f:
        f.write("key=" + str(exp_dot) + "," + str(T) + "\n")
        f.flush()


