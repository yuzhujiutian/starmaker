# coding=utf-8
import argparse

parser = argparse.ArgumentParser()
# 版本信息
parser.add_argument("version")
# 待测包名
parser.add_argument("package")
# 设备信息
parser.add_argument("platformVersion")
parser.add_argument("device")
parser.add_argument("deviceName")

args = parser.parse_args()

param = vars(args)

v = {}

for key, value in param.items():
    v[key] = value

with open('../main/config.txt', 'w') as f:
    f.write(str(v))
    f.flush()

