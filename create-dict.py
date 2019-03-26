#!/usr/bin/env python
# -*-coding:utf-8 -*-
# filename create-dict.py
# author MaxD
import os
import string
import re
import random

one_dict = {}
def get_name():
    name = ""
    num_zishu = random.randint(3,5)
    str_from = string.ascii_letters
    for _ in range(num_zishu):
        x = ''.join([random.choice(str_from)])
        name = name+x
    return name

def get_key():
    key = ""
    num_zishu = random.randint(0,1)
    str_from = string.digits
    for _ in range(2):
        x = ''.join([random.choice(str_from)])
        key = key+x
    return key
    
cishu = input('输入生成词典内容个数：')
for _ in range(int(cishu)):
    # key1 = input('姓名：')
    # value1 = input('年龄：')
    key1 = get_name()
    value1 = get_key()
    # print('分割线'.center(30,'#'))
    one_dict['姓名:'+key1] = '年龄:'+value1
print(one_dict)