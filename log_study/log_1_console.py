#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# log_1_console.py
# 对比print和log
# author: De8uG


import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def count_sheep():
    print('第8哥睡不着，躺在床上数绵羊🐑')  # 1
    print('生成随机数, 表示到时候睡着了')
    num = random.randint(1, 100)
    print(num)
    for i in range(1, 100):
        print(i, '只🐑')
        if i == num:
            print('数到第%s只🐑，睡着了(～﹃～)~zZ' %i)  # 2
            if num < 10:
                print('今天睡的很早')
            elif 10 <= num < 50:
                print('今天有点心事，睡不着，好困...')
            else:
                print('Ohh my god, 这是要失眠的节奏啊！/(ㄒoㄒ)/~~')
            break


def count_sheep_log():
    logging.disable(logging.CRITICAL)
    print('第8哥睡不着，躺在床上数绵羊🐑')
    logger.info('生成随机数, 表示到时候睡着了')
    num = random.randint(1, 100)
    logger.debug(num)
    for i in range(1, 100):
        logger.info(f'{i} 只🐑')
        if i == num:
            print('数到第%s只🐑，睡着了(～﹃～)~zZ' %i)
            if num < 10:
                logger.debug('今天睡的很早')
            elif 10 <= num < 50:
                logger.warning('今天有点心事，睡不着，好困...')
            else:
                logger.error('Ohh my god, 这是要失眠的节奏啊！/(ㄒoㄒ)/~~')
            break


def main():
    # count_sheep()
    count_sheep_log()

if __name__ == '__main__':
    main()
