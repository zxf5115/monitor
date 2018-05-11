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
