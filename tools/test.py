# coding=utf-8
import pymysql


# "starmaker-device-r2.db" = "172.16.7.107"
# "sm-img-r2" = "172.16.2.140"
# "starmaker-final-r2.db" = "172.16.4.39"
con = pymysql.connect(
       host='172.16.7.28',
       port=3306,
       user='readonly',
       password='https://phabricator.ushow.media/K47',
       charset='utf8')

cur = con.cursor()
row = cur.execute("show databases")


if __name__ == '__main__':
    pass
