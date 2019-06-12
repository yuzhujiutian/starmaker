# coding=utf-8
import os
import re
import time


# from StarMaker.Utils.ReadXMLData import ReadXMLData


# 读取日志
def check_log():
    t = time.strftime("%Y%m%d", time.localtime(time.time())).__str__()
    # 调试使用
    # log_path = "../.logs"
    log_path = "../../analysis_dot/analysis_report_dot/.logs"
    log_list = os.listdir(log_path)
    # 处理log日志
    for i in log_list:
        logs = os.path.join(log_path, i)
        Suffix = os.path.splitext(i)[0]
        if Suffix == "events-logs-" + t:
            with open(logs, 'r') as f1:
                return f1.readlines()


# 校验打点
def check_dotting():
    dotting_list = check_log()
    exp_list = []
    act_list = []
    try:
        # 调试使用
        # with open("./dot_data.txt", "r") as f2:
        with open("../../analysis_dot/analysis_report_dot/checking_dotting/dot_data.txt", "r") as f2:
            log = re.findall("key=""(.*)", f2.read())
        for i1 in log:
            key = i1.split(",")
            type = key[0]
            page = key[1]
            obj = key[2]
            T = key[3]
            dotting_keyword = [r"'type': '%s', 'page': '%s', 'obj': '%s'" % (type, page, obj)]
            exp_list.append(dotting_keyword)
        for i2 in dotting_list:
            try:
                dot_1 = re.findall(r"{" + "(.*?)" + ", 'timestamp': ", i2)
                dot_2 = re.findall(r"(.*?)" + ", 'source': '", dot_1[0])
                if dot_2:
                    act_list.append(dot_2)
                else:
                    act_list.append(dot_1)
            except Exception:
                pass
        error_list = [i for i in exp_list if i not in act_list]
        if error_list:
            return error_list
        else:
            return False
        #     for i2 in dotting_list:
        #         if re.findall(dotting_keyword, str(i2)):
        #             if abs(int(re.findall(r"'timestamp': ""(\\d+)", i2)[0]) - int(T)) <= 60000:
        #                 continue
        #             else:
        #                 error_list.append(i2)
        #         else:
        #             continue
        # if error_list:
        #     return error_list
        # else:
        #     return True
    except:
        pass


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


