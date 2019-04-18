#!/usr/bin/env python
# -*-coding:utf-8 -*-
# filename my_pass.py
# author MaxD

import base64
import string

default_str = 'hong1968'
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
        
print()
print()
print(F_pass[3:])
print()