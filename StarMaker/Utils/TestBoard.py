# coding=utf-8
class PopupProcessing:
    # 查找弹窗，如果存在则返回True
    def Popup_GeneralMethod(self, **elements):
        # **为可传项；如果该元素有text属性，传入**text时会判断精确符合。
        for key in elements:
            global element
            element = elements.get(key)
            if key == "ID":
                PopupProcessing().ID()
            else:
                print("key 错误")
                print(key)
                return False

    # 1.ID = [ID, **text]
    def ID(self):
        # 提取键值
        ID = element
        print(ID)
        print("ID类型为")
        print(type(ID))
        # 如果值是字符串
        if len(ID) == 1:
            print("str")
        # 如果值是列表
        elif len(ID) == 2:
            print("list")
        # 否则返回值的属性


# PopupProcessing().Popup_GeneralMethod(ID=["com.android.packageinstaller:id/permission_message", "ABC"])
# PopupProcessing().Popup_GeneralMethod(ID="com.android.packageinstaller:id/permission_message")


if __name__ == '__main__':
    pass
