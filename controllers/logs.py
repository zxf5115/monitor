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

from .base import BaseHandler
from models.logs import Logs

class LogsHandler(BaseHandler):

  # -----------------------------------------------------------------------
  # 得到当前用户

  @tornado.web.authenticated
  def get(self):

    logs = Logs().get_log_info()

    self.render("logs\\index.html", logs=logs)


