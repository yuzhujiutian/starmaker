# coding=utf-8
from StarMaker.Utils.ReadXMLData import ReadXMLData

A = ReadXMLData().returnXMLFile(
    "dot_keys.xml", "Sing", "Click_LibraryRecommend_SingButton", path="./")
print(A)


if __name__ == '__main__':
    pass