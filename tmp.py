# name2_list = []
# five_list = []
# for e in range(0,len(sum4_list)):
#     user_con = input(f'{name1_list[e]} 是否继续？(y/n)')
#     if user_con == 'y':
#         five_list.append(sum4_list[e])
#         name2_list.append(name1_list[e])
#     elif user_con == 'n':
#         end_dict = {name2_list[e]:sum4_list[e]}
#         del user1_dict[name1_list[e]]
# print(end_dict)

# sort_list = []
# user1_dict = {}
# if user1_dict == {}:
#     for u in [1,2,56,77,3,22,20,18]:
#         if u < 21:
#             sort_list.append(u)
#     print(sort_list)
# sort_list.sort(reverse=True)
# print(sort_list)
u = (1,2,4,55,55,5,3,1111)
sorted(u,reverse=True)
print(sorted(u,reverse=True))