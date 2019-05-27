#!/usr/bin/env python
# -*-coding:utf-8 -*-
# filename my_pass.py
# author MaxD

import base64
import string
import getpass
import time
import pyperclip

print('''一个生成密码的小程序,作者 MaxD
输入一个默认密码再输入一组字符串，可生成一串加密后的密码并可以直接粘贴使用。
（注：并非随机密码。如两次输入一样则生成的密码也一样，可以方便忘记时找回）
        ''')

default_str = getpass.getpass('Default_str: ')
input_str = input('Domain name: ')
add_str = default_str+input_str
base_str = (base64.b64encode(add_str.encode('utf-8'))).decode('utf-8')

count = 0
F_pass = ""

for _ in range(0,len(base_str)):
    count += 2
    try:
        F_pass = F_pass + base_str[count]
    except IndexError as error1:
        pass
    if len(F_pass) == 7:
        F_pass = F_pass + str(len(input_str))
    if len(F_pass) == 5:
        F_pass = F_pass + string.punctuation[len(add_str)]

pyperclip.copy(F_pass[3:])
print()
print()
print(F_pass[3:])

print()
time.sleep(10)