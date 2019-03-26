import string
import re
s = 'u1uxx'
# # print(s.strip('f').strip("U"),end = "")
# print(s.strip(string.ascii_letters))
# t = float(s.strip(string.ascii_letters))
# print(type(t))
# # print(re.sub('[A-Za-z]',' ',s))
menu = {
    't':'wendu',
    'l':'changdu',
    'c':'huobi'
}
for k,v in menu.items():
    print(k,v)
print(menu.items())
