#for迴圈

for i in range(11):     #起始值默認為0 i<11 每一迴圈默認+1
    print(i)

for i in range(1,11):   #起始值為1 i<11 每一迴圈默認+1
    print(i)

for i in range(1,11,2): #起始值為1 i<11 每一迴圈+2
    print(i)

total = 0
# i = 1           
# while i < 101: 
#     total += i   #total = total + i
#     i += 1      
# print('total =', total) 
# 可將以上寫為
for i in range(1, 101, 1):
    total += i 
print('total =', total)
