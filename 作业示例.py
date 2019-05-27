#! /usr/bin/env python
# -*- coding:utf-8 -*-
# unit_conversion.py
# author : orient

import string


class Temper_trans:
    """ 温度转换类 """
    def __init__(self, values: str):      
        self.svalue = values
       
    def c_f_trans(self):
        """ 摄氏转华氏 """     
        Tf = 0.0
        if self.svalue.endswith('c'):
            try:
                temperv = float(self.svalue.strip('c'))
                Tf = (9 / 5) * temperv + 32 
            except Exception as e:
                print('输入非法值，请重新开始')
                return
        else:
            return self.svalue
        return str(f'{Tf}F')

    def f_c_trans(self):
        """ 华氏转摄氏"""
        Cf = 0.0
        if self.svalue.endswith('f'):
            try:
                temperv = float(self.svalue.strip('f'))
                Cf = (temperv - 32) * (5 / 9) 
            except Exception as e:
                print('输入非法值，请重新开始')
                return
        else:
            return self.svalue
        return str(f'{Cf}C')


class Currency_trans:
    """ 货币转换类 """
    def __init__(self, values: str):      
        self.svalue = values   
       
    def m_r_trans(self):
        """ 美元转人币币 """     
        money = 0.0
        if self.svalue.endswith('usd'):                
            try:
                tempm = float(self.svalue.strip('usd'))
                money = tempm * 6.8870
            except Exception as e:
                print('输入非法值，请重新开始')
                return
        else:
            return self.svalue
        return str(f'{money}CNY')

    def r_m_trans(self):
        """ 人币币转美元 """
        money = 0.0
        if self.svalue.endswith('cny'):              
            try:
                tempk = float(self.svalue.strip('cny'))
                money = tempk * 0.1452
            except Exception as e:
                print('输入非法值，请重新开始')
                return
        else:
            return self.svalue
        return str(f'{money}USD')


class Length_trans:
    """ 长度转换类 """
    def __init__(self, values: str):      
        self.svalue = values   
       
    def A_C_trans(self):
        """ 英里转公里 """     
        lengthv = 0.0
        if self.svalue.endswith('mi'):
            try:
                tempm = float(self.svalue.strip('mi'))
                lengthv = tempm * 0.6213712
            except Exception as e:
                print('输入非法值，请重新开始')
                return
        else:
            return self.svalue
        return str(f'{lengthv}km')

    def C_A_trans(self):
        """ 公里转英里 """
        lengthv = 0.0
        if self.svalue.endswith('km'):
            try:
                tempk = float(self.svalue.strip('km'))
                lengthv = 1.609344 * tempk
            except Exception as e:
                print('输入非法值，请重新开始')
                return
        else:
            return self.svalue
        return str(f'{lengthv}mi')


class Transfer:
    """ 处理主程序类 """
    def __init__(self, seltype: str):      
        self.stype = seltype
    
    def dotransfer(self):        # 转换主方法
        ''' 单位转换主方法 '''
        if self.stype == 't':
            temp = str(input('请输入温度（示例:2C或2F）'))
            temp = temp.strip()
            if temp == '' or len(temp) < 2 or (temp.lower().find('c') == -1 and temp.lower().find('f') == -1):
                print('输入非法值，请重新开始')
                return
            
            temper = Temper_trans(temp)
            res1 = temper.c_f_trans()
            res2 = temper.f_c_trans()
            if temp != res1:
                print(f'摄氏温度{temp}转华氏温度为{res1}')
            else:
                print(f'华氏温度{temp}转摄氏温度为{res2}')
        elif self.stype == 'l':
            temp = str(input('请输入长度公里或英里数（示例:2km或2mi）'))
            temp = temp.strip()
            if temp == '' or len(temp) < 3 or (temp.lower().find('km') == -1 and temp.lower().find('mi') == -1):
                print('输入非法值，请重新开始')
                return

            temper = Length_trans(temp)
            res1 = temper.A_C_trans()
            res2 = temper.C_A_trans()
            if temp != res1:
                print(f'英里{temp}转公里为{res1}')
            else:
                print(f'公里{temp}转英里为{res2}')
        elif self.stype == 'c':
            temp = str(input('请输入货币美元或人民币（示例:2CNY或2USD）'))
            temp = temp.strip()
            if temp == '' or len(temp) < 4 or (temp.lower().find('cny') == -1 and temp.lower().find('usd') == -1):
                print('输入非法值，请重新开始')
                return

            temper = Currency_trans(temp)
            res1 = temper.m_r_trans()
            res2 = temper.r_m_trans()
            if temp != res1:
                print(f'美元{temp}转人民币为{res1}')
            else:
                print(f'人民币{temp}转美元为{res2}')


class Helper:
    @staticmethod
    def welcome():
        ''' 欢迎内容 '''
        print('欢迎使用万能转换器'.center(30, '*'))
        menu = {
            'T': '温度转换',
            'L': '长度转换',
            'C': '货币转换'  
        }
        for k, v in menu.items():
            print(k, v)

    @staticmethod
    def get_choose():
        ''' 获得用户选择内容 '''
        choose = input('请输入转换类型（不区分大小写,t,l,c,不输入内容按回车退出）：')
        choose = choose.strip()
        return choose

    @staticmethod
    def get_is_run(choose):
        ''' 判断用户选择是否可继续 '''
        return choose != '' and string.ascii_lowercase.find(choose.lower()) != -1 

    @staticmethod
    def dowhile(is_run, choose):
        ''' 主实现逻辑，递归 '''
        while(is_run):
            tf = Transfer(choose)
            tf.dotransfer()
            choose = Helper.get_choose()
            is_run = Helper.get_is_run(choose)
        else:
            if choose == '':
                print('退出转换器') 
            else:
                print('输入非法值，请重新输入')
                choose = Helper.get_choose()
                is_run = Helper.get_is_run(choose)
                Helper.dowhile(is_run, choose)  # 递归实现


def main():
    Helper.welcome() #输出帮助
    choose = Helper.get_choose() # 得到用户选择的输入
    is_run = Helper.get_is_run(choose) #判断 选择输入格式是否正确 返回布尔值
    Helper.dowhile(is_run, choose)      # 主逻辑递归实现
if __name__ == '__main__':
    main()