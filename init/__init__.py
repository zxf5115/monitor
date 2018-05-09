#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys

# 获得文件当前路径os.path.abspath 获得文件的父目录os.path.dirname
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(BASE_DIR)

from config.config import DB
