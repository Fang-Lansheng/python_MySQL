#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  Transfer-Accounts.py
@Time    :  2018/10/21 21:34
"""
import sys
import pymysql

class TransferMoney(object):
    # 构造函数
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)    # 检查账户是否有效
            # self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money) # 检查余额是否足够
            self.reduce_money(source_acctid, money)     # 扣款
            self.add_money(target_acctid, money)        # 收款
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s" % acctid
            cursor.execute(sql)
            print('check_acct_available:\t', sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号 %s 不存在！' % acctid)
        finally:
            cursor.close()


    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>%s" % (acctid, money)
            cursor.execute(sql)
            print('has_enough_money:\t', sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号 %s 余额不足！' % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print('reduce_money:\t\t', sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception('账号 %s 扣款失败！' % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print('add_money:\t\t', sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception('账号 %s 收款失败！' % acctid)
        finally:
            cursor.close()


if __name__ == '__main__':
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    # 连接数据库
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='Thistledown',
        passwd='123456',
        db='python_MySQL',
        charset='utf8'
    )
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print('出现了问题', str(e))
    finally:
        conn.close()


