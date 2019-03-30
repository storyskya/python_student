#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename 21point.py
# author MaxD
import sys
import string
import random
readme = '欢迎来到21点游戏'
print(readme.center(30,'#'))
user_num = input('请输入玩家人数,限制为4人：')
name_list = []
if int(user_num) <= 4:
    for i in range(1,int(user_num)+1):
        user_name = input(f'输入玩家{i}名字: ')
        name_list.append(user_name)
    print(f'玩家列表为：{" ".join(name_list)}')
else:
    print('请输入正确的数值')
    sys.exit()

# 第一轮发牌
one_list=[]
for _ in range(int(user_num)):
    p1 = random.randint(5,10)
    one_list.append(p1)
print('第一轮发牌 ',end = " ")
for one in one_list:
    print(one,end = " ")
print()

# 第二轮发牌
two_list=[]
for _ in range(int(user_num)):
    p1 = random.randint(5,10)
    two_list.append(p1)
print('第二轮发牌 ',end = " ")
for two in two_list:
    print(two,end = " ")
print()

# 前两轮点数和
sum_list=[]
for sum in range(0,len(one_list)):
    sum_1 = one_list[sum] + two_list[sum]
    sum_list.append(sum_1)
print('当前玩家总点数 ',end = " ")
for sum3 in sum_list:
    print(sum3,end = " ")
print()

# 生成一个词典
user_dict = {}
for yuansu in range(0,len(name_list)):
    user_dict[name_list[yuansu]] = sum_list[yuansu]
# print(user_dict)

# 询问玩家是否继续
name1_list = []
user1_dict = user_dict.copy()
end_dict = {}
for a in range(0,len(sum_list)):
    user_con = input(f'{name_list[a]} 是否继续？(y/n)')
    if user_con == 'y':
        name1_list.append(name_list[a])
    elif user_con == 'n':
        end_dict[name_list[a]] = sum_list[a]
        del user1_dict[name_list[a]]
    else:
        print('要玩就好好玩')
        exit(0)
print(f'所剩玩家{name1_list}')
print(30*'-')
print(f'已停手玩家{end_dict}')
print(30*'-')
print(f'当前玩家得分{user_dict}')
print(30*'-')

four_list=[]
for _ in range(0,len(name1_list)):
    p1 = random.randint(5,10)
    four_list.append(p1)
print('第三轮发牌：',end = " ")
for four in four_list:
    print(four,end = " ")
print()

# 第四轮点数和
sum4_list=[]
for sum4 in range(0,len(four_list)):
    sum_3 = sum_list[sum4] + four_list[sum4]
    sum4_list.append(sum_3)
print('当前玩家总点数 ',end = " ")
for sum5 in sum4_list:
    print(sum5,end = " ")
print()

name2_list = []
five_list = []
for e in range(0,len(name1_list)):
    user_con = input(f'{name1_list[e]} 是否继续？(y/n)')
    if user_con == 'y':
        five_list.append(sum4_list[e])
        name2_list.append(name1_list[e])
    elif user_con == 'n':
        end_dict[name1_list[e]] = sum4_list[e]
        del user1_dict[name1_list[e]]
    else:
        print('要玩就好好玩')
        exit(0)

print(f'游戏结束 当前玩家点数为：{end_dict}')

sort_list = []
if int(user_num) == 1:
    if end_dict[user_name] <= 21:
        print(f'{user_name} 获胜')
        exit()
    else:
        print('爆了')
        exit()

if user1_dict == {}:
    for u in name_list:
        if end_dict[u] <= 21:
            sort_list.append(end_dict[u])
    sort_list.sort(reverse=True)
for name,point in end_dict.items():
    if point == sort_list[0]:
        print(f'{name} 获胜  当前点数为 {point}')
            

