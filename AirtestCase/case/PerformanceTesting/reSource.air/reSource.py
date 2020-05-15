# coding=utf-8
import re
# mapping表地址
# mapping_path = "C:/Package/starmaker-qa/StarMaker/bin/resource_mapping.txt"
mapping_path = "E:/Work/starmaker-qa/StarMaker/bin/resource_mapping.txt"
mapping_table = {}


# 整理mapping表到字典
def get_mapping_from_file():
    # 如果mapping表已存在内存中
    if mapping_table:
        pass
    # 如果为空则读取并写入内存
    else:
        # 读取本地mapping表
        with open(mapping_path, "r") as ReadMappingTable:
            # 逐行读取
            for i in ReadMappingTable.readlines():
                # 调用map方法提取key, value
                j = map_mapping_table(i)
                try:
                    # 将key, value写入字典
                    mapping_table[j[0]] = j[1]
                except TypeError:
                    pass
    return mapping_table


# 提取mapping元素
def map_mapping_table(mapping_read):
    try:
        Source_ID = re.findall("R.id." + "(.*)"" -> ", mapping_read)
        Result_ID = re.findall(" -> "".+""R.id." + "(.*)", mapping_read)
        return Source_ID[0], Result_ID[0]
    except IndexError:
        pass


# 包名
def get_package_name():
    packages = {"sm":"com.starmakerinteractive.starmaker",
                "tvp":"com.starmakerinteractive.thevoice",
                "sa":"com.horadrim.android.sargam",
                "su":"com.windforce.android.suaraku"}
    return packages