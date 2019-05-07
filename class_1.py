#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename class_1.py
# author MaxD
class Car:
    name = 'xxx'
    def __init__(self,brand,price,wheels,power):
        self._brand = brand
        self.price = price
        self.wheels = wheels
        self.power = power
        self.__speed = 0


    def run(self,action):
        print(f'{self._brand} is running')
        if action == '1':
            self.__speed += 1 * 10
            print('当前速度: {} km/h'.format(self.__speed))

    
    @property
    def brand(self):
        return self._brand

    def speed(self):
        return self.__speed

    @brand.setter
    def brand(self,brand):
        if not isinstance(brand,str):
            raise TypeError('品牌应该是字符串')
        self._brand = brand

    @property
    def info(self):
        return f'{self.brand}:{self.price}'

# c = Car('on',3,4,5).run('1')
# c
auto = Car('auto',30000,4,123)
auto.run('1')
print(auto.info)

Car.speed = 33
print(Car.speed)