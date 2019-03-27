# -*- coding=utf-8 -*-
import string
import re
import os
print('Wellcome'.center(30,'*'))
menu = {
    't':'温度',
    'l':'长度',
    'c':'货币'
}
for k,v in menu.items():
    print(k,v)
choose = input('please select type:')
if choose == 't':
    temp = input('please input wendu(例如 1c 或者 1f):')
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
else:
    print('Are you kidding me???')
# if choose == 'l':
#     temp = input('please select type:')
#     temp = float(temp.strip(string.ascii_letters))
#     tf = 