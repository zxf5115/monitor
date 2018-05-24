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

class UserHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    users = Users().get_user_info(1, '*')
    print(users[0])
    self.render("users\\index.html", users=users)


  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    username = self.get_argument("username")
    password = self.get_argument("password")
    email    = self.get_argument("email")

    confirm_password = self.get_argument("confirm_password")

    if not username:
      res["msg"] = "用户名不能为空"
      self.finish(res)
      return

    if not email:
      res["msg"] = "邮箱不能为空"
      self.finish(res)
      return

    if not password:
      res["msg"] = "密码不能为空"
      self.finish(res)
      return

    if confirm_password != password:
      res["msg"] = "密码不一致"
      self.finish(res)
      return

    info = {
      "username": username,
      "email": email,
      "password": password
    }
    result = Users().create_user(**info)

    if not result["success"]:

      res["msg"] = result["msg"]
      self.finish(res)

    else:

      res["success"] = True
      res["msg"] = "注册成功"
      self.write(res)





class UserAddHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    self.render("users\\add.html")




class UserEditHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    self.render("users\\edit.html")




class UserSearchHandler(BaseHandler):

  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    keyword = self.get_argument("keyword")

    where = r"`username` LIKE %'%s'%" % (keyword)

    users = Users().get_user_info(where, '*')

    self.render("users\\index.html", users=users)









class UserDeleteHandler(BaseHandler):

  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    user_id = self.get_argument("user_id")
    result = delete_user(user_id)

    if not result:

      res["msg"] = "删除失败"
      self.finish(res)

    else:

      res["success"] = True
      res["msg"] = "删除成功"
      self.write(res)

