#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：base.py
# 作者：zhangxiaofei
# 日期：2018-05-10
# 功能：基础类
# -------------------------------------------------------------------------


import tornado.web

from .base import BaseHandler

class LogoutHandler(tornado.web.RequestHandler):

  @tornado.web.authenticated
  def get(self):

    self.clear_cookie("user")
    self.redirect("/index")
