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


class IndexHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    self.render("index.html")




# define("port", default=8888, help="run on the given port", type=int)
# define("debug", default=True, type=bool)




# class MainHandler(BaseHandler):

#   @tornado.web.authenticated
#   def get(self):

#     name = tornado.escape.xhtml_escape(self.current_user)
#     self.write("Hello, " + name)


# class RegisterHandler(tornado.web.RequestHandler):

#   def get(self):
#     self.render("register.html")

#   def post(self):
#     res = {"success": False, "msg": ""}
#     username = self.get_argument("username")
#     email = self.get_argument("email")
#     password = self.get_argument("password")
#     confirm_password = self.get_argument("confirm_password")

#     if not username:
#       res["msg"] = "用户名不能为空"
#       self.finish(res)
#       return

#     if not email:
#       res["msg"] = "邮箱不能为空"
#       self.finish(res)
#       return

#     if not password:
#       res["msg"] = "密码不能为空"
#       self.finish(res)
#       return

#     if confirm_password != password:
#       res["msg"] = "密码不一致"
#       self.finish(res)
#       return

#     info = {
#       "username": username,
#       "email": email,
#       "password": password
#     }
#     result = create_user(**info)

#     if not result["success"]:

#       res["msg"] = result["msg"]
#       self.finish(res)

#     else:

#         res["success"] = True
#         res["msg"] = "注册成功"
#         self.write(res)


# class LoginHandler(tornado.web.RequestHandler):

#   def get(self):
#     self.render("login.html")

#   def post(self):
#     email = self.get_argument("email")
#     password = self.get_argument("password")
#     auth = authenticate(email=email, password=password)

#     if auth["success"]:

#       self.set_secure_cookie("user", str(auth["user_id"]))

#     self.write(auth)


# class LogoutHandler(tornado.web.RequestHandler):

#   @tornado.web.authenticated
#   def get(self):

#     self.clear_cookie("user")
#     self.redirect("/index")
