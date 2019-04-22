# coding=utf-8
import os
import re

path1 = os.path.abspath("ktv_solo.txt")
path2 = os.path.abspath("ktv_multi.txt")
path3 = os.path.abspath("live.txt")
path4 = os.path.abspath("test.txt")
if path1:
    f = open(path1, "r", encoding='gbk', errors='ignore')
    try:
        text = f.read()
        room_id = re.findall(r',"room_id":(.+?),"index":', text)
        online_people_count = re.findall(r'":"","online_people_count":(.+?),"ndselect":', text)
    finally:
        f.close()
    correspond1 = dict(zip(room_id, online_people_count))
    print("【ktv_solo】'房间ID':'在线真实人数'")
    print(correspond1)
    print(online_people_count)
    # num = 0
    # print("【ktv_solo】排序有问题的房间ID:在线人数")
    # while num < len(correspond1)-1:
    #     if int(online_people_count[num]) < int(online_people_count[num+1]):
    #         A = list(correspond1.keys())[list(correspond1.values()).index(online_people_count[num])]
    #         B = list(correspond1.keys())[list(correspond1.values()).index(online_people_count[num+1])]
    #         print(A + ":" + online_people_count[num], B + ":" + online_people_count[num+1])
    #     num += 1


if path2:
    f = open(path2, "r", encoding='gbk', errors='ignore')
    try:
        text = f.read()
        room_id = re.findall(r',"room_id":(.+?),"index":', text)
        online_people_count = re.findall(r'":"","online_people_count":(.+?),"ndselect":', text)
    finally:
        f.close()
    correspond2 = dict(zip(room_id, online_people_count))
    print("【ktv_multi】'房间ID':'在线真实人数'")
    print(correspond2)
    print(online_people_count)
    # num = 0
    # print("【ktv_multi】排序有问题的房间ID:在线人数")
    # while num < len(correspond2)-1:
    #     if int(online_people_count[num]) < int(online_people_count[num+1]):
    #         A = list(correspond2.keys())[list(correspond2.values()).index(online_people_count[num])]
    #         B = list(correspond2.keys())[list(correspond2.values()).index(online_people_count[num+1])]
    #         print(A + ":" + online_people_count[num], B + ":" + online_people_count[num+1])
    #     num += 1


if path3:
    f = open(path3, "r", encoding='gbk', errors='ignore')
    try:
        text = f.read()
        live_id = re.findall(r',"live_id":(.+?),"index":', text)
        online_users = re.findall(r'":"","online_users":(.+?),"stream_info":', text)
    finally:
        f.close()
    correspond3 = dict(zip(live_id, online_users))
    print("【live】'房间ID':'在线真实人数+EVA'")
    print(correspond3)
    print(online_users)
    # num = 0
    # print("【live】排序有问题的房间ID:在线人数")
    # live_error_list = []
    # while num < len(correspond3) - 1:
    #     if int(online_users[num]) < int(online_users[num + 1]):
    #         A = list(correspond3.keys())[list(correspond3.values()).index(online_users[num])]
    #         B = list(correspond3.keys())[list(correspond3.values()).index(online_users[num + 1])]
    #         live_error_list.append(A)
    #         live_error_list.append(B)
    #     num += 1
    # print(live_error_list)


if path4:
    f = open(path4, "r", encoding='gbk', errors='ignore')
    try:
        text = f.read()
        user_id = re.findall(r'{"id":"(.+?)","name":"', text)
    finally:
        f.close()
    print(len(user_id))
    print(user_id)

if __name__ == '__main__':
    pass
