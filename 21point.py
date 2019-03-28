#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename 21point.py
# author MaxD
import string
import random
readme = '欢迎来到21点游戏'
print(readme.center(30,'#'))
user_num = input('请输入玩家人数：')
name_list = []
for i in range(1,int(user_num)+1):
    user_name = input(f'输入玩家{i}名字: ')
    name_list.append(user_name)
print(" ".join(name_list))

one_list=[]
for _ in range(int(user_num)):
    p1 = random.randint(1,10)
    one_list.append(p1)
for x in one_list:
    print(x,end = " ")

