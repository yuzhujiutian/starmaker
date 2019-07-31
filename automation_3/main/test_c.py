# coding=utf-8
with open('../main/config.txt', 'r', encoding='utf-8') as f:
    config = f.read()

con = eval(config)
print(con)
print(con["version"])

# # 版本信息
# version = re.findall("version", )
# # 待测包名
# parser.add_argument("package")
# # 设备信息
# parser.add_argument("platformVersion")
# parser.add_argument("device")
# parser.add_argument("deviceName")



if __name__ == '__main__':
    pass