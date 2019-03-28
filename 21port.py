import random
import string
import re
'''
21 点游戏
'''
user1_win = 0
user2_win = 0
user1 = input('user1\'s name: ')
user2 = input('user2\'s name: ')
print(f'玩家名: {user1},{user2}')
users = {
    user1:
    {'win':0},
    user2:
    {'win':0}
}
while True:

    target = 21

    print(users)

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    user1_guess = input(user1+' guess: ')
    user2_guess = input(user2+' guess: ')

    user1_sum = int(num1) + int(num2) + int(user1_guess)
    user2_sum = int(num1) + int(num2) + int(user2_guess)

    if abs(user1_sum-21) > abs(user2_sum-21):
        print(f'{user1_sum}',f'{user2_sum}')
        print(f'{user2} win')
        user2_win += 1
        users[user2]['win'] = user2_win
    else:
        print(f'{user1} win')
        user1_win += 1
        users[user1]['win'] = user1_win
    print(users)
    print(f'随机数为{num1}和{num2}')
    kaiguan = input('还继续吗？(y/n)')
    if kaiguan == 'n':
        print('bye')
        break
    elif kaiguan == 'y':
        continue