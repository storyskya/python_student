#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# log_3_set_out.py
# log的各种输出控制
# author: De8uG
# https://docs.python.org/3/library/logging.html#formatter-objects

import logging


# basicConfig每个文件配置一次，且放最前面

# 2.修改显示格式
# logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.DEBUG)

# 3.添加时间
# logging.basicConfig(format='%(asctime)s %(message)s')

# 4.复杂格式
logging.basicConfig(level=logging.DEBUG, format='%(lineno)d - %(filename)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')

# --------------------------------------------------
# 1.根据变量显示内容
de8ug = 'de8ug'
logging.warning('%s python', de8ug)

print('修改显示格式:')

# 2.修改显示格式
logging.debug('这一行跟着格式走')
logging.info('这行也是')

# 3.添加时间
print('添加时间:')
logging.warning('这条日志设置了时间')

# 4.复杂格式
logging.debug('这一行好像复杂多了')