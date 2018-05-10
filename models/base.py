#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# 程序：base.py
# 作者：zhangxiaofei
# 日期：2018-05-09
# 功能：model基础类
# -------------------------------------------------------------------------

import os
import uimodules
import tornado.ioloop
import tornado.web
import tornado.locale
import tornado.escape
from tornado.options import define, options

from ..database.mysql import Mysql


define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, type=bool)



class Base:

  table_name = ''




  def __init__(self, table_name):

    # 获取连接对象
    self.handle = Mysql.connection()
