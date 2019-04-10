#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename new_beiwanglu.py
# author MaxD

import string
import random
from color_me import ColorMe

zong_list = []


def Add_list():

    str = input('请输入一段文字,包含人物,时间,事件.每个元素间通过","分割：')

    str_list = str.split(',')
    Man = str_list[0]
    Time = str_list[1]
    Thing = str_list[2]
    
    Thing_dict = {
    '人物':Man,
    '时间':Time,
    '待办事项':Thing
    }

    zong_list.append(Thing_dict)
    return()

def Find_list():
    if zong_list is not None:       
        Find_con = input('请输入查询内容（例如 1.30或10:28或开会 ）: ')
        for list_num in range(len(zong_list)):
            # for Find_con in zong_list[list_num]:
            if Find_con in zong_list[list_num].values():
                # print (zong_list[list_num].items())
                for k,v in zong_list[list_num].items():
                    print (f'{ColorMe(k).blue()}:{ColorMe(v).red()}')
                print()
    else:
        print('请增加备忘录内容')

def Del_list():
    if len(zong_list) != 0:

        Del_con = input('可根据条目内容删除某个事件（例如 输入10:30则将删除该时间点的一条记录）：')
        for list_num in range(len(zong_list)):
            if Del_con in zong_list[list_num].values():
                print(zong_list[list_num])
                Del_yn = input('是否删除这条备忘录？(y/n)')
                if Del_yn == 'y':
                   del zong_list[list_num]
                   break
                elif Del_yn == 'n':
                    continue
    elif len(zong_list) == 0:
        f = ColorMe('目前备忘录已被清空').red()
        print (f'\n {f} \n')

def Look_list():
    if len(zong_list) != 0:
        for i in range(len(zong_list)):
            for k,v in zong_list[i].items():
                print (f'{ColorMe(k).blue()}:{ColorMe(v).red()}')
            print ('_'*30)
    elif len(zong_list) == 0:
        f = ColorMe('目前备忘录没内容').blue()
        print(f'\n {f} \n')

while True:
    choose = input('''
    请选择如下几种操作:
    \n
    A 增加备忘录内容
    F 查找备忘录内容
    D 删除备忘录内容
    L 列出所有内容
    Q 退出
    \n
    ''')

    if choose == 'A':
        Add_list()

    if choose == 'F':
        Find_list()

    if choose == 'D':
        Del_list()

    if choose == 'L':
        Look_list()

    if choose == 'Q':
        print('Bye')
        exit(0)
    if choose not in ['A','F','D','Q','L']:
        print('Are you kidding me???')
        print()