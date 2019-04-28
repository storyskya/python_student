import random
import string
from color_me import ColorMe
stuInfo = {'westos'+ str(i):random.randint(60,100) for i in range(20)}
# print({name:score for name,score in stuInfo.items() if score > 90})

Thing_dict = {
    '日期':'',
    '时间':'',
    '地点':'',
    '待办事项':''
}
# con = input('shuru : ')
# Thing_list = [{'日期': '1.3', '时间': '3.1', '地点': 'hahah', '待办事项': '111'}, {'日期': 'hahah', '时间': '111', '地点': 'uuu', '待办事项': 'vvv'},{'日期': 'hahah', '时间': '111', '地点': 'uuu', '待办事项': 'vvv'}]
# for i in range(len(Thing_list)):
#     print ('123')
#     pass
# print(Thing_list)

# for u in range(9,0):
#     print(u)

# s = 'ab,cdefg,hiajkuiop,bcol,ua'
# u = s.find(',')+1
# print(u)
# print (s[u:s.find(',',u)])

str = 'ab,cdefg,hiajkuiop,bcol,ua'
# Man = str[:str.find(',')]
# num = str[str.find(',')]
# print(Man)
# time = str[str.find(Man)]
# print(time)
# zong_list=[]
# str = input('请输入一段文字,包含人物,时间,事件.每个元素间通过","分割：')
# str_list = str.split(',')
# Man = str_list[0]
# Time = str_list[1]
# Thing = str_list[2]

# Thing_dict = {
# '人物':Man,
# '时间':Time,
# '待办事项':Thing
# }
# zong_list.append(Thing_dict)
# print(zong_list)

# def car(**ks):
#     for k,v in ks.items():
#         print(f'{k}::{v}')
# car(doom='blue',pp=20,user='ufo')
# def car(*aa):
#     print(aa)
#     for k in aa:
#         print(k)

# def car(*k,**a):
#     print('a',a)
#     print('k',k)
#     for i in k:
#         print(i)
#     for u,v in a.items():
#         print(f'{u}::{v}')

# kwargs = {'color':'red','price':'ufo'}
# def car(color='',price=''):
#     print(color,price)
# car(**kwargs)
# def all_up(s):
#     return s.strip().upper()
# print(all_up('ufoUFO'))
# my_list = [1,3,5,3,4,67,8,4,6,8]
# def odd(*L):
#     new_list = []
#     for k in L:
#         if k %2 ==1:
#             new_list.append(k)
#     return (new_list)
# def add(x:int,y:'hahah') -> 'ufo':
#     """Add ufo into here"""
#     return x + y
# print(add.__doc__)
# print(add.__annotations__)
# x = 123
# def test():
#     y = 1
#     x = y + 1
#     print(x)
# test()
# print(x)
# list1 = []
# def addlist():
#     list2 = list1
#     list2 += '99'
#     print(list2)
# addlist()
# def calc(x,y):
#     def add(x,y):
#         print('x+y:',x + y)
#     def sub(x,y):
#         print('x-y:',x - y)
#     def mul(x,y):
#         print('x*y:',x * y)
#     add(x,y)
#     sub(x,y)
#     return mul

# bbb = calc(8,9)
# print (bbb(11,22))
# def hello():
#     s = 'ufo'
#     def say():
#         print(s)
#     return say
# print(hello())
name = ''
str_from = string.ascii_letters
# for _ in range(8):
#     x = ''.join([random.choice(str_from)])
#     print (x)
#     name = name+x
# print (name)
# str_from = string.ascii_letters
# # print(''.join([random.choice(str_from) for _ in range(5)]))
# print(''.join([random.choice(str_from)
# class Car():
#     pass

# class MyCar():
#     pass
# c = MyCar()
# print(Car)
# print(type(Car))
# print(type(c))
# print(c)
# print(isinstance(c,MyCar))
class Bird:
    def __init__(self,name):
        self.name = name
    
    def sing():
        print(f'{self.name}zai gechang')

b5 = Bird('bailing ')
Bird.sing('bailing')