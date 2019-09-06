#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 51memo0814.py
# author : orient

import string
import pickle


class Memo:
    ''' 备忘录实体类 '''
    def __init__(self, id: int, name: str, thing: str, date: str, time: str):      
        self._id = id
        self.date = date
        self.thing = thing
        self.name = name
        self.time = time

    @property
    def id(self):
        return self._id


class MemoAdmin:
    ''' 备忘录管理类 '''
    def __init__(self, author): 
        self.memo_list = []
        self.__author = author 

    def load(self):  
        ''' 加载db.pkl到备忘录实体list '''
        try:
            data1 = ''
            with open('db.pkl', 'rb') as f:
                self.memo_list = pickle.load(f) 
        except Exception as e:
            self.memo_list = []
            print("暂时无数据", e)    

    def save(self):
        ''' 把备忘录实体list保存到db.pkl '''
        with open('db.pkl', 'wb') as f:
            pickle.dump(self.memo_list, f)

    def add(self, mome):
        ''' 添加备忘录并保存 '''
        self.memo_list.append(mome)
        self.save()

    def modify(self, ids, thing, time):
        ''' 修改备忘录并保存 '''
        self.load()
        for memo in self.memo_list:
            if memo.id == ids: 
                memo.thing = thing
                memo.time = time
                self.save()
                print('修改成功')
    
    def delete(self, ids):
        ''' 删除备忘录并保存 '''
        self.load()
        for memo in self.memo_list:
            if memo.id == ids:
                self.memo_list.remove(memo)
                self.save()
                print('删除成功')
    
    def query(self, ids):
        ''' 通过ID查询备忘录并返回 '''
        self.load()
        for memo in self.memo_list:
            if memo.id == ids:
                return memo
        else:
            return '没有查询到'

    def welcome(self): 
        ''' 备忘录启动欢迎相关信息 '''
        descr = '51备忘录'.center(30, "-")
        print(descr)
        print(f'welcome,{self.__author}')
        print('请输入备忘信息：')

    @staticmethod
    def findstr(self, things, strs, in_date, types='a'):
        ''' 上午，下午，中午，晚上，早上，夜里，把用户输入信息转成实体Memo并保存'''        
        nid = self.memo_list.__len__() + 1      # ID实现自增
        memo = Memo(nid, self.__author, '', in_date, "")
        if things.find(strs) >= 0:
            memo.thing = things[things.find('strs')+1:]             
            memo.time = strs
            if types == 'a':        # a代表添加
                self.add(memo)  
            else:
                self.modify(mem.id, mem.thing, mem.time)  

    @staticmethod
    def printlist(self):  
        ''' 每次添加完打印列表结果并提示相关信息 '''
        print('待办列表：'.center(30, "-"))
        num = 0
        for m in self.memo_list:
            num += 1
            d = m.date
            th = m.thing
            tim = m.time
            # print("%s:%s" % (num, m))
            print(f'\033[0m {num}:\033[1;36;47m{d},\033[1;31;47m{th},\033[1;32;47m{tim}')
            
        print(f'\033[0m 共{self.memo_list.__len__()}条待办事项', end='')
        print('\033[0m (y: 继续添加,不输入内容按回车：退出)')
        print('\033[0m (mid修改事件内容(示例m2+3点会见客人),(d+id删除相关事项(示例d2))') 
        print('\033[0m 输入id值为查询，(示例: 1)')   

    @staticmethod
    def str_to_memo(self, mem, in_thing, types='a'):
        ''' 输入字符串转成实体 '''
        in_d = mem.date
        if in_thing.find('点') != -1:
            mem.thing = in_thing[in_thing.find('点')+1:]
            mem.time = in_thing[in_thing.find('点')-1:in_thing.find('点')+1]
            pren = in_thing[in_thing.find('点')-2:in_thing.find('点')-1]
            if string.digits.find(pren) >= 0:
                mem.time = pren + mem.time
            if types == 'a':
                self.add(mem)
            else:
                self.modify(mem.id, mem.thing, mem.time)                
        MemoAdmin.findstr(self, in_thing, '早上', in_d, types)
        MemoAdmin.findstr(self, in_thing, '晚上', in_d, types)
        MemoAdmin.findstr(self, in_thing, '中午', in_d, types)
        MemoAdmin.findstr(self, in_thing, '夜里', in_d, types)
        MemoAdmin.findstr(self, in_thing, '上午', in_d, types)
        MemoAdmin.findstr(self, in_thing, '下午', in_d, types)

    def do_memo(self):
        ''' 主逻辑实现方法 '''
        try:
            is_add = True
            all_time = 0
            while(is_add):
                in_date = str(input("\033[0m 日期（示例：2018-08-14）:")).strip()   
                if in_date == '':
                    break

                in_thing = str(input('\033[0m 提醒事件（示例：8点开始学习英语）:')).strip()
                if in_thing == '':
                    break

                counta = self.memo_list.__len__()
                nid = self.memo_list.__len__() + 1
                mem = Memo(nid, self.__author, '', in_date, "")                
                MemoAdmin.str_to_memo(self, mem, in_thing)               
                if self.memo_list.__len__() == counta:      # 检查是否添加成功
                    print('\033[1;31;47m添加事项失败，请查询输入事项格式是否正确') 
                MemoAdmin.printlist(self)   # 不管添加成功打印所有列表开始后续提示
                mids = input().strip()
                if mids == 'y':     # y继续添加
                    is_add = True
                elif mids.lower().startswith('d'):      # 删除
                    id = int(mids.lower().strip('d'))
                    pco = self.memo_list.__len__()
                    self.delete(id)
                    if pco == self.memo_list.__len__():
                        print('删除失败')
                    MemoAdmin.printlist(self)
                elif mids.lower().startswith('m'):      # 修改
                    idstring = mids.lower().strip('m')
                    arrs = idstring.split('+')
                    id = int(arrs[0])
                    mem1 = Memo(id, self.__author, '', '', '')                
                    MemoAdmin.str_to_memo(self, mem1, arrs[1], 'm')                    
                    MemoAdmin.printlist(self)
                else:
                    if mids == '':      # 不输入内容按回车退出
                        break
                        print('退出')
                    elif int(mids) > 0:     # 通过ID查询备忘录
                        mm = self.query(int(mids))
                        print(f'\033[0m {mm.id}:\033[1;36;47m{mm.date},\033[1;31;47m{mm.thing},\033[1;32;47m{mm.time}')
                    else:
                        print('输入非法值,退出')
                        break
        except Exception as e:
            print('出错了', e)


def main():     # 主函数入口
    memoadmin = MemoAdmin('orient')
    memoadmin.load()
    memoadmin.welcome()
    memoadmin.do_memo()

if __name__ == '__main__':
    main()