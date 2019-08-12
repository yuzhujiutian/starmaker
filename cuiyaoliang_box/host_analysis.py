# coding=utf-8
# 数据表结构
# https://phabricator.ushow.media/w/%E6%9C%8D%E5%8A%A1%E7%AB%AF%E6%96%87%E6%A1%A3/%E6%95%B0%E6%8D%AE%E8%A1%A8%E7%BB%93%E6%9E%84/
host_analysis = {
    # 用户基本信息
    "shard": {
        "IP": {
            "shard00-r2.db": "172.16.3.202",
            "shard01-r2.db": "172.16.3.148",
            "shard02-r2.db": "172.16.4.1",
            "shard03-r2.db": "172.16.3.194"
        },
        "databases": [
            "id",
            "mysql",
            "shard_sm_0",
            "shard_sm_1",
            "shard_sm_2",
            "shard_sm_3",
            "shard_sm_4",
            "shard_sm_5",
            "shard_sm_16",
            "shard_sm_17",
            "information_schema",
            "performance_schema"
        ]
    },

    # 用户身份
    "starmaker-final-r2.db": "172.16.4.39",
    # 作品信息
    "sm-img-r2": "172.16.2.140",
    # 其他
    "starmaker-backend-r2.db": "172.16.4.104",
    "es.master2": "172.16.3.137",
    "starmaker-live-r2.db": "172.16.4.124",
    "zookeeper2": "172.16.0.129",
    # mis
    "starmaker-device-r2.db": "172.16.7.107"
}


if __name__ == '__main__':
    A = ['information_schema','id','mysql','performance_schema','shard_sm_0','shard_sm_1','shard_sm_2','shard_sm_3','shard_sm_4','shard_sm_5','shard_sm_16','shard_sm_17','sys','test','tmp']
    print set(A)