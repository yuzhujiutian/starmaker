# coding=utf-8
import re
import sys
from io import BytesIO

import requests
from PIL import Image

# 获取当前工作路径
current_working_path = sys.path[0]


# 批量爬取图片
def get_picture(url, Initial_value=1568621396468, number=1000):
    success_num = 0
    code_error = 0
    transcoding_error = 0
    while number:
        number -= 1
        Initial_value += 1
        get_jpg = requests.get(url +
                               str(Initial_value) + "-270x270.jpg")
        try:
            code = re.findall('{"meta":{"code":' + '(.*)' + ',"error_message":"', str(get_jpg.content))[0]
            if code == "404":
                code_error += 1
                print("图片未找到" + str(code_error))
                number += 1
        except IndexError:
            try:
                jpg = Image.open(BytesIO(get_jpg.content))
                jpg.save(current_working_path + "\\" + str(Initial_value) + ".png", "png")
                success_num += 1
                print("图片保存成功" + str(success_num))
            except:
                transcoding_error += 1
                print("图片转存错误" + str(transcoding_error))
                number += 1


if __name__ == '__main__':
    get_picture(url="")
