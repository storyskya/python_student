import random
import string
# print (random.choice('YIOKJHOIUOI'))
count = 8
u = ""
str_from = string.ascii_letters+string.digits
for i in range(count):
    x = ''.join([random.choice(str_from)])
    u = x+u
print(u)
x = ''.join([random.choice(str_from) for _ in range(count)])
print(x)