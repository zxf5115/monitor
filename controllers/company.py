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



class CompanyAddHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    self.render("company_add.html")






class CompanyHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    companies = get_companies()
    self.render("company.html", companies=companies)



  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    name_cn = self.get_argument("name_cn")
    name_en = self.get_argument("name_en")
    industry = self.get_argument("industry")

    if not name_cn:

      res["msg"] = "中文名称不能为空"
      self.finish(res)
      return

    if not name_en:

      res["msg"] = "英文名称不能为空"
      self.finish(res)
      return

    if not industry:

      res["msg"] = "所属行业不能为空"
      self.finish(res)
      return

    info = {
      "name_cn": name_cn,
      "name_en": name_en,
      "industry": industry
    }

    result = create_company(**info)

    if not result["success"]:

      res["msg"] = result["msg"]
      self.finish(res)

    else:

      res["success"] = True
      res["msg"] = "创建成功"
      res["company_id"] = result["company"].id
      self.write(res)




class CompanySearchHandler(BaseHandler):

  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    search_text = self.get_argument("search_text")
    company_list = search_company(search_text)
    self.render("company.html", companies=company_list)






class CompanyDeleteHandler(BaseHandler):

  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    company_id = self.get_argument("company_id")
    result = delete_company(company_id)

    if not result:

      res["msg"] = "删除失败"
      self.finish(res)

    else:

      res["success"] = True
      res["msg"] = "删除成功"
      self.write(res)
