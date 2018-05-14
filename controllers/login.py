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

from models.users import Users

class LoginHandler(tornado.web.RequestHandler):

  def get(self):
    self.render("login/login.html")

  def post(self):
    email = self.get_argument("email")
    password = self.get_argument("password")
    auth = Users().authenticate(email=email, password=password)

    if auth["success"]:

      self.set_secure_cookie("user", str(auth["user_id"]))

    self.write(auth)
