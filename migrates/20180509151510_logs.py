#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：00000000000001_migration.py
# 作者：zhangxiaofei
# 日期：2018-05-02
# 功能：migration
# -------------------------------------------------------------------------

import os
import sys
import time

# 获得文件当前路径os.path.abspath 获得文件的父目录os.path.dirname
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(BASE_DIR)

from libs.migrate.migration import Migration

class Model(Migration):

  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, table_name):

    super().__init__(table_name)

    self.filename = os.path.basename(__file__)

    if self.exists():

      exit()





  def exists(self):

    sql = "select id from migration where version = '%s'" % (self.filename)

    return self.select(sql)



  # -----------------------------------------------------------------------
  # 向migration表中添加当前版本的命令

  def migration(self):

    try:

      timestamp = int(time.time())

      sql = "insert into migration (version, create_time) values (%s,%s)"
      data= [[self.filename, timestamp]]

      self.insert(sql, data)

    except Exception as e:

      print(e)





  # -----------------------------------------------------------------------
  # 执行创建命令

  def up(self):

    try:

      self.primary('id', 11, '自增编号')

      self.tinyint('level', 1, 1, '级别')

      self.text('text', '信息')

      self.integer('create_time', 10, 0, '创建时间')

      self.primary_key('id')

      self.engine()

      self.charset()

      self.comment('日志信息表')

      self.create()

      print('创建成功')

      self.migration()

    except Exception as e:

      print(e)

    finally:

      self.add()


  def add(self):

    try:

      pass

      # timestamp = int(time.time())

      # sql = "insert into logs (version, create_time) values (%s,%s)"
      # data= [['00000000000001_migration.py', timestamp]]

      # self.insert(sql, data)

    except Exception as e:

      print(e)



if __name__ == '__main__':

  model = Model('logs')
  model.up()
