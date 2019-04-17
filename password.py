#/bin/python
import string
import random


def random_pwd(count):
    str_from = string.ascii_letters + string.digits
    str_list = []
    for i in range(count):
        random_str = random.choice(str_from)
        str_list.append(random_str)
    str_pwd = ''.join(str_list)
    return str_pwd
print(random_pwd(9))
