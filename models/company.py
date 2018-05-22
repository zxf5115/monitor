#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# 程序：base.py
# 作者：zhangxiaofei
# 日期：2018-05-09
# 功能：model基础类
# -------------------------------------------------------------------------

from models.base import Base
from libs.tools.tools import *

class Company(Base):

  table_name = 'company'

  def __init__(self):

    # 获取连接对象
    super(Company, self).__init__()





  # -----------------------------------------------------------------------
  # 创建用户

  def create_company(self, **args):

    try:

      res = {"success": False, "msg": "", 'company': None}

      where = "chinese_name = '%s'" % (args["chinese_name"])

      company = self.select('id', where)

      if company:
        res["msg"] = "公司已存在"
        return res

      field = "chinese_name, english_name, industry, website, description, create_time, update_time"
      values = "'%s', '%s', '%s', '%s', '%s', '%s', '%s'" % (args["chinese_name"], args["english_name"], args["industry"], args["website"], args["description"], timestamp(), timestamp())

      result = self.insert(field, values)

      res["success"] = True
      res["company"] = result
      return res

    except Exception as e:

      print(str(e))
      # session.rollback()
      res["msg"] = "创建出错"
      return res




  def get_company_info(self, cid = 0, field = 'id'):

    try:

      res = {"success": False, "msg": ""}

      # if not id:

      #   res["msg"] = "UID不能为空"
      #   return res

      where = '1'

      if cid:

        where = "id = '%s'" % (cid)

      result = self.select(field, where)

      return result

    except Exception as e:

      print(e)



  def delete_company(self, cid):

    try:

      if cid:

        where = "id = '%s'" % (cid)

        result = self.delete(where)

        return True

    except Exception as e:

      # print(e)
      return False

