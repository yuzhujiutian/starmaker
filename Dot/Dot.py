import requests
import city
import json
import jsonpath
import re

city_list = city.jsons
tags_list = city.Tag

def city_func(city_id):
    try:
        city = jsonpath.jsonpath(city_list, '$..sub[?(@.code=={})]'.format(int(city_id)))[0]["name"]
    except:
        city = jsonpath.jsonpath(city_list, '$[?(@.code=={})]'.format(int(city_id)))[0]["name"]
    return city

def tags_func(tags_id):
    tags_join = []
    if tags_id:
        for tags in tags_id:
            t = jsonpath.jsonpath(tags_list,'$..spotFilterTags[?(@.id=={})]'.format(int(tags)))
            tags_join.append(t[0]["title"])

    return ('-'.join(tags_join))

def split_n(ags):
    return re.sub('\n','  ',ags)


def request(page):
    print('开始下载第%d页'%page)
    url = 'https://app-api.chargerlink.com/spot/searchSpot'
    two_url = "https://app-api.chargerlink.com/spot/getSpotDetail?spotId={d}"
    head = {
        "device": "client=android&cityName=%E5%8C%97%E4%BA%AC%E5%B8%82&cityCode=110106&lng=116.32154281224254&device_id=8A261C9D60ACEBDED7CD3706C92DD68E&ver=3.7.7&lat=39.895024107858724&network=WIFI&os_version=19",
        "appId": "20171010",
        "timestamp": "1532342711477",
        "signature": "36daaa33e7b0d5d29ac9c64a2ce6c4cf",
        "forcecheck": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "68",
        "Host": "app-api.chargerlink.com",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/3.2.0"
    }


    data = {
        "userFilter[operateType]": 2,
        "cityCode": 110000,
        "sort": 1,
        "page": page,
        "limit": 10,
    }

    response = requests.post(url,data=data,headers=head)
    #获取数据
    data = response.json()
    for i in data['data']:
        c = []
        id = i['id']
        name = i["name"] #充电桩名
        phone = i["phone"] #手机号
        num = i['quantity'] #有几个充电桩
        city = city_func(i["provinceCode"]) #城市
        tags =tags_func(i["tags"].split(','))#标签
        message = c + [id,name,phone,num,city,tags]
        parse_info(two_url.format(d=id),message)

def parse_info(url,message):

    #打开文件
    with open('car.csv','a',encoding='utf-8')as c:
        head = {
            "device": "client=android&cityName=&cityCode=&lng=116.32154281224254&device_id=8A261C9D60ACEBDED7CD3706C92DD68E&ver=3.7.7&lat=39.895024107858724&network=WIFI&os_version=19",
            "TOKEN": "036c8e24266c9089db50899287a99e65dc3bf95f",
            "appId": "20171010",
            "timestamp": "1532357165598",
            "signature": "734ecec249f86193d6e54449ec5e8ff6",
            "forcecheck": "1",
            "Host": "app-api.chargerlink.com",
            "Connection": "Keep-Alive",
            "User-Agent": "okhttp/3.2.0",
        }
        #发起详情请求
        res = requests.get(url,headers=head)
        price = split_n(jsonpath.jsonpath(json.loads(res.text),'$..chargingFeeDesc')[0]) #价钱
        payType = jsonpath.jsonpath(json.loads(res.text),'$..payTypeDesc')[0] #支付方式
        businessTime =split_n(jsonpath.jsonpath(json.loads(res.text),'$..businessTime')[0]) #营业时间
        result = (message + [price,payType,businessTime])
        r = ','.join([str(i) for i in result])+',\n'
        c.write(r)

def get_page():
    url = 'https://app-api.chargerlink.com/spot/searchSpot'
    head = {
        "device": "client=android&cityName=%E5%8C%97%E4%BA%AC%E5%B8%82&cityCode=110106&lng=116.32154281224254&device_id=8A261C9D60ACEBDED7CD3706C92DD68E&ver=3.7.7&lat=39.895024107858724&network=WIFI&os_version=19",
        "appId": "20171010",
        "timestamp": "1532342711477",
        "signature": "36daaa33e7b0d5d29ac9c64a2ce6c4cf",
        "forcecheck": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "68",
        "Host": "app-api.chargerlink.com",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/3.2.0"
    }

    data = {
        "userFilter[operateType]": 2,
        "cityCode": 110000,
        "sort": 1,
        "page": 1,
        "limit": 10,
    }
    response = requests.post(url, data=data, headers=head)
    # 获取数据
    data = response.json()
    total = (data["pager"]["total"])
    page_Size = (data["pager"]["pageSize"])
    totalPage = (data['pager']["totalPage"])
    print('当前共有{total}个充电桩，每页展示{page_Size}个，共{totalPage}页'.format(total=total,page_Size=page_Size,totalPage=totalPage))
if __name__ == '__main__':
    get_page()
    start = int(input("亲,请输入您要获取的开始页:"))
    end = int(input("亲,请输入您要获取的结束页:"))
    for  i in range(start,end+1):
        request(i)