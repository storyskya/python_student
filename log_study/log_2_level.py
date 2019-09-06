#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# log_2_level.py
# log的等级
# author: De8uG


import logging

logging.basicConfig(level=logging.DEBUG)


# 共五个级别
# debug(), info(), warning(), error() and critical()
logging.debug('这是一条debug, 开始使用日志啦')
logging.info('这是一条info, 开始使用日志啦')
logging.warning('这是一条warning, 开始使用日志啦')
logging.error('这是一条error, 开始使用日志啦')
logging.critical('这是一条critical告, 开始使用日志啦')

# 默认当前是warning级别，从上到下依次增强。
# 只显示当前和比当前强烈的级别
"""
DEBUG: 详细信息，通常仅在诊断问题时感兴趣。
INFO: 确认事情按预期工作。
WARNING: 表示意外发生，或表示在不久的将来出现一些问题（例如“磁盘空间低”）。该软件仍然按预期工作。
ERROR: 由于更严重的问题，软件无法执行某些功能。
CRITICAL: 一个严重的错误，指示程序本身可能无法继续运行。
"""

# 调整级别
# logging.basicConfig(level=logging.DEBUG)
print('*' * 50, 'level=debug')
logging.debug('这是一条debug, 开始使用日志啦')
logging.info('这是一条info, 开始使用日志啦')
logging.warning('这是一条warning, 开始使用日志啦')
logging.error('这是一条error, 开始使用日志啦')
logging.critical('这是一条critical告, 开始使用日志啦')
