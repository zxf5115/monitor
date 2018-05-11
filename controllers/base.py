#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：base.py
# 作者：zhangxiaofei
# 日期：2018-05-10
# 功能：基础类
# -------------------------------------------------------------------------

import os
import tornado.ioloop
import tornado.web
import tornado.locale
import tornado.escape
from tornado.options import define, options

class BaseHandler(tornado.web.RequestHandler):

  def __init__(self):

    pass

  # -----------------------------------------------------------------------
  # 得到当前用户

  def get_current_user(self):

    user_id = self.get_secure_cookie("user")

    if not user_id:

      return None

    user = get_user(u_id=int(user_id))

    return user
