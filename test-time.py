#!/bin/python
from datetime import date
from datetime import time
from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
import time

# d = date(2033,1,13)
# # print(d)
# f = time(12,12)
# u = timedelta(days=5)
# t = date.today()
# x = t + u * 3
# # print(d + u * 3)
# # print(x)
# print(x - u)
# t = time.time()
# # print(t)
# b = datetime.utcfromtimestamp(t)
# print(f'{b:%Y-%m-%d}',b)

# dt = datetime(1111,8,8,8,8)
# # print(dt)
# print(dt.strftime('%Y/%m/%d %X'))
# print(f'{dt:%Y/%m/%d %X}')
d = datetime.now()
# print(d)
# print(d + relativedelta(weekday=WE))
# print(d + relativedelta(weekday=WE,weeks = -1))
# print(date(2019,1,30) + relativedelta(months=+3))

print("Loading",end = "")
for i in range(6):
    print(".",end = '')
    time.sleep(1)