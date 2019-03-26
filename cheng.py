#print ( '1*2 =' 1*2 )
#print ( "1*2 =",1*2,end = " ")
#print (123)
import os
for i in range(9,0,-1):
    for j in range(1, i+1):
        # print(j,"*",i," = ",j*i,end= "  ")
        print(f"{j}*{i}= {j*i:2}",end=" ")
    print ()
# for x in range(100,1):
#     print (x)

# for i in range(10,0,-1):
#     for x in range(0,i):
#         print (x,end=" ")
#     print ()

# n = 10
# for i in range(n):
#     for x in range(0,n):
#         print (x,end=" ")
#     n-=1    
#     print ()    