# coding=utf-8
import os
images_path = "../TestReport/images/"
images_list = os.listdir(images_path)
for i in images_list:
    images = os.path.join(images_path, i)
    print(images)
    Suffix = os.path.splitext(i)[1]
    print(Suffix)
    if Suffix == ".png":
        os.remove(images)



if __name__ == '__main__':
    pass
