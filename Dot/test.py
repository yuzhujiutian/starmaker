# coding=utf-8
import subprocess
import gzip
import io
import os
# 获取文件路径
path = os.path.abspath("2")
print("path:" + path)
# 调用php脚本
# subprocess.call("php C:/Package/starmaker-qa/Dot/gzdecode.php")

proc = subprocess.Popen("php C:/Package/starmaker-qa/Dot/gzdecode.php", shell=True,
                        stdout=subprocess.PIPE)

script_response = proc.stdout.read()
print(script_response)
print(type(script_response))









if __name__ == '__main__':
    pass