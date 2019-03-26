count = 0       #总和
ev_count = 0    #偶数和
odd_count = 0   #奇数和

i = 0
#for i in range(1,101):
while i <= 100:
    count += i
    if i%2 == 0:
    	ev_count += i
    else:
    	odd_count += i
    i += 1

print '总和是：%d' % count
print '偶数和是: %d' % ev_count
print '奇数和是: %d' % odd_count
while :
    pass
    