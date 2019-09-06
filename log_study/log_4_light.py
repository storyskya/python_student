#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# log_4_light.py
# log的工程应用, 交通信号灯案例
# author: De8uG


import random
import log_4_func

log = log_4_func.de8ug_log()
# log.info('test')
# log2 = log_4_func.de8ug_log(logger_name='a', log_file='a.log')
# log2.info('test222')


light = ['红灯', '黄灯', '绿灯']
road = {
    '长安街': random.choice(light),
    '二环': random.choice(light),
    '五环': random.choice(light)
}


def driving(name, car):
    print(f'{name}开着【{car}】逛北京')
    for k, v in road.items():
        v = random.choice(light)  # 临时调整
        log.info(f'开着开着，到了{k}， 遇到了：{v}')
        if v == '红灯':
            log.error('快刹车啊')
        elif v == '绿灯':
            log.info('继续开吧，老司机')
        else:
            log.warning('开不开都行，看运气吧')


def main():
    for i in range(5):
        print(f'----》开始第{i+1}次逛马路')
        driving('de8ug', '长江八号')
    print('我到家了'.center(50, '='))

if __name__ == '__main__':
    main()