#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：logger.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：弃用，因为无法显示错误文件地址
# -------------------------------------------------------------------------

import time
import hashlib
import datetime

def encryption(text):

  timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%a%B%f%Z')

  salt = "%s%s" % (text, timestamp)

  code = hashlib.md5(salt.encode(encoding='utf-8')).hexdigest()

  return code, timestamp


def timestamp():

  timestamp = time.time()

  timestamp = int(timestamp)

  return timestamp
