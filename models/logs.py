#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# 程序：logs.py
# 作者：zhangxiaofei
# 日期：2018-06-15
# 功能：日志类
# -------------------------------------------------------------------------

from models.base import Base
from libs.tools.tools import *

class Logs(Base):

  table_name = 'logs'

  def __init__(self):

    # 获取连接对象
    super(Logs, self).__init__()



  # -----------------------------------------------------------------------
  # 创建用户



  def get_log_info(self):

    try:

      res = {"success": False, "msg": ""}

      since = time_difference(1)

      where = 'create_time > ' + str(since)

      logs = self.select('*', where)

      return logs

    except Exception as e:

      print(e)




# def get_logs(mins):
#     since = datetime.datetime.now() - datetime.timedelta(minutes=mins)
#     logs = session.query(CrawlerLOG).filter(CrawlerLOG.create_at > since).order_by(desc(CrawlerLOG.create_at)).all()

#     flag = datetime.datetime.now() - datetime.timedelta(days=1)
#     old_logs = session.query(CrawlerLOG).filter(CrawlerLOG.create_at <= flag).all()
#     for log_item in old_logs:
#         session.delete(log_item)
#     session.flush()
#     return logs
