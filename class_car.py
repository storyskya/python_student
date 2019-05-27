#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename class_car.py
# author MaxD

class Car:
    def info(self):
        print('Car 父亲')

class Audi(Car):
    def info(self):
        print('Audi 汽车')

class Tesla(Car):
    def info(self):
        print('Tesla 汽车')

class Factory:
    def create(self):
        print('创建汽车，工厂基类')

class AudiFactory(Factory):
    def create(self):
        print('创建Audi汽车')
        return Audi()

class TeslaFactory(Factory):
    def create(self):
        print('创建Tesla汽车')
        return Tesla()

audi = AudiFactory()
audi.create().info()