#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  MySQLdb_Test.py
@Time    :  2018/10/21 14:41
"""

# 引入模块
import pymysql

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='Thistledown',
    passwd='123456',
    db='python_MySQL',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

# sql = 'SELECT * FROM user'
# cursor.execute(sql)
#
# rs = cursor.fetchall()
# for row in rs:
#     print('userid = %s, username = %s' % row)

sql_insert = "INSERT INTO user(userid, username) VALUES(10, 'name10')"
sql_update = "UPDATE user set username='name91' WHERE userid=9"
sql_delete = "DELETE FROM user WHERE userid<3"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)

    connect.commit()
except Exception as e:
    print(e)
    connect.rollback()

# # SQL 语句
# sql = 'SELECT * FROM user'
# cursor.execute(sql)
#
# print('行数 rowcount：', cursor.rowcount)
#
# rs = cursor.fetchone()
# print('获取第一行：', rs)
#
# rs = cursor.fetchmany(3)
# print(rs)
#
# rs = cursor.fetchall()
# print(rs)

cursor.close()      # 管理连接
connect.close()     # 关闭连接


