# -*- encoding=utf8 -*-
__author__ = "yaoliang.cui"

from airtest.core.api import *
import sqlite3 as db

auto_setup(__file__)

# 从SQLite文件中读取数据
def readFronSqllite(db_path,exectCmd):
    conn = db.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor=conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory=db.Row     # 可访问列信息
    cursor.execute(exectCmd)    #该例程执行一个 SQL 语句
    rows=cursor.fetchall()      #该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    return rows
    #print(rows[0][2]) # 选择某一列数据

# 解析ARPA 单帧信息
def readfromAppaFrame(ARPAFrame):
    subARPA=ARPAFrame.split(',')
    print(subARPA)

if __name__=="__main__":
    rows=readFronSqllite('E://ARPA.db',"select ARPA from ARPAInfo")
    readLines=10010
    lineIndex=10000
    while lineIndex<readLines:
        row=rows[lineIndex] # 获取某一行的数据,类型是tuple
        content="".join(row) #tuple转字符串
        readfromAppaFrame(content) # 解析ARPA数据
        lineIndex+=1