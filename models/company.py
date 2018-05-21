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






# def create_company(**kwargs):
#     try:
#         res = {"success": False, "msg": "", 'company': None}
#         company = session.query(Company).filter_by(name_cn=kwargs["name_cn"]).first()
#         if company:
#             res["msg"] = "公司已存在"
#             return res
#         session.add(Company(name_cn=kwargs["name_cn"], name_en=kwargs["name_en"], industry=kwargs["industry"]))
#         # session.commit()
#         session.flush()
#         company = session.query(Company).filter_by(name_cn=kwargs["name_cn"]).first()
#         res["success"] = True
#         res["company"] = company
#         return res
#     except Exception as e:
#         # print(str(e))
#         # session.rollback()
#         res["msg"] = "创建出错"
#         return res



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

      field = "chinese_name, english_name, industry, website, is_admin, last_login_time, create_time, update_time"
      values = "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'" % (args["username"], password, args["email"], encrypt, 1, timestamp(), timestamp(), timestamp())

      self.insert(field, values)

      res["success"] = True
      return res

    except Exception as e:

      print(str(e))
      # session.rollback()
      res["msg"] = "创建出错"
      return res




  def get_user_info(self, uid = 0, field = 'id'):

    try:

      res = {"success": False, "msg": ""}

      # if not uid:

      #   res["msg"] = "UID不能为空"
      #   return res

      where = '1'

      if uid:

        where = "id = '%s'" % (uid)

      user = self.select(field, where)

      return user

    except Exception as e:

      print(e)






  def authenticate(self, email=None, password=None):

    res = {"success": False, "msg": "", "user_id": None}

    where = "email = '%s'" % (email)

    user = self.find('id, encrypt, email, password', where)

    if not user:

      res["msg"] = "用户名不存在"
      return res

    password = decryption(password, user['encrypt'])

    if user['password'] != password:
      res["msg"] = "用户名与密码不符"
      return res

    res["success"] = True
    res["user_id"] = user['id']
    res["msg"] = "认证成功"
    return res
# c9e81949a181e2e1b903530afcbfe563
