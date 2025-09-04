#結合亂數模組運用
from random import randint

# times3 = 0
# times5 = 0
# times7 = 0
# others = 0
# count = 1
# for i in range(1, 101):
#     num = randint(1, 100)
#     print('%4d' % num, end=' ')
#     Flag = False
#     if count % 10 == 0:
#         print()
#     count += 1
#     if num % 3 == 0:
#         times3 += 1
#         Flag = True
#     if num % 5 == 0:
#         times5 += 1
#         Flag = True
#     if num % 7 == 0:
#         times7 += 1
#         Flag = True
#     if Flag == False:
#         others += 1
# print(f'\n3的倍數有{times3}個,5的倍數有{times5}個,7的倍數有{times7}個,都不是的有{others}個')

#=====================================
#另一種寫法 不使用Flag
# times3 = 0
# times5 = 0
# times7 = 0
# others = 0
# for i in range(1, 101):
#     print('%4d' % num, end=' ')
#     if count % 10 == 0:
#         print()
#     count += 1
#     num = randint(1, 100)
#     if num % 3 == 0:
#         times3 += 1
#     if num % 5 == 0:
#         times5 += 1
#     if num % 7 == 0:
#         times7 += 1
#     if (num % 3 != 0) and (num % 5 != 0) and (num % 7 != 0):
#         others += 1
# print(f'\n3的倍數有{times3}個,5的倍數有{times5}個,7的倍數有{times7}個,都不是的有{others}個')

#=====================================

#詳列同為3&5、3&7、5&7倍數的個數，以及僅為3、5、7倍數的個數共有多少個，讓總個數加總等於100
times35 = 0
times37 = 0
times57 = 0
times3 = 0
times5 = 0
times7 = 0
others = 0
count = 1
for i in range(1, 101):
    num = randint(1, 100)
    print('%4d' % num, end=' ')
    if count % 10 == 0:
        print()
    count += 1
    if num % 3 == 0 and num % 5 == 0:
        times35 += 1
    elif num % 3 == 0 and num % 7 == 0:
        times37 += 1
    elif num % 5 == 0 and num % 7 == 0:
        times57 += 1
    elif num % 3 == 0:
        times3 += 1
    elif num % 5 == 0:
        times5 += 1
    elif num % 7 == 0:
        times7 += 1
    else:
        others += 1
print(f'是3也是5的倍數有{times35}個,是3也是7的倍數有{times37}個,是5也是7的倍數有{times57}個,是3的倍數有{times3}個,是5的倍數有{times5}個,是7的倍數有{times7}個,都不是的有{others}個')

    