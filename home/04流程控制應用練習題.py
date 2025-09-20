from random import randint
#1.利用迴圈讓使用者輸入10次數字 後將這10個數字的最小值輸出

a = int(input("請輸入數字: "))
min = a #假設使用者第一個輸入的數字 a 就是目前為止最小的數字 先把 a 的值儲存到 min
for i in range(10-1): #外面已經有一次了所以這邊減少一次
    a = int(input("請輸入數字: ")) 
    if a < min: #判斷新輸入的數字 a 是否小於我們目前記錄的最小值 min
        min = a #若判斷成立 表我們找到了一個更小的值 把這個更小的數字 a 存到 min 變數裡
print(f'最小值為{min}')


#2.使用者輸入任意數 輸入9999時結束 然後找出輸入目前為止的最小數

a = int(input("請輸入任意數: "))
while True:
    num = int(input("請輸入任意數: "))
    if num == 9999:
        break
    else:
        if num < a:
            a = num
print(f'最小的數值是{a}')

#===============第二種寫法===============
#但此方法會記錄9999作為一個數值

a = int(input("請輸入任意數: "))
while a != 9999:
    num = int(input("請輸入任意數: "))
    if num < a:
        a = num
    
print(f'最小的數值是{a}')




#3.使用者輸入a,b兩個正整數(a<b) 輸出從a到b之間所有的4與9的倍數(一列10個數字 欄寬4 靠左對齊) 並且輸出4或9的倍數有機個 並且加總是多少

a= int(input('請輸入正整數a: '))
b= int(input('請輸入正整數b:'))
count = 0
sum = 0
if a > b:
    a , b = b , a
for i in range(a, b+1):
    if i % 4 == 0 or i % 9 == 0:
        print('%-4d'%i, end=" ")
        count += 1
        sum += i
        if count % 10 == 0:
            print()
print()
print(f"4或9的倍數有{count}個")
print(f"加總是{sum}")


#4.輸入一個正整數 將正整數以反轉的順序輸出

a = int(input("請輸入一個正整數: "))
b = 0
while a > 0:
    b = b * 10 + a % 10
    a //= 10
print(f'反轉後的數字為: {b}')


#5.輸入一個代表成績的正整數 根據分數等級對照 輸入9999時結束迴圈

a = int(input("請輸入成績: "))
if 100 >= a >= 0:    
    while a != 9999:
        if 100 >= a >= 90:
            print("A")
        elif 90 > a >= 80:
            print("B")
        elif 80 > a >= 70:
            print("C")
        elif 70 > a >= 60:
            print("D")
        else:
            print("E")
        a = int(input("請輸入成績: "))
else:
    print("輸入錯誤")
print("結束")


#6.以迴圈方式 提供使用者反覆輸入身高與體重 幫忙計算BMI到小數點後兩位 並列出過輕-肥胖 直到輸入9999退出迴圈 

cm = int(input("請輸入身高(公分): "))
kg = int(input("請輸入體重(公斤): "))
while True:
    bmi = kg / (cm/100)**2
    if bmi < 18.5:
        print(f'你的BMI為{bmi:.2f},判定為過輕')
    elif 18.5 <= bmi < 24.9:
        print(f'你的BMI為{bmi:.2f},判定為正常')
    elif 25 <= bmi < 29.9:
        print(f'你的BMI為{bmi:.2f},判定為過重')
    else:
        print(f'你的BMI為{bmi:.2f},判定為肥胖')
    if cm == 9999 or kg == 9999:
        break
    cm = int(input("請輸入身高(公分): "))
    kg = int(input("請輸入體重(公斤): "))
print("退出程式")


#7. 以迴圈方式讓使用者翻覆輸入西元年並判斷是否為閏年  直到輸入9999退出

year = int(input("請輸入西元年: "))
while True:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'{year}為閏年')
    else:
        print(f'{year}不是閏年')
    if year == 9999:
        break
    year = int(input("請輸入西元年: "))
print("結束")


#8.輸入兩個西元年份 並且顯示這兩個年份之間的所有閏年 每一列顯示10筆資料

count = 0
year1 = int(input("請輸入第一個西元年份: "))
year2 = int(input("請輸入第二個西元年份: "))
if year1 > year2:
    year1 , year2 = year2 , year1
for i in range(year1, year2+1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print('%4d'%i, end=" ")
        count += 1
        if count % 10 == 0:
            print()


#9.輸入三個正整數a, b, c然後求最大公因數

a = int(input("請輸入正整數a: "))
b = int(input("請輸入正整數b: "))
c = int(input("請輸入正整數c: "))
if a > b:
    a , b = b , a
if b > c:
    b , c = c , b
if a > c:
    a , c = c , a
for i in range(a, 0, -1): #從最小的數開始往下找 都可以被整除的就是公因數
    if a % i == 0 and b % i == 0 and c % i == 0:
        x = i
        print(f'最大公因數為{x}')
        break



#10.一個數若恰巧等於他的因數之和稱為完美數 設計一個for迴圈 輸入一個值 找出這個值以內的所有完美數

a = int(input("請輸入正整數: "))

for i in range(1, a+1):        #外層的 for 迴圈 從 1 開始，一個一個檢查到 a 為止的所有數字 變數 i 在每一輪迴圈中，會代表當前正在被檢查的數字
    sum = 0                    #每一輪檢查開始時 宣告一個變數 sum 並將它設為 0 且每次檢查新的 i 時，都要把 sum 歸零，才不會影響到計算
    for j in range(1, i):      #內層的 for 迴圈 目的是找出 i 的所有「真因數」因為真因數不包含數字本身，所以只檢查到 i-1
        if i % j == 0:         # % (取餘數) 來判斷 j 是否為 i 的因數
            sum += j           #如果 j 是 i 的因數，就把它加到 sum 裡面
                               #內層迴圈跑完後，sum 就會是 i 的所有真因數的總和
    if sum == i:               #判斷「真因數總和 (sum)」是否剛好等於「數字本身 (i)」
        print(i,end=' ')
print(f'是從1到{a}的所有完美數')
