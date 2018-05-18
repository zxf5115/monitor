#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：base.py
# 作者：zhangxiaofei
# 日期：2018-05-10
# 功能：基础类
# -------------------------------------------------------------------------


import tornado.web
import tornado.escape

from .base import BaseHandler


class MainHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    name = tornado.escape.xhtml_escape(self.current_user)
    self.write("Hello, " + name)
