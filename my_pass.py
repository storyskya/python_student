#!/usr/bin/env python
# -*-coding:utf-8 -*-
# filename my_pass.py
# author MaxD

import base64
import string
import getpass
import os
import sys

print('''一个生成密码的小程序,作者 MaxD
输入一个常用密码再输入一组字符串，可生成一串加密后的密码。
（注：并非随机密码。如两次输入一样则生成的密码也一样，可以方便忘记时找回）
        ''')


def input_str():
    TF = True

    while TF:
        one_str = getpass.getpass('请输入原始密码(最少8个字符): ')
        two_str = input('请输入随机密码(最少5个字符): ')
        base_str = one_str + two_str
        if len(base_str) <= 13:
            print('字符串过短请重新输入')
        else:
            TF = False
    return(base_str)


def create_pass():
    base_str = input_str()
    count = 0
    F_pass = ""

    base_pass = (base64.b64encode(base_str.encode('utf-8'))).decode('utf-8')

    for _ in range(0,len(base_pass)):
        count += 2
        try:
            F_pass = F_pass + base_pass[count]
            if len(F_pass) == 7:
                F_pass = F_pass + str(int(len(base_str)/2))
            if len(F_pass) == 5:
                F_pass = F_pass + string.punctuation[len(base_str)]
        except IndexError as error1:
            pass

    print()
    print()
    print(F_pass[3:])
    print()

sys.tracebacklimit = 0
create_pass()

os.system('cmd.exe')