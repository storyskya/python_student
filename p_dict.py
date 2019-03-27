#!/usr/bin/python
print('Wellcome my Dict'.center(30,'-'))
print(30*'-')
orig_dict ={'中文':'Chinese','书':'book','超人':'superman'}
query = input('plese input what you find mast be Chinese:')
if (orig_dict.get(query,'')):
    print ( f'your find Chinese is:{query},That is:{orig_dict[query]}' )
else:
    add = input('Nothing found,Do you want add it?(y/n)')
    if add == 'y':
        print(orig_dict)
        print('Thank you, You can input new word use :to split')
        
        worlds = input('like this:(鸟：birld)')
        worlds = worlds.split(':')
        orig_dict[worlds[0]]=worlds[1]
        print(orig_dict)
    else:
        print('bye')
print('END'.center(30,'-'))
# -*- coding=utf-8 -*-
print()
print()
