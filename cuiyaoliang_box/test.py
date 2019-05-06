# coding=utf-8
import pymysql
# from cuiyaoliang_box import host_analysis


# def sql_query(databases, sql):
       # # 如果databases是字符串
       # if isinstance(databases, str):
       #        db = host_analysis.host_analysis[databases]
       # # 如果databases是列表
       # elif isinstance(databases, list):
       #        for i in databases:
       #               db = host_analysis.host_analysis[i]


def test():
    con = pymysql.connect(
        host='172.16.3.148',
        port=3306,
        user='readonly',
        passwd='JKw6woZgRXsveegL',
        db='mysql',
        charset='utf8')

    cur = con.cursor()
    show_databases = "show databases"
    show_tables = "show tables"
    show_columns = "show columns from db"
    cur.execute(show_databases)
    row1 = cur.fetchall()
    print("databases")
    print(row1)
    print(len(row1))
    cur.execute(show_tables)
    row2 = cur.fetchall()
    print("tables")
    print(row2)
    print(len(row2))
    cur.execute(show_columns)
    row3 = cur.fetchall()
    print("columns")
    print(row3)
    print(len(row3))

    con.close()


if __name__ == '__main__':
    # sql = "select * from mis where sm_id = 262364731;"
    # sql_query(sql)
    test()
