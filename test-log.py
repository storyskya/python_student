#!/bin/python
import logging

# logging.basicConfig(level = logging.DEBUG)
logging.basicConfig(format = '%(name)s:%(lineno)s:%(asctime)s:%(levelname)s:%(message)s',level = logging.DEBUG)

print("*" * 50,'level = debug')
logging.debug('这是debug，start 日志')
logging.info('这是info，start 日志')
logging.critical('这是critical，start 日志')
logging.warning('这是warning，start 日志')
