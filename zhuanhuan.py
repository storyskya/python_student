#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename create-dict.py
# author MaxD

import string
import re
import os

def wendu():
    temp = input('please input 温度(例如 1c 或者 1f):')
    if temp.endswith('c'):
        temp = float(temp.strip(string.ascii_letters))
        tf = (9/5) * temp + 32
        print(f'tf = (9/5)*{temp}+32 = {tf}F')
    elif temp.endswith('f'):
        temp = float(temp.strip(string.ascii_letters))
        tf = (5/9) * temp - 32
        print(f'tf = (5/9)*{temp}-32 = {tf}T')
    else:
        print('bye')
    return()

def huobi():
    temp = input('please input 货币(例如 1rmb 或者 1usd):')
    if temp.endswith('rmb'):
        temp = float(temp.strip(string.ascii_letters))
        usd = temp / 6.78
        print(f'{temp}rmb = {temp}/6.78 = {usd}usd')
    elif temp.endswith('usd'):
        temp = float(temp.strip(string.ascii_letters))
        rmb=  temp * 6.78
        print(f'{temp}usd = {temp} * 6.78 = {rmb}rmb')
    else:
        print('bye')

def changdu():
    temp = input('please input 长度(例如 1M 或者 1ft):')
    if temp.endswith('M'):
        temp = float(temp.strip(string.ascii_letters))
        m = temp * 3.28
        print(f'{temp}M = {temp} * 3.28 = {m}ft')
    elif temp.endswith('ft'):
        temp = float(temp.strip(string.ascii_letters))
        ft=  temp / 3.28
        print(f'{temp}ft = {temp} / 3.28 = {ft}M')
    else:
        print('bye')

while True:
    print('Wellcome'.center(30,'*'))
    menu = {
        't':'温度',
        'l':'长度',
        'c':'货币',
        'q':'退出'
    }

    for k,v in menu.items():
        print(k,v)
    choose = input('please select type:')

    if choose == 't':
        wendu()

    if choose == 'c':
        huobi()

    if choose == 'l':
        changdu()

    if choose == 'q':
        print('Bye')
        exit(0)
    if choose not in ['t','c','l','q']:
        print('Are you kidding me???')
        print()



