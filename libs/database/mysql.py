#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：mysql.py
# 作者：zhangxiaofei
# 日期：2018-04-28
# 功能：Mysql操作类
# -------------------------------------------------------------------------

import pymysql
from ..conf.conf import Conf

class Mysql:


  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, host, username, password, dbname, port=3306):

    # 打开数据库连接
    self.db = pymysql.connect(host=host, port=port, user=username, passwd=password, db=dbname, charset='utf8')



  @classmethod
  def connection(self):

    # 获取配置
    conf = Conf()

    # 得到mysql配置文件
    host, username, password, dbname, port = conf.get_mysql_conf_info()

    # 打开数据库连接
    db = Mysql(host, username, password, dbname, int(port))

    return db




# -----------------------------------------------------------------------
  # 插入数据表操作

  def insert(self, table, field, value):

    # 使用cursor()方法获取操作游标
    cursor = self.db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, field, value)

    try:
      # 执行sql语句
      cursor.execute(sql)
      # 提交到数据库执行
      self.db.commit()
    except Exception as e:
      print(e)
      # 如果发生错误则回滚
      self.db.rollback()

    # 关闭游标
    cursor.close()




  # -----------------------------------------------------------------------
  # 删除数据

  def delete(self, table, where = "1"):

    # 使用cursor()方法获取操作游标
    cursor = self.db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM `%s` WHERE %s" % (table, where)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交修改
       self.db.commit()
    except:
       # 发生错误时回滚
       self.db.rollback()

    # 关闭连接
    db.close()




  # -----------------------------------------------------------------------
  # 更新数据

  def update(self, table, field, value, where = "1"):

    # 使用cursor()方法获取操作游标
    cursor = self.db.cursor()

    # SQL 更新语句
    sql = "UPDATE `%s` SET `%s` = '%s' WHERE %s " % (table, field, value, where)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交到数据库执行
       self.db.commit()
    except:
       # 发生错误时回滚
       self.db.rollback()

    # 关闭数据库连接
    db.close()




  # -----------------------------------------------------------------------
  # 查询数据
  # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
  # fetchall(): 接收全部的返回结果行.
  # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

  def select(self, table, field = '*', where = "1", group = "", order = ""):

    # 使用cursor()方法获取操作游标
    cursor = self.db.cursor()

    # SQL 查询语句
    sql = "SELECT %s FROM %s WHERE %s %s %s " % (field, table, where, group, order)

    try:
      # 执行SQL语句
      cursor.execute(sql)

      # 返回查询结果
      return cursor.fetchall()
    except:
      print ("Error: unable to fetch data")

    # 关闭游标
    cursor.close()

    # 关闭数据库连接
    self.close()





  # -----------------------------------------------------------------------
  # 查询数据
  # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
  # fetchall(): 接收全部的返回结果行.
  # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

  def find(self, table, field = '*', where = "1", group = "", order = ""):

    # 使用cursor()方法获取操作游标
    cursor = self.db.cursor()

    # SQL 查询语句
    sql = "SELECT %s FROM %s WHERE %s %s %s " % (field, table, where, group, order)

    try:
      # 执行SQL语句
      cursor.execute(sql)

      # 返回查询结果
      return cursor.fetchone()
    except:
      print ("Error: unable to fetch data")

    # 关闭游标
    cursor.close()

    # 关闭数据库连接
    self.close()







  # -----------------------------------------------------------------------
  # 创建表

  def execute(self, sql):

    conn = self.db.cursor()

    result = conn.execute(sql)

    conn.close()

    return result




  def executemany(self, sql, data):

    conn = self.db.cursor()

    conn.executemany(sql, data)

    result = self.db.commit()

    conn.close()

    return result


