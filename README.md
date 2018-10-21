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



### 一、Python DB API

- 背景：没有 Python DB API 之前，接口程序混乱

  ![](https://ws1.sinaimg.cn/large/006y42ybgy1fwevmugp4lj30zd0ejjxy.jpg)

- Python DB API：Python 访问数据库的统一接口规范

  - 官方说明文档：https://www.python.org/dev/peps/pep-0249/

    ![](https://ws1.sinaimg.cn/large/006y42ybly1fwf1qgs6h0j30w50dldk5.jpg)

  - 包含内容：

    ![](https://ws1.sinaimg.cn/large/006y42ybgy1fwevttpe4ej30ux0a47am.jpg)

  - 使用 Python DB API 访问数据库的流程

    ![](https://ws1.sinaimg.cn/large/006y42ybgy1fwevvgz25nj30vv0ftwik.jpg)

### 二、Python 开发 MySQL 环境

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

使用 MySQL 自带的 MySQL Workbench 进行管理