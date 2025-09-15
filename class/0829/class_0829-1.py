#定數迴圈與不定數迴圈
#定數迴圈-for 迴圈 :確定要重複的具體次數
#不定數迴圈-while 迴圈 :不確定重複次數，但知道停止條件

#不定迴圈範例一
'''
from random import randint
a = 1
while a == 1:
    for i in range(1 ,7):
        num = randint(1,49)
        print('%3d'%num,end='')
    print()
    a = int(input('繼續請按1，結束請按任意件'))
print('結束')
'''
#不定迴圈範例二
'''
while True:
    a = input('請輸入內容')
    if a == 'q':
        break
    print(a)
print('結束')
'''
#不定迴圈範例三
#自動命題
'''
from random import randint
num1 = randint(1 ,200)
num2 = randint(1 ,200)
while True: # 建立一個無限迴圈 裡面的程式碼會一直重複執行 直到遇到 break 為止
    sol = num1 + num2 #將正確達案儲存到變數sol
    a = int(input(f'{num1}+{num2}=')) #畫面印出加法題目 將使用者輸入的數字存到變數 a
    if a == sol: # 判斷使用者輸入的答案 a 是否等於 (==) 正確答案 sol
        print('答對')
        break #正確就使用 break 來跳出 while 迴圈
    else:     #if 判斷不成立 沒有break 迴圈會回到最上面 讓使用者再答一次
        print('答錯 繼續猜')
print('結束')
'''
#不定迴圈範例四
'''
from random import randint
from random import choice
num1 = randint(1 ,200)
num2 = randint(1 ,200)
op = choice(['+' , '-' , '*' , '/'])
while True: # 建立一個無限迴圈 裡面的程式碼會一直重複執行 直到遇到 break 為止
    if op == '+':
        sol = num1 + num2 #將正確達案儲存到變數sol
    elif op == '-':
        if num1 < num2:
            num1 , num2 = num2 , num1
        sol = num1 - num2
    elif op == '*':
        sol = num1 * num2
    elif op == '/':
        if num1 < num2:
            num1 , num2 = num2 , num1
        sol = num1 / num2
    a = int(input(f'{num1} {op} {num2}='))
    if a == sol: # 判斷使用者輸入的答案 a 是否等於 (==) 正確答案 sol
        print('答對')
        break #正確就使用 break 來跳出 while 迴圈
    else:     #if 判斷不成立 沒有break 迴圈會回到最上面 讓使用者再答一次
        print('答錯 繼續')
print('結束')
'''
#continue用法
#列出1-100的數 但排除5的倍數 再將顯示的數字都相加
total = 0
count = 0
for i in range(1 ,101):
    if i % 5 == 0:
        continue
    print('%3d' %i ,end=' ')
    count += 1
    if count % 10 == 0:
        print()
    total += i
print()
print(f'總和為{total}')