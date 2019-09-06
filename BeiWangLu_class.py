#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename BeiWangLu_class.py
# author MaxD

import string
import pickle


class Memo:
    '''初始化类'''
    def __init__(self, id, name, thing, date):      
        self._id = id
        self.date = date
        self.thing = thing
        self.name = name
        

#备忘录主体
class MemoAdmin(Memo):
    '''用于增删改查'''
    def __init__(self): 
        self.zong_list = []

    def Get_ID(self): 
        '''该函数作用为 ID 获取，并根据删除后的通讯录条目数重新分配ID'''
        self.load() #提前将db.pkl文件读取到内存
        if len(self.zong_list) != 0:
            for key in self.zong_list[-1].keys():
                if key == 'ID':
                    RealId = self.zong_list[-1][key] + 1
        else:
            RealId = 0
        return(RealId)

    def Add_list(self):
        '''添加内容函数'''
        self.date = input('请输入日期（例如 1.30）: ')
        self.name = input('请输入人物（例如 小明）: ')
        self.thing = input('请输入待办事项（例如 开会）: ')
        self._id = self.Get_ID()

        Thing_dict = {
        'ID':self._id,
        '日期':self.date,
        '人名':self.name,
        '待办事项':self.thing
        }

        self.zong_list.append(Thing_dict)  #将新内容追加到 'zong_list'
        self.save()
        return()

    def Find_list(self):
        '''根据输入内容查找所有匹配的记录'''
        self.load()
        if len(self.zong_list) != 0 :       
            Find_con = input('请输入查询内容（例如 1.30或10:28或开会 ）: ')
            for list_num in range(len(self.zong_list)):
                # for Find_con in zong_list[list_num]:
                if Find_con in self.zong_list[list_num].values():
                    # print (zong_list[list_num].items())
                    for k,v in self.zong_list[list_num].items():
                        print (k,v)
                    print()
        else:
            print('请增加备忘录内容')

    def Del_list(self):
        '''根据内容删除某条备忘录'''
        self.load()
        if len(self.zong_list) != 0:
            Del_con = input('可根据条目内容删除某个事件（例如 输入10:30则将删除该时间点的一条记录）：')
            for list_num in range(len(self.zong_list)):
                if Del_con in self.zong_list[list_num].values():
                    print(self.zong_list[list_num])
                    Del_yn = input('是否删除这条备忘录？(y/n)')
                    if Del_yn == 'y':
                        del self.zong_list[list_num]
                        break
                    elif Del_yn == 'n':
                        continue
                    elif len(self.zong_list) == 0:
                        f = '目前备忘录已被清空'
                        print (f'\n {f} \n')
        self.save()

    def Look_list(self):
        self.load()
        if len(self.zong_list) != 0:
            for i in range(len(self.zong_list)):
                for k,v in self.zong_list[i].items():
                    print (k,v)
                print ('_'*30)
        elif len(self.zong_list) == 0:
            f = '目前备忘录没内容'
            print(f'\n {f} \n')

    def Change_list(self):
        '''根据输入的内容来修改备忘录'''
        self.load()
        if len(self.zong_list) != 0:
            Change_con = input('可根据条目内容修改某个事件（例如 输入10:30则将修改该时间点的一条记录）：')
            for list_num in range(len(self.zong_list)):
                if Change_con in self.zong_list[list_num].values():
                    print(self.zong_list[list_num])
                    Change_yn = input('是否修改这条备忘录？(y/n)')
                    if Change_yn == 'y':
                        New_date = input('新的日期: ')
                        New_thing = input('新的事件: ')
                        New_name = input('新的名字: ')
                        self.zong_list[list_num].update({'日期':New_date,'人名':New_name,'待办事项':New_thing})
                        break
                    elif Change_yn == 'n':
                        continue
                    elif len(self.zong_list) == 0:
                        f = '目前备忘录没有内容'
                        print (f'\n {f} \n')
        self.save()
    
    def load(self):  
        ''' 加载db.pkl到内存'''
        try:
            with open('db.pkl', 'rb') as f:
                self.zong_list = pickle.load(f)
        except Exception as e:
                self.save()
        return(self.zong_list)

    def save(self):
        ''' 把备忘录保存到db.pkl '''
        with open('db.pkl', 'wb') as f:
            pickle.dump(self.zong_list, f)

def main():

    while True:
        choose = input('''
        请选择如下几种操作:
        \n
        A 增加备忘录内容
        C 修改备忘录内容
        F 查找备忘录内容
        D 删除备忘录内容
        L 列出所有内容
        Q 退出
        \n
        ''')

        Func_API = MemoAdmin()

        if choose == 'A':
            Func_API.Add_list()

        if choose == 'F':
            Func_API.Find_list()

        if choose == 'C':
            Func_API.Change_list()

        if choose == 'D':
            Func_API.Del_list()

        if choose == 'L':
            Func_API.Look_list()

        if choose == 'Q':
            print('Bye')
            exit(0)
        if choose not in ['A','F','D','Q','L','C']:
            print('Are you kidding me???')
            print()

if __name__ == '__main__':
    main()