#!/bin/python
import string
import os


data = [{
    'id':1,
    'time':'1.2',
    'thiht':'buy a coat'
},{
    'id':2,
    'time':'1.8',
    'thing':'gave d8g a PI'
},{
    'id':6,
    'time':'3.8',
    'thing':'写个代码'
}

]

base_dir = 'D:\python-start'
data_path = os.path.join(base_dir,'data.txt')
# with open(data_path,'a',encoding = 'utf-8') as f:
#     for db in data:
#         print(db.values())
#         line = '-'.join([str(x) for x in db.values()])
#         f.write(line + '\n')

def save_dic(dic):
    ret = {'status':0, 'statusText':'saved'}
    try:
        with open(data_path,'a',encoding = 'utf-8') as f:
            for db in data:
                print(db.values())
                line = '-'.join([str(x) for x in db.values()])
                f.write(line + '\n')
    except Exception as e:
        print(e)
        ret['status'] = 1
        ret['statusText'] = e
    return ret

save_dic(data)
