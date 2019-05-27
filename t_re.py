#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename create-dict.py
# author MaxD

import re
import string


RE_PHONE = re.compile(r'\d{3}-\d{8}|\d{4}-\d{7}')

RE_CHINESE = re.compile(r'^[\u4e00-\u9fa5]{1,8}$')

RE_PWD = re.compile(r'^[a-zA-Z]\w{7,17}$')

def find_phone(text: str):
    return RE_PHONE.findall(text)


def verify_CH(text):
    if RE_CHINESE.match(text):
        return True
    else:
        return False

def verify_user(re_obj,text):
    if re_obj.match(text):
        return True
    else:
        return False    


def main():
    # text = '0467-9867788 , 13811729959'
    name = '哈哈哈'
    # print(find_phone(text))
    print(verify_user(RE_CHINESE,name))

    password = 'NAO9gaZcp'
    print(verify_user(RE_PWD,password))

if __name__ == '__main__':
    main()
