#coding: utf-8
import random
import math
import pickle
import os


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
# ch_n = [' ','一','二','三','四','五','六','七','八','九','零']
# alb_n = [' ','1','2','3','4','5','6','7','8','9','0']
# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         result = str(i*j).ljust(2)
#         left = ch_n[alb_n.index(result[0])]
#         right = ch_n[alb_n.index(result[1])]
#         print(f"{ch_n[j]}*{ch_n[i]}={left}{right}",end = " ")
#     print ()
# list1 = [1,3,4,5,6]
# print(len(list1)+1)

# with open('db.pkl','rb') as f:
#     zong_list = pickle.load(f)
#     print(zong_list[1]['日期'])

# for k in e[1].keys():
#     if k == 'ID':
#         print(e[1][k])



# NewId = len(self.zong_list)
# for ListNum in range(len(self.zong_list)):
#     for k in self.zong_list[ListNum].keys():
#         if k == 'ID':
#             if NewId == self.zong_list[ListNum][k]:
#                 self._id = len(self.zong_list) + 1
#             else:
#                 self._id = len(self.zong_list)
# return(self._id)
# if len(zong_list) != 0:
#     for k in zong_list[-1].keys():
#         if k == 'ID':
#             RealId = zong_list[-1][k] + 1
# else:
#     RealId = 0
# print(RealId)
cdir = r"c:"
# for i in os.listdir(cdir):
#     print(i)
# print(os.getcwd())
# os.chdir(r'C:\windows')
# print(os.getcwd())
# os.chdir(r'D:\Download')
# os.mkdir(r'testdir')
# print(os.getcwd())
# print(os.path.relpath('C20190604.gho',r'd:\python-start\class.py'))
import shutil
p = r'C:\Program Files (x86)\Acer\Care Center\ACCStd.exe'
b = r'c:\\'
d = 'D:/Download/'
e = 'D:/python-start/'
# print(os.path.sep)
# print(p.split(os.path.sep))
# print(os.path.split(p))
# print(os.path.splitext(r'C:\Program Files (x86)\Acer\Care Center\ACCStd.exe'))
# print(os.path.basename(b))
# print(os.path.dirname(p))
# print(os.getcwd())
# shutil.copytree(d'testdir',d'ufo')
# shutil.copy('db.pkl','dir1')
# print(os.path.getsize(p))
# print(os.path.isfile(p))
# print(os.path.isdir(d))
# print(os.stat(b))
# print(p[-2:])
import re
import zipfile
re_name = re.compile('(.*pdf$)|(.*exe$)|(.*py$)')
# print(re_name.match(p).group(1))
# print(os.walk('.'))
my_zip = zipfile.ZipFile('python-start.zip','w')
# for a,b,c in os.walk(e):
#     for name in c:
#         file = os.path.join(a,name)
#         if re_name.match(file) and os.path.getsize(file) > 1024:
#             my_zip.write(file,compress_type=zipfile.ZIP_DEFLATED)
# my_zip.close()
# my_zip = zipfile.ZipFile('python-start.zip','w')
# my_zip.write('class.py',compress_type=zipfile.ZIP_DEFLATED)
# my_zip.write('cgi.py',compress_type=zipfile.ZIP_DEFLATED)
# my_zip.close()
# look_zip = zipfile.ZipFile('python-start.zip')
# print(look_zip.namelist())
# print(look_zip.getinfo('python-start/21point.py'))
import fnmatch
import glob

# for f in os.listdir(e):
#     if fnmatch.fnmatch(f,'*.txt'):
#         print(f)
#     elif fnmatch.fnmatch(f,'*.py'):
#         print('find pdf',f)

# for fd in glob.glob('[a-z].py'):
#     print(fd)
import io
# output = io.StringIO()
# output.write('onelinecode\n')
# print('test print to file:',file = output)

# cc = output.getvalue()
# print(cc)

# output.close()
import shelve
# with shelve.open('ufo.shelv') as so:
#     so['ttt'] = 'bsdlinux'
#     print(so['ttt'])
#     print(so)
dic1 = {'abc':[1,3,4,5,6],'bcd':9,'ccc':89}
print(dic1.get('ufo'))