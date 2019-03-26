# 
# print(ip_add)
# mydict = {'a':"1",'b':'2'}
# print(mydict.get('c','1'))
# mydict['c'] = '333'
# print(mydict)
# from collections import defaultdict
is_add = True
all_time = 0
all_memo=[]
while(is_add):
    in_date = input('riqi: ')
    in_thing = input('shijian: ')
    in_time = input('yongshi: ')
    print('list'.center(30,'-'))
    one = {}
    one['date'] = in_date
    one['thing'] = in_thing
    one['time'] = in_time
    all_memo.append(one)
    all_time += int(in_time)
    num = 0
    for m in all_memo:
        num +=1
        print('%s:%s' %(num,m))

    print(f'共{len(all_memo)}条事物,时长:{all_time}',end ='')
    print(all_memo)
    print(one)
    print('y/n')
    
    is_add = input().strip() == 'y'
