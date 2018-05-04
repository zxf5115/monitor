#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：mysql.py
# 作者：zhangxiaofei
# 日期：2018-04-28
# 功能：Mysql操作类
# -------------------------------------------------------------------------

import os
import sys


def environment_variable():

  BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
  sys.path.append(BASE_DIR)
