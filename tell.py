import random
import string
# list1 = []
# list1.append
# name_list = []
# name_num = 1
# list1 = [1,3,4,5]
# print(list1)

temp = input('please input wendu(例如 1rmb 或者 1usd):')
if temp.endswith('rmb'):
    temp = float(temp.strip(string.ascii_letters))
    usd = temp / 6.78
    print(f'{temp}rmb = {temp}/6.78 = {usd}usd')
elif temp.endswith('usd'):
    temp = float(temp.strip(string.ascii_letters))
    rmb=  temp * 6.78
    print(f'{temp}usd = {temp} * 6.78 = {rmb}rmb')
else:
    print('bye')