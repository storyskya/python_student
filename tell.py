dict1 = {'a':1,'b':2,'c':3}
print(id(dict1))
dict2 = dict1.copy()
print(id(dict2))
dict2['a'] = 3
print(dict1)
print(dict2)
