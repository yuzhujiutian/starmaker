# coding=utf-8
import re
import subprocess


# 处理chls打点数据
def analysis_chls_dot():
    # 调用php脚本
    # subprocess.call("php C:/Package/starmaker-qa/Dot/gzdecode.php")
    proc = subprocess.Popen("php C:/Package/starmaker-qa/Dot/gzdecode.php", shell=True, stdout=subprocess.PIPE)

    # 解析返回数据
    script_response = proc.stdout.read().decode()
    # print(script_response)

    # 提取events
    events_list = re.findall('","events":' + '(.*)', script_response)
    print("共有 %s 条有效数据" % len(events_list))
    num = 1
    for i in events_list:
        print("当前为第 %s 个events" % num)
        print(i)
        num += 1


if __name__ == '__main__':
    analysis_chls_dot()
