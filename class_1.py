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
# auto.run('1')
auto.brand = 'auto2018'
# print(auto.brand)
# # print(auto.info)

# # Car.speed = 33
# # print(Car.speed)
# auto.brand
# tesla = Car('Tesla',100000,4,'electric')
# tesla.run('1')
# tesla.price = 999
# print(tesla.price)
# tesla.name = '123'
# print(auto.name)
# print(Car.name)
# print(tesla.name)
# class Computer:
#     def play(self,game = 'qqGame'):
#         print('play',game)

# pcl = Computer()
# pcl.play('123')
# # pcl.play(game = 'abc')
# Computer.play(Computer,game = 'abc')
class Computer:
    '''DianNao'''
    __slots__ = ('_name','mem','cpu')
    def __init__(self,name,mem,cpu):
        self._name = name
        self.mem = mem
        self.cpu = cpu
    
    def play(self,game='qq Game'):
        print('play',game)

    def __str__(self):
        return f'{self._name}:{self.mem}-{self.cpu}'

    def __eq__(self,other):
        return self.cpu == other.cpu

    @classmethod
    def new_pc(ufo1,info):
        xman,ufo,xxx = info.split('-')
        return ufo1(xman,ufo,xxx)

    @staticmethod
    def calc(a,b,oper):
        if oper == '-':
            return a+b

pc1 = Computer('0','16G',8)

pc3 = Computer('8','16G',8)

pc666 = Computer.new_pc('pc666-16g-4')
# print(pc666)

# print(pc1 == pc3)
u=Computer.calc(3,5,'+')
# print(u)


class PP(int):
    def __new__(cls,value):
        return super(PP,cls).__new__(cls,abs(value))

i = PP(-3)
# print(i)

class Person(object):
    def __init__(self,name):
        self.name = name
        print("--init ....")

    def __new__(cls, *args, **kwargs):
        """
        cls  : 代表Person这个类本身
        :param args:
        :param kwargs:
        :return:
        """
        print("--in new: ",cls,*args,**kwargs)

        return object.__new__(cls)  # 调用父类的__new__方法，必须这么干 ，要不然__init__方法就不会执行了


p = Person("Alex")
# print(p.name)
# print(Person)

class d8gmeta(type):
    def __new__(cls,name,base,my_dict):
        print(f'{name} use __new__ create')
        d8g_class = super().__new__(cls,name,base,my_dict)
        print(type(d8g_class),'1')
        return d8g_class

class d8g(metaclass=d8gmeta):
    pass

d8g()
a = d8g()
b = d8g()
print(type(d8g))
print(type(a))
