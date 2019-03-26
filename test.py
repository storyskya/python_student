#coding: utf-8
import random
import math
point_21 = random.randint(1,21)
sishewuru = math.floor(9.9)
def listAdd(list1,c):
    list1.append(c)
    return list1

list1 = ['a','b','c']

list3 = ([1] * 3)
listAdd(list1,'d')

list2 = [1,2,3,4,5,6,7,8,9,19]

# for i in range(10,0,-1):
#     for x in range(0,i):
#         print (x,end=" ")
#     print ()
# n = 10
# for i in range(n):
#     for x in range(0,n):
#         print (x,end=" ")
#     n-=1    
#     print ()
# cs 代表乘数 bcs代表被乘数
# for cs in range(9,0,-1):
#     for bcs in range(1,cs+1):
#         # print (f"{cs}*{bcs}={str(cs*bcs).ljust(2)}",end=" ")
#         print(bcs,"*",cs," = ",str(bcs*cs),end= "  ")
#     print ()
ch_n = [' ','一','二','三','四','五','六','七','八','九','零']
alb_n = [' ','1','2','3','4','5','6','7','8','9','0']
for i in range(9,0,-1):
    for j in range(1,i+1):
        result = str(i*j).ljust(2)
        left = ch_n[alb_n.index(result[0])]
        right = ch_n[alb_n.index(result[1])]
        print(f"{ch_n[j]}*{ch_n[i]}={left}{right}",end = " ")
    print ()
