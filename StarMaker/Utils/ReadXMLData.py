#coding=utf-8
#导入minidom类库
from xml.dom import minidom


class ReadXMLData(object,):
    # 定义方法，且接收传递的参数
    @staticmethod
    def returnXMLFile(fileName: object, first: object, two: object, ) -> object:
        # 使用parse，通过相对路径打开xml文件，读取模块为公用模块，文件名不能写死，用变量代替
        # noinspection PyTypeChecker
        Xfile = minidom.parse("../Data/" + fileName)
        # 基于xml文件定位一级标签，读取模块为公用模块，一级标签用变量代替
        OneNode = Xfile.getElementsByTagName(first)[0]
        # 基于一级标签获取二级标签的节点值
        TwoNode = OneNode.getElementsByTagName(two)[0].childNodes[0].nodeValue
        # 返回节点值
        return TwoNode
