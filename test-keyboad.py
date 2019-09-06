#!/bin/python
import string
import random

def get_time():
    run_time = random.choice(string.digits)
    return(run_time)

def get_direction():
    direction_key = ['w','s','a','d','q','e']
    get_key = random.choice(direction_key)
    return(get_key)

print(get_direction())
print(str(get_direction()))

action = random.randrange(1,6)
print(action)
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# slice = random.sample(list, 5)
