import os

GetPath = os.path.split(os.path.realpath(__file__))
PackagePath = GetPath[0] + "\\" + GetPath[1]
print(PackagePath)


# 后期设计——自动拼接Path组成Button
if __name__ == '__main__':
    pass