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




class ContactAddHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self, company_id):

    company = get_company(company_id)
    profile = get_profile(company_id)
    contact = get_contact(company_id)
    self.render("contact_add.html", company=company, profile=profile, contact=contact)




  @tornado.web.authenticated
  def post(self, company_id):

    res = {"success": False, "msg": ""}
    fullname = self.get_argument("fullname")

    if not fullname:

      res["msg"] = "用户名不能为空"
      self.finish(res)
      return

    contact_info = {
      "company_id": company_id,
      "name": fullname,
      "gender": self.get_argument("gender"),
      "position": self.get_argument("position"),
      "phone_number": self.get_argument("phone_number"),
      "wechat": self.get_argument("wechat"),
      "email": self.get_argument("email"),
      "comment": self.get_argument("comment"),
    }

    result = create_contact(**contact_info)

    if not result['success']:

      res["success"] = False
      res["msg"] = result["msg"]
      self.finish(res)

    else:

      res["success"] = True
      res["msg"] = "提交成功"
      self.write(res)


class ContactDeleteHandler(BaseHandler):

  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    contact_id = self.get_argument("contact_id")
    result = delete_contact(contact_id)

    if not result:

      res["msg"] = "删除失败"
      self.finish(res)

    else:

      res["success"] = True
      res["msg"] = "删除成功"
      self.write(res)

