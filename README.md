# python_MySQL

Python 操作 MySQL 数据库
###### 课程地址：[Python操作MySQL数据库](https://www.imooc.com/learn/475)
`2018年10月20日` `Python` `MySQL`  
[TOC]

## 课程介绍

![](https://ws1.sinaimg.cn/large/006y42ybly1fwf1q63gvvj30ln0gqjul.jpg)

**课程目标：**

> 能够开发完整的数据库操作程序



**课程内容：**

- Python 访问 DB 的官方接口规范
- Python 开发 DB 程序的开发环境
- Python 访问 DB 的 connection、cursor 两大对象
- 完整实例：银行转账实现



## Python DB API

- 背景：没有 Python DB API 之前，接口程序混乱

  ![](https://ws1.sinaimg.cn/large/006y42ybgy1fwevmugp4lj30zd0ejjxy.jpg)

- Python DB API：Python 访问数据库的统一接口规范

  - 官方说明文档：https://www.python.org/dev/peps/pep-0249/

    ![](https://ws1.sinaimg.cn/large/006y42ybly1fwf1qgs6h0j30w50dldk5.jpg)

  - 包含内容：

    ![](https://ws1.sinaimg.cn/large/006y42ybgy1fwevttpe4ej30ux0a47am.jpg)

  - 使用 Python DB API 访问数据库的流程

    ![](https://ws1.sinaimg.cn/large/006y42ybgy1fwevvgz25nj30vv0ftwik.jpg)

## Python 开发 MySQL 环境

![](https://ws1.sinaimg.cn/large/006y42ybly1fwf1pdpd4tj30qx0f543i.jpg)



Python connector 的安装：

> MySQLdb下载地址：https://sourceforge.net/projects/mysql-python/

Python 3 中不支持 MySQLdb，可以用 PyMySQL代替。

命令行中：

```powershell
pip install PyMySQL
```

在项目中的 `__init_.py` 文件中添加：

```python
import pymysql
pymysql.install_as_MySQLdb()
```

就可以成功 `import MySQLdb` 了。其他的方法与 MySQLdb 一样。

使用 MySQL 自带的 SQLyog 或者 MySQL Workbench 进行管理。

![](https://ws1.sinaimg.cn/large/006y42ybly1fwfsj1ooxdj30wy0otwg2.jpg)



## DB API - 数据库连接对象 connection

- 连接对象：建立 Python 客户端与数据库的网络连接
- 创建方法：MySQLdb.Connect（参数）

| 参数名  | 类型   | 说明               |
| :------ | :----- | :----------------- |
| host    | 字符串 | MySQL 服务器地址   |
| port    | 数字   | MySQL 服务器端口号 |
| user    | 字符串 | 用户名             |
| passwd  | 字符串 | 密码               |
| db      | 字符串 | 数据库名称         |
| charset | 字符串 | 连接编码           |

- connection 对象支持的方法：

  | 方法名     | 说明                     |
  | :--------- | :----------------------- |
  | cursor()   | 使用该连接创建并返回游标 |
  | commit()   | 提交当前事务             |
  | rollback() | 回滚当前事务             |
  | close()    | 关闭连接                 |

## DB API - 数据库游标对象 cursor

- 游标对象：用于执行查询和获取结果

- cursor 对象支持的方法：

  | 参数名             | 说明                                      |
  | ------------------ | ----------------------------------------- |
  | execute(op[,args]) | 执行一个数据库查询和命令                  |
  | fetchone()         | 取得结果集的下一行                        |
  | fetchmany(size)    | 获取结果集的下几行                        |
  | fetchall()         | 获取结果集中剩下的所有行                  |
  | rowcount()         | 最近一次 execute 返回数据的行数或影响行数 |
  | close()            | 关闭游标对象                              |
  - execute 方法：执行 SQL、将结果从数据库获取到客户端

    ![](https://ws1.sinaimg.cn/large/006y42ybly1fwg3e74jxvj30ta0bl778.jpg)

  - fetch*() 方法：移动 rownumber，返回数据

    - rownumber 类似于数组的指针，移动指针，返回数据。相当于数组缓冲区的位置

    ![](https://ws1.sinaimg.cn/large/006y42ybly1fwg3hvt1upj31030eeq8l.jpg)

## 实例演示 —— SELECT 查询数据

![](https://ws1.sinaimg.cn/large/006y42ybly1fwg3jtqq70j30x50h4n2d.jpg)

在数据库中创建 user 表：

```sql
create table `user` (
	`userid` int(11) not null auto_increment,
    `username` varchar(100) default null,
    primary key(`userid`)
)	engine=InnoDB auto_increment=0 default charset=utf8
```

Python 文件代码：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

# SQL 语句
sql = 'SELECT * FROM user'
cursor.execute(sql)

print('行数 rowcount：', cursor.rowcount)

rs = cursor.fetchone()
print('获取第一行：', rs)

rs = cursor.fetchmany(3)
print(rs)

rs = cursor.fetchall()
for row in rs:
    print('userid = %s, username = %s' % row)

cursor.close()      # 管理连接
connect.close()     # 关闭连接
```

## 实例演示 —— INSERT/UPDATE/DELETE 更新数据库

![](https://ws1.sinaimg.cn/large/006y42ybly1fwg4lyjxxoj311b0hi7br.jpg)

### 事务

- 事务：访问和更新数据库的一个程序执行单元（很多操作的一个集合）
  - 原子性：事务中包括的诸操作要么都做，要么都不做
  - 一致性：数据必须使数据库从一致性状态变到另一个一致性状态
  - 隔离性：一个事务的提交不能被其他事务干扰
  - 持久性：事务一旦提交，它对数据库的改变就是永久性的
- 开发中怎样事务？
  - 关闭自动 commit：设置 connect.autocommit(False) __（默认为False）__
  - 正常结束事务：conn.commit()
  - 异常结束事务：conn.rollback()

## 银行转账实例

![](https://ws1.sinaimg.cn/large/006y42ybly1fwg5s3xyqaj30tz0gmq6g.jpg)

## 课程总结

- **Python DB API**
  - connection：建立数据库连接
  - cursor：执行 SQL、获取数据
- **开发数据库程序流程**
  - 创建 connection 对象，获取 cursor
  - 使用 cursor 执行 SQL
  - 使用 cursor 获取数据、判断执行状态
  - 提交事务 或者 回滚事务
  - 关闭 cursor、关闭 connection