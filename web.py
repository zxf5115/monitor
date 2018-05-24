#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# 程序：base.py
# 作者：zhangxiaofei
# 日期：2018-05-09
# 功能：model基础类
# -------------------------------------------------------------------------

import os
import tornado.ioloop
import tornado.web
import tornado.locale
import tornado.escape
from tornado.options import define, options

import uimodules

from libs.conf.conf import Conf
from controllers.main import *
from controllers.index import *
from controllers.login import *
from controllers.logout import *
from controllers.register import *
from controllers.users import *
from controllers.subscription import *
from controllers.company import *




class Run:

  def __init__(self):

    conf = Conf()
    debug, port = conf.get_system_conf_info()


    self.handlers = [
      (r"/", IndexHandler),
      (r"/login", LoginHandler),
      (r"/register", RegisterHandler),
      (r"/logout", LogoutHandler),
      (r"/index", IndexHandler),
      # (r"/admin", IndexHandler),
      # (r"/info", InfoHandler),
      # (r"/info/filter/([0-9]+)/page/([0-9]+)", InfoFilterHandler),
      # (r"/info/company/search", InfoCompanySearchHandler),
      # (r"/oversea/filter/([0-9]+)/page/([0-9]+)", OverseaFilterHandler),
      # (r"/oversea/company/search", OverseaCompanySearchHandler),
      # (r"/info/page/([0-9]+)", InfoPageHandler),
      # (r"/oversea/page/([0-9]+)", OverseaPageHandler),
      # (r"/oversea", OverseaInfoHandler),
      # (r"/keyword", KeywordHandler),
      # (r"/keyword/delete", KeywordDeleteHandler),
      # (r"/report", ReportHandler),
      # (r"/report/add", ReportAddHandler),
      # (r"/report/delete", ReportDeleteHandler),
      # (r"/report/detail/([0-9]+)", ReportDetailHandler),
      (r"/company", CompanyHandler),
      (r"/company/add", CompanyAddHandler),
      (r"/company/edit", CompanyEditHandler),
      (r"/company/search", CompanySearchHandler),
      (r"/company/delete", CompanyDeleteHandler),
      # (r"/profile/([0-9]+)", ProfileHandler),
      # (r"/profile/edit/([0-9]+)", ProfileEditHandler),
      # (r"/contact/add/([0-9]+)", ContactAddHandler),
      # (r"/contact/delete", ContactDeleteHandler),
      # (r"/website/add/([0-9]+)", WebsiteAddHandler),
      # (r"/website", WebsiteHandler),
      (r"/subscription", SubscriptionHandler),
      # (r"/company/delete", CompanyDeleteHandler),
      # (r"/subscription", SubscriptionHandler),
      # (r"/website/delete", WebsiteDeleteHandler),
      (r"/user/index", UserHandler),
      (r"/user/add", UserAddHandler),
      (r"/user/edit", UserEditHandler),
      (r"/user/search", UserSearchHandler),
      (r"/user/delete", UserDeleteHandler),
      # (r"/log", LogHandler),
      # (r"/clean", CleanHandler),
    ]


    self.settings = dict(
      cookie_secret = "61oEuYhFp2XdEQA7mGeJJGaYdkL5gETzKXTP1oQn",
      login_url     = "/login",
      template_path = os.path.join(os.path.dirname(__file__), "views"),
      static_path   = os.path.join(os.path.dirname(__file__), "static"),
      xsrf_cookies  = True,
      ui_modules    = uimodules,
      debug         = debug,
    )


    i18n_path = os.path.join(os.path.dirname(__file__), 'i18n/locales')

    tornado.locale.load_gettext_translations(i18n_path, 'zh_CN')

    tornado.locale.set_default_locale('zh_CN')

    application = tornado.web.Application(self.handlers, **self.settings)

    application.listen(port)

    print("App Start running at: http://127.0.0.1:{port}".format(port=port))

    tornado.ioloop.IOLoop.instance().start()



if __name__ == '__main__':

  Run()
