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
for one in one_list:
    print(one,end = " ")
print()
two_list=[]
for _ in range(int(user_num)):
    p1 = random.randint(1,10)
    two_list.append(p1)
for two in two_list:
    print(two,end = " ")
print()

sum_list=[]
for sum in range(0,len(one_list)):
    sum_1 = one_list[sum] + two_list[sum]
    sum_list.append(sum_1)
for sum3 in sum_list:
    print(sum3,end = " ")
print()

user_dict = {}
for yuansu in range(0,len(sum_list)):
    user_dict[name_list[yuansu]] = sum_list[yuansu]

# for a in range(0,len(sum_list)):
#     user_con = input(f'{name_list[a]} 是否继续？(y/n)')
#     if user1_con == 'n':
#         new_point = del 
