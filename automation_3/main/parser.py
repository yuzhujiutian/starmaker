# coding=utf-8
import argparse
import os

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

# 当前脚本的父目录的绝对路径
current_script_parent_dir = os.path.realpath(os.path.abspath(__file__ + '/..'))

with open(os.path.join(current_script_parent_dir, 'config.txt'), 'w') as f:
# with open('config.txt', 'w') as f:
    f.write(str(v))
    f.flush()

