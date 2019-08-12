# coding=utf-8
import re
import os


def internationalization():
    Localizable_path = ".//锘縇ocalizable"
    Localizable_list = os.listdir(Localizable_path)
    for i in Localizable_list:
        if os.path.splitext(i)[1] == ".lproj":
            # 修改strings文件格式为txt
            if os.path.exists(Localizable_path + "//" + i + "//""Localizable.strings"):
                os.rename(Localizable_path + "//" + i + "//""Localizable.strings",
                          Localizable_path + "//" + i + "//""Localizable.txt")
            # 提取key
            if i == "en.lproj":
                global en_List
                en_List = []
                with open(Localizable_path + "//" + i + "//""Localizable.txt", encoding="gb18030",
                          errors="ignore") as C:
                    D = re.findall('"'"(.*)"'" = "', C.read())
                    for j in D:
                        en_List.append(j)

    Localizable_path1 = ".//锘縇ocalizable1"
    Localizable_list1 = os.listdir(Localizable_path1)
    for i in Localizable_list1:
        if os.path.splitext(i)[1] == ".lproj":
            # 修改strings文件格式为txt
            if os.path.exists(Localizable_path1 + "//" + i + "//""Localizable.strings"):
                os.rename(Localizable_path1 + "//" + i + "//""Localizable.strings",
                          Localizable_path1 + "//" + i + "//""Localizable.txt")
            # 提取key
            if i == "en.lproj":
                global en_List1
                en_List1 = []
                with open(Localizable_path1 + "//" + i + "//""Localizable.txt", encoding="gb18030", errors="ignore") as C:
                    D = re.findall('"'"(.*)"'" = "', C.read())
                    for j in D:
                        en_List1.append(j)

    # 版本key值变化校验
    newly_added = [i for i in en_List1 if i not in en_List]
    newly_delete = [i for i in en_List if i not in en_List1]
    print("一、【en语言key值变化校验】：")
    if newly_added and newly_delete:
        print("结论：本版本既有新增，也有移除")
        print("1>版本新增了 " + str(len(newly_added)) + " 个key：" + "\n" + str(newly_added))
        print("2>版本移除了 " + str(len(newly_delete)) + " 个key：" + "\n" + str(newly_delete))
    elif newly_added:
        print("结论：本版本只有新增")
        print("1>版本新增了 " + str(len(newly_added)) + " 个key：" + "\n" + str(newly_added))
    elif newly_delete:
        print("结论：本版本只有移除")
        print("1>版本移除了 " + str(len(newly_delete)) + " 个key：" + "\n" + str(newly_delete))

    # 获取对应key的其他多语言
    langue = []
    print("二、【新增key值翻译校验】：")
    Untranslated_Langue = []
    if newly_added:
        for o in Localizable_list1:
            if os.path.splitext(o)[1] == ".lproj":
                # 提取语言
                if os.path.splitext(o)[0] != "en":
                    langue.append(os.path.splitext(o)[0])
                else:
                    continue

                if o == langue[-1] + ".lproj":
                    global langue_List
                    langue_List = []
                    with open(Localizable_path1 + "//" + o + "//""Localizable.txt", encoding="gb18030",
                              errors="ignore") as C:
                        d = re.findall('"'"(.*)"'" = "', C.read())
                        for j in d:
                            if j in newly_added:
                                langue_List.append(j)
                        if langue_List:
                            if len(langue_List) == len(newly_added):
                                pass
                            elif len(langue_List) < len(newly_added):
                                less_list = [i for i in newly_added if i not in langue_List]
                                print("【部分未翻译】" + langue[-1] + " 语言以下未翻译" + "\n" + str(less_list))
                        else:
                            Untranslated_Langue.append(langue[-1])
    print("【全部未翻译】：" + "\n" + str(Untranslated_Langue))

    print("三、【新增key值对应所有语言的value】：")
    if newly_added:
        for o in Localizable_list1:
            if os.path.splitext(o)[1] == ".lproj":
                # 提取语言
                langue.append(os.path.splitext(o)[0])
                if o == langue[-1] + ".lproj":
                    global value_List
                    value_List = []

                    with open(Localizable_path1 + "//" + o + "//""Localizable.txt", encoding="gb18030",
                              errors="ignore") as C:
                        d = re.findall('"'"(.*)"'" = "', C.read())
                        for j in d:
                            if j in newly_added:
                                with open(Localizable_path1 + "//" + o + "//""Localizable.txt", encoding="utf-8",
                                          errors="ignore") as T:
                                    e = re.findall(j + '"(.*)"', T.read())
                                    for n in e:
                                        key_value = '"' + j + '"' + n
                                        value_List.append(key_value)
                    if value_List:
                        print(langue[-1] + " 语新增：" + "\n" + str(value_List) + "\n")






if __name__ == '__main__':
    internationalization()
