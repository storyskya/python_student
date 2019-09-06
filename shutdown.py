#!/bin/python
import os
from os import system
import time
import subprocess
# 关机
# os.system("shutdown -s -t  600 ")

# 重启
# system("shutdown -r -t 100")

# set_time = input('请输入关机的时间 例如(08:00): ')
# # os.system("schtasks.exe /create /tn test /TR \"shutdown -s\" /sc once /st %s" %set_time)
# from subprocess import run
# run("ping 127.0.0.1",shell=True)
# os.popen("md 1ab")

# if subprocess.Popen(['schtasks.exe'],'/query' '/tn shut1900') == 0:
    # print('ok')
# subprocess.call(['schtasks.exe','/query','/tn','shut1900'])
subprocess.run(['shutdown.exe','-s','-t','900'])
# while True:
#     t = time.localtime()
#     fmt = "%H:%M:%S"
#     now = time.strftime(fmt,t)
#     # print(now + '\r', end = '')
#     # sys.stdout.write(now + '\r')
#     # sys.stdout.flush()
#     # time.sleep(1)
#     if now[:5] == set_time.rjust(5,'0'):
#         print(f"at {now} shutdown -s")
#         os.system("schtasks.exe /create /tn shut /TR \"shutdown -s\" /sc once /st %s" %now)
#         break