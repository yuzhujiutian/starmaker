#coding=utf-8
# 导入生成测试报告模块
import HTMLTestRunner


class CreatTestReporter(object):
    # 定义方法，并接受调用模块传递的参数
    @staticmethod
    def HTMLReporter(fileName, RevT, RevDes, RevTest, RevTester="最棒QA"):
        # 找到存储的测试报告，公用模块不能写死
        fileHtmlName = "../TestReport/" + fileName + ".html"
        # 打开测试报告，以二进制形式写入，并存储在内存空间中
        with open(fileHtmlName, "wb") as htmlSteam:
            HTMLTestRunner.HTMLTestRunner(
                stream=htmlSteam,
                verbosity=2,
                title=RevT,
                description=RevDes,
                tester=RevTester
            ).run(RevTest)
        htmlSteam.close()
