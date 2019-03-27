import string
import random
my_dict = {
    "a":1,"b":2
}

my_dict['b'] = 9
dict_list = [string.ascii_letters + string.digits]
my_book = {
    "linux":7.0,
    "windows":10
}

# print (dict_list)
# print (my_dict.get("c","xman"))
my_dict["c"] = 88
my_dict["list"] = dict_list
my_dict["book"] = my_book
del my_dict['a']
x = [ i for i in my_dict.keys()]
# print (x)
# print (my_dict.items())
# # print (my_dict['book']["linux"])
# # print (my_dict.keys())
# print()
# for item in my_dict.items():
#     print(item)
# for key,value in my_dict.items():
#     print(f'{key}:{value}')
my_book = {
    "linux":7.0,
    "windows":10
}
print(my_book.get('igpz',''))
print(my_book.get('linu'))