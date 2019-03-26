import random
stuInfo = {'westos'+ str(i):random.randint(60,100) for i in range(20)}
# print({name:score for name,score in stuInfo.items() if score > 90})
print(stuInfo)