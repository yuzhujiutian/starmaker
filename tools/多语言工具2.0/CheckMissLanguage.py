# coding=utf-8
import re
import os


def internationalization():
    Localizable_path = ".//锘縇ocalizable"
    Localizable_list = os.listdir(Localizable_path)
    langue = []
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
                with open(Localizable_path + "//" + i + "//""Localizable.txt", encoding="gb18030", errors="ignore") as C:
                    D = re.findall('"'"(.*)"'" = "', C.read())
                    for j in D:
                        en_List.append(j)

    for o in Localizable_list:
        if os.path.splitext(o)[1] == ".lproj":
            # 提取语言
            if os.path.splitext(o)[0] != "en":
                langue.append(os.path.splitext(o)[0])
            else:
                continue

            if o == langue[-1] + ".lproj":
                global langue_List
                langue_List = []
                with open(Localizable_path + "//" + o + "//""Localizable.txt", encoding="gb18030", errors="ignore") as C:
                    D = re.findall('"'"(.*)"'" = "', C.read())
                    for j in D:
                        langue_List.append(j)

            # 检查多语言
            ExpectText = en_List
            ActuallyText = langue_List
            TextList = []
            for index in range(len(ActuallyText)):
                TextList.append(ActuallyText[index])
            if ExpectText == TextList:
                return True
            else:
                LessThanExpected = [i for i in ExpectText if i not in TextList]
                MoreThanExpected = [i for i in TextList if i not in ExpectText]
                # 比预期少了
                if LessThanExpected:
                    print("\n" + langue[-1] + "比en少了 " + str(len(LessThanExpected)) + " 个")
                    print(LessThanExpected)
                # 比预期多了
                elif MoreThanExpected:
                    print("\n" + langue[-1] + "比en多了 " + str(len(MoreThanExpected)) + " 个")
                    print(MoreThanExpected)
                # 排序不正确或未取到
                else:
                    print("执行错误")
                    print("预期结果:", ExpectText)
                    print("实际结果:", TextList)
                    return False




if __name__ == '__main__':
    internationalization()