 #-*- coding:utf-8 -*-

import string
import re
import os
import pickle


class wendu:
    '''温度转换类'''
    def Hua_She(temp):
        tf = (5/9) * temp - 32
        print("\n")
        print(f'{temp}f = {tf}c')

    def She_Hua(temp):
        tf = (9/5) * temp + 32
        print("\n")
        print(f'{temp}c = {tf}f')

class huobi:
    '''货币转换类'''
    def usd_rmb(temp):
        usd = temp / 6.78
        print("\n")
        print(f'{temp}rmb = {temp}/6.78 = {usd}usd')
    
    def rmb_usd(temp):
        rmb=  temp * 6.78
        print("\n")
        print(f'{temp}usd = {temp} * 6.78 = {rmb}rmb')

class changdu_class:
    def M_ft(temp):
        m = temp * 3.28
        print()
        print(f'{temp}M = {temp} * 3.28 = {m}ft')

    def ft_M(temp):
            ft=  temp / 3.28
            print()
            print(f'{temp}ft = {temp} / 3.28 = {ft}M')

class IO:
    '''输入输出管理类'''
    def wendu(self):
        temp = input('please input 温度(例如 1c 或者 1f):')
        try:
            if temp.endswith('c') or (temp[-1].lower() == 'c'):
                temp = float(temp.strip(string.ascii_letters))
                return(wendu.She_Hua(temp))
            
            elif temp.endswith('f') or (temp[-1].lower() == 'f'):
                temp = float(temp.strip(string.ascii_letters))
                return(wendu.Hua_She(temp))
                
            else:
                print("Please Input c/f")

        except Exception as e:
            print("\n")
            print('Input Error')
            return

    def huobi(self):
        temp = input('please input 货币(例如 1rmb 或者 1usd):')
        try:
            if temp.endswith('rmb') or (temp[-3:].lower() == 'rmb'):
                temp = float(temp.strip(string.ascii_letters))
                return(huobi.rmb_usd(temp))
            
            elif temp.endswith('usd') or (temp[-3:].lower() == 'usd'):
                temp = float(temp.strip(string.ascii_letters))
                return(huobi.usd_rmb(temp))
                
            else:
                print("Please Input rmb/usd")

        except Exception as e:
            print("\n")
            print('Input Error')
            return

    def changdu(self):
        temp = input('please input 长度(例如 1M 或者 1ft):')
        try:
            if temp.endswith('M') or (temp[-1].lower() == 'm'):
                temp = float(temp.strip(string.ascii_letters))
                return(changdu_class.M_ft(temp))
            
            elif temp.endswith('ft') or (temp[-2:].lower() == 'ft'):
                temp = float(temp.strip(string.ascii_letters))
                return(changdu_class.ft_M(temp))
                
            else:
                print("Please Input rmb/usd")

        except Exception as e:
            print("\n")
            print('Input Error')
            return


def main():
    main_api = IO()
    while True:
        print("\n")
        print('Wellcome'.center(30,'*'))
        menu = {
            't':'温度',
            'l':'长度',
            'c':'货币',
            'q':'退出'
        }

        for k,v in menu.items():
            print(k,v)
        choose = input('please select type:')

        if choose == 't':
            choose_api = main_api.wendu()
            choose_api

        if choose == 'c':
            choose_api = main_api.huobi()
            choose_api

        if choose == 'l':
            choose_api = main_api.changdu()
            choose_api

        if choose == 'q':
            print('Bye')
            exit(0)
        if choose not in ['t','c','l','q']:
            print('Are you kidding me???')
            print()

# def main():

#     x = a.wendu()
#     x

# if __name__ == '__main__':
#     main()

class Memo:

    def __init__(self, id, name, thing, date):      
        self._id = id
        self.date = date
        self.thing = thing
        self.name = name
        

class MemoAdmin(Memo):
    '''备忘录主体'''

    def __init__(self): 
        self.zong_list = []

    def Get_ID(self):
        self.load() #提前将db.pkl文件读取到内存

        # NewId = len(self.zong_list)
        # for ListNum in range(len(self.zong_list)):
        #     for k in self.zong_list[ListNum].keys():
        #         if k == 'ID':
        #             if NewId == self.zong_list[ListNum][k]:
        #                 self._id = len(self.zong_list) + 1
        #             else:
        #                 self._id = len(self.zong_list)
        # return(self._id)
        if len(self.zong_list) != 0:
            for key in self.zong_list[-1].keys():
                if key == 'ID':
                    RealId = self.zong_list[-1][key] + 1
        else:
            RealId = 0
        return(RealId)

    def Add_list(self):

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
        self.load()
        if self.zong_list is not None:       
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

    def load(self):  
        ''' 读取db.pkl'''
        try:
            with open('db.pkl', 'rb') as f:
                self.zong_list = pickle.load(f)
        except Exception as e:
                self.save()
        return(self.zong_list)

    def save(self):
        ''' 把记录保存到db.pkl '''
        with open('db.pkl', 'wb') as f:
            pickle.dump(self.zong_list, f)

    def change(self,name, thing, date):
        ''' 修改记录并保存 '''
        self.load()
        for memo in self.memo_list:
            if memo.id == ids: 
                memo.thing = thing
                memo.time = time
                self.save()
                print('修改成功')


a = MemoAdmin()
# a.Add_list()
# a.Find_list()
# a.Del_list()
# a.Look_list()
# a.Change_list()
# a.Add_list()
with open('db.pkl', 'rb') as f:
    list1 = pickle.load(f)
    print(list1[-1].values())
    # del list1[3]
    # for i in list1:
    #     print(i)
    # pickle.dump(list1, f)


