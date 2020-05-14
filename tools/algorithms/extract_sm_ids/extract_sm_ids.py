# coding=utf-8
import re
import sys
# 获取当前工作路径
current_working_path = sys.path[0]
sm_ids = []

# 读取数据文件
with open(current_working_path + '/originals.txt', 'r') as f:
    originals_file = f.read()

# 提取sm_id
sm_id = re.findall('{"sm_id":"' + '(.\d+)', originals_file)
for i in sm_id:
    sm_ids.append(int(i))

# 存储到txt文件中
with open(current_working_path + '/sm_id_list.txt', 'w+') as g:
    for j in sm_ids:
        g.write(str(j) + "\n")

print("done")

if __name__ == '__main__':
    pass
