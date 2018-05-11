#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# 程序：base.py
# 作者：zhangxiaofei
# 日期：2018-05-09
# 功能：model基础类
# -------------------------------------------------------------------------

from libs.database.mysql import Mysql

class Base:

  table_name = ''

  def __init__(self):

    # 获取连接对象
    self.handle = Mysql.connection()



  # -----------------------------------------------------------------------
  # 新增数据

  def insert(self, field, value):

    return self.handle.insert(self.table_name, field, value)







  # -----------------------------------------------------------------------
  # 删除数据

  def delete(self, where = ""):

    return self.handle.delete(self.table_name, where)




  # -----------------------------------------------------------------------
  # 更新数据

  def update(self, field, value, where = ""):

    return self.handle.update(self.table_name, field, value, where)





  # -----------------------------------------------------------------------
  # 查询数据

  def select(self, field = '*', where = "", group = "", order = ""):

    return self.handle.select(self.table_name, field, where, group, order)
