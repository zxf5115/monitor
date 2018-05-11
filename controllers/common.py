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

    """
    获取所有个公司的feed
    """
    @tornado.web.authenticated
    def get(self):

      print(1)
      exit()
      # feeds = get_info_feed(TIME_LIMIT)
      # oversea_feeds = get_oversea_info_feed(TIME_LIMIT)
      # total_page = len(feeds) // ITEMS_NUM_PERPAGE + 1
      # page_num = 1
      # start = ITEMS_NUM_PERPAGE * (page_num - 1)
      # end = ITEMS_NUM_PERPAGE * page_num
      # feeds = feeds[start:end]

      # self.render("information.html", feeds=feeds, oversea_feeds=oversea_feeds, total_page=total_page,
      #             current_page=page_num)








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
