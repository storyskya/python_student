#!/bin/python

import sys
import time
import subprocess

set_time = input('设置起床时间(如：8:00)')

print(f'闹钟被设置为:{set_time}')

print('现在时间是:')

while True:
    t = time.localtime()
    fmt = "%H:%M:%S"
    now = time.strftime(fmt,t)
    print(now + '\r', end = '')
    # sys.stdout.write(now + '\r')
    # sys.stdout.flush()
    time.sleep(1)
    if now[:8] == set_time.rjust(8,'0'):
        print('时间到！')
        # subprocess.Popen(['start','VOICES.mp3'],shell = True)
        continue