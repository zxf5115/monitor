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

class Users(Base):

  table_name = 'users'

  def __init__(self):

    # 获取连接对象
    super(Users, self).__init__()



  # -----------------------------------------------------------------------
  # 创建用户

  def create_user(self, **args):

    try:

      res = {"success": False, "msg": ""}

      where = "email = '%s'" % (args["email"])

      user = self.select('id', where)

      if user:
        res["msg"] = "已存在"
        return res

      password, encrypt = encryption(args["password"])



      field = "username, password, email, encrypt, is_admin, last_login_time, create_time, update_time"
      values = "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'" % (args["username"], password, args["email"], encrypt, 1, timestamp(), timestamp(), timestamp())

      self.insert(field, values)

      res["success"] = True
      return res

    except Exception as e:

      print(str(e))
      # session.rollback()
      res["msg"] = "创建出错"
      return res
