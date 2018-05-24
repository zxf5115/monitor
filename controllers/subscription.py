#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：base.py
# 作者：zhangxiaofei
# 日期：2018-05-10
# 功能：基础类
# -------------------------------------------------------------------------


import tornado.ioloop
import tornado.web
import tornado.locale
import tornado.escape
from tornado.options import define, options

from .base import BaseHandler
from models.users import Users

class SubscriptionHandler(BaseHandler):
  @tornado.web.authenticated
  def get(self):
    self.render("subscription\\index.html")

  @tornado.web.authenticated
  def post(self):
    res = {"success": False, "msg": ""}
    email = self.get_argument("email")
    info = {
      "username": '订阅者',
      "email": email,
      "password": 'globus#2017#subscription'
    }
    result = create_user(**info)
    if not result["success"]:
      res["msg"] = result["msg"]
      self.finish(res)
    else:
      res["success"] = True
      res["msg"] = "订阅成功"
      self.write(res)
