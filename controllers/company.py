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
from models.company import Company

class CompanyHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    companies = Company().get_company_info(1, '*')

    self.render("company\\index.html", companies=companies)



  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}

    chinese_name = self.get_argument("chinese_name")
    english_name = self.get_argument("english_name")
    industry = self.get_argument("industry")
    website = self.get_argument("website")
    description = self.get_argument("description")

    if not chinese_name:

      res["msg"] = "中文名称不能为空"
      self.finish(res)
      return

    if not english_name:

      res["msg"] = "英文名称不能为空"
      self.finish(res)
      return

    if not industry:

      res["msg"] = "所属行业不能为空"
      self.finish(res)
      return

    info = {
      "chinese_name": chinese_name,
      "english_name": english_name,
      "industry": industry,
      "website": website,
      "description": description
    }

    result = Company().create_company(**info)

    if not result["success"]:

      res["msg"] = result["msg"]
      self.finish(res)

    else:

      res["success"] = True
      res["msg"] = "创建成功"
      res["company_id"] = result["company"]
      self.write(res)





class CompanyAddHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    self.render("company\\add.html")




class CompanyEditHandler(BaseHandler):

  @tornado.web.authenticated
  def get(self):

    self.render("company\\edit.html")







class CompanySearchHandler(BaseHandler):

  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    keyword = self.get_argument("keyword")

    where = r"`chinese_name` LIKE %'%s'%" % (keyword)

    companies = Company().get_company_info(where, '*')

    self.render("company\\index.html", companies=companies)






class CompanyDeleteHandler(BaseHandler):

  @tornado.web.authenticated
  def post(self):

    res = {"success": False, "msg": ""}
    company_id = self.get_argument("company_id")

    if not company_id:
      res["msg"] = "企业编号不能为空"
      self.finish(res)
      return

    result = Company().delete_company(company_id)

    if not result:

      res["msg"] = "删除失败"
      self.finish(res)

    else:

      res["success"] = True
      res["msg"] = "删除成功"
      self.write(res)
