#!/usr/bin/env python
# -*-coding:utf-8 -*-
# filename Get-shutdown.py
# author MaxD

import sys
import subprocess





def a_time():
    set_time = input('请输入关机的时间 例如(08:00): ')
    set_name = 'shut'+set_time.replace(':','')
    out_put = {'shell' : True,'stdout' : open('tmp.log','w'),'stderr' : subprocess.STDOUT}

    print()
#     if int(set_time[0:2]).isdigit() and int(set_time[-2:]).isdigit():
    try:
        if int(set_time[0:2]) > 24 or int(set_time[-2:]) >60:
                print('请按照正确格式输入时间,如：08:00')
        else:
                try:
                        if subprocess.call(['schtasks.exe','/query','/tn',set_name],**out_put) == 0:
                                subprocess.run(['schtasks.exe', '/delete', '/tn', set_name, '-f'],**out_put)
                                subprocess.run(['schtasks.exe', '/create', '/tn', set_name, '/TR', 'shutdown -s', '/sc', 'once', '/st',set_time],**out_put)
                                subprocess.run(['del','tmp.log'],**out_put)
                                print('设置成功')
                        else:
                                subprocess.run(['schtasks.exe', '/create', '/tn', set_name, '/TR', 'shutdown -s', '/sc', 'once', '/st',set_time],**out_put)
                                subprocess.run(['del','tmp.log'],**out_put)
                                print('设置成功')
                except:
                        print('请按照正确格式输入时间,如：08:00')
    except:
            print('请输入数字')

def l_time():
    set_time = input("请输入时间,系统将在对应分钟后关闭 (例如:60): ")
    try:
        true_time = int(set_time) * 60
    except:
        print('你输入了什么？')

    try:
        if int(set_time) < 0:
            print("请输入正确的数字")
        else:
            subprocess.run(['shutdown', '-s', '-t',str(true_time)])
            print('设置成功')

    except:
        print('请输入数字')

sys.tracebacklimit = 0
while True:
    print()
    print('Wellcome'.center(30,'*'))

    print('''定时关机的小程序,作者 MaxD
        使用方法
   1、指定时间关机;
   2、指定多久后关机;
   q、退出;
                ''')

    choose = input('please select type:')

    if choose == '1':
        a_time()


    if choose == '2':
        l_time()
        
    if choose == 'q':
        print('Bye')
        exit(0)
    if choose not in ['1','2','q']:
        print('Are you kidding me???')
        print()
