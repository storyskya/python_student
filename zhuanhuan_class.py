#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename zhuanhuan_class.py
# author MaxD

import string
import sys

sys.tracebacklimit = 0


class wendu_class:
    '''温度转换类'''
    def Hua_She(temp):
        tf = (5/9) * temp - 32
        print()
        print(f'{temp}f = {tf}c')

    def She_Hua(temp):
        tf = (9/5) * temp + 32
        print()
        print(f'{temp}c = {tf}f')

class huobi_class:
    '''货币转换类'''
    def rmb_usd(temp):
        usd = temp / 6.78
        print("\n")
        print(f'{temp}rmb = {temp}/6.78 = {usd}usd')
    
    def usd_rmb(temp):
        rmb=  temp * 6.78
        print("\n")
        print(f'{temp}usd = {temp} * 6.78 = {rmb}rmb')

class changdu_class:
    '''长度转换类'''
    def M_ft(temp):
        m = temp * 3.28
        print()
        print(f'{temp}M = {temp} * 3.28 = {m}ft')

    def ft_M(temp):
            ft=  temp / 3.28
            print()
            print(f'{temp}ft = {temp} / 3.28 = {ft}M')



class Transfer:
    '''输入输出管理类'''
    def wendu(self):
        temp = input('please input 温度(例如 1c 或者 1f):')
        try:
            if temp.endswith('c') or (temp[-1].lower() == 'c'):
                temp = float(temp.strip(string.ascii_letters))
                return(wendu_class.She_Hua(temp))
            
            elif temp.endswith('f') or (temp[-1].lower() == 'f'):
                temp = float(temp.strip(string.ascii_letters))
                return(wendu_class.Hua_She(temp))
                
            else:
                print()
                print()
                print("Please Input c/f")

        except Exception as e:
            print("\n")
            print('Input Error')
            return

    def huobi(self):
        temp = input('please input 货币(例如 1rmb 或者 1usd):')
        try:
            if temp.endswith('rmb') or (temp[-3:].lower() == 'rmb'):
                temp = float(temp.strip(string.ascii_letters))
                return(huobi_class.rmb_usd(temp))
            
            elif temp.endswith('usd') or (temp[-3:].lower() == 'usd'):
                temp = float(temp.strip(string.ascii_letters))
                return(huobi_class.usd_rmb(temp))
                
            else:
                print("Please Input rmb/usd")

        except Exception as e:
            print("\n")
            print('Input Error')
            return

    def changdu(self):
        temp = input('please input 长度(例如 1M 或者 1ft):')
        try:
            if temp.endswith('M') or (temp[-1].lower() == 'm'):
                temp = float(temp.strip(string.ascii_letters))
                return(changdu_class.M_ft(temp))
            
            elif temp.endswith('ft') or (temp[-2:].lower() == 'ft'):
                temp = float(temp.strip(string.ascii_letters))
                return(changdu_class.ft_M(temp))
                
            else:
                print()
                print("Please Input M/ft")

        except Exception as e:
            print("\n")
            print('Input Error')
            return

def main():
    main_api = Transfer()
    while True:
        print("\n")
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
            choose_api = main_api.wendu()
            choose_api

        if choose == 'c':
            choose_api = main_api.huobi()
            choose_api

        if choose == 'l':
            choose_api = main_api.changdu()
            choose_api

        if choose == 'q':
            print('Bye')
            exit(0)
        if choose not in ['t','c','l','q']:
            print()
            print('Are you kidding me???')



if __name__ == '__main__':
    main()