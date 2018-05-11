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

from base import BaseHandler



define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, type=bool)




class UserManageHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    users = get_users()
    self.render("user_manage.html", users=users)


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

