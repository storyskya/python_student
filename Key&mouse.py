#!/usr/bin/env python
# -*-coding:utf-8 -*-
# filename Key&mouse.py
# author MaxD

print('''
                        用于游戏不掉线的工具,作者 MaxD
使用方法: 双击本程序以后5秒钟内切换到游戏窗口，人物会随机向不同方向走动并释放快捷键1-5内的技能。
                     (建议1-6内放置不需要目标就能释放的技能)
        ''')

import sys
import time
import random
import string

from pykeyboard import PyKeyboard

show_time = 6
while True:
    show_time = show_time -1
    print(show_time)
    time.sleep(1)
    if show_time == 0:
        break

sys.tracebacklimit = 0
time.sleep(5)

k = PyKeyboard()

def get_time():
    run_time = random.choice(string.digits)
    return(int(run_time))

def get_direction():
    direction_key = ['w','s','a','d','q','e']
    get_key = random.choice(direction_key)
    return(get_key)

def run_move():
    direction = get_direction()
    k.press_key(direction)
    time.sleep(get_time())
    k.release_key(direction)


def run_action():
    action = str(random.randrange(1,5))
    k.tap_key(k.tab_key)
    k.tap_key(action)
    time.sleep(get_time())
    k.tap_key(action)
    # print(type(action))

while True:
    k.tap_key(k.tab_key)
    run_move()
    time.sleep(get_time())
    run_action()

if __name__ == '__main__':
    main()