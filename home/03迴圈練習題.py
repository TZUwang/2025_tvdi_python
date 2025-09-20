#1.使用者輸入兩個正整數a,b(a<b) 利用迴圈計算a連加到b的總和
a = int(input('請輸入一個正整數a:'))
b = int(input('請輸入一個正整數b:'))
if a > b:
        a , b = b , a
sum = 0
for a in range(a,b+1):
    sum += a
print(sum)


#2.使用者輸入兩個正整數a,b(a<b) 利用迴圈計算a連加到b的偶數總和
a = int(input('請輸入一個正整數a:'))
b = int(input('請輸入一個正整數b:'))
if a > b:
        a , b = b , a
if a % 2 == 1:
        a += 1
sum = 0
for a in range(a,b+1,2):
        sum += a
print(sum)


#3.使用者輸入一個正整數(<30) 以三角形方式輸出階乘結果
a = int(input('請輸入一個正整數:'))

if not (0 < a < 30):
    print(f"輸入錯誤，請輸入一個介於 1 到 29 之間的正整數。")
else:
    result = 1 
    for i in range(1, a + 1):
        for j in range(1, i + 1, 1):
            print(i * j, end=" ")
        print()


#4.使用者輸入一個正整數a 利用迴圈計算1到a之間所有5倍數的和
a = int(input('請輸入一個正整數:'))

if a > 0:
    total = sum(range(5, a + 1, 5))
    print(f"從 1 到 {a} 之間所有 5 的倍數總和是: {total}")
else:
    print("請輸入一個正整數。")


#5.使用者輸入一個正整數a 將此數反轉順序輸出 EX:輸入31528 輸出82513
a = int(input('請輸入一個正整數a: '))

if a <= 0:
        print("請輸入一個正整數。")
else:
    reversed_a = 0  
    while a > 0:
        b = a % 10    #取得最後一位數
        reversed_a = (reversed_a * 10) + b #將最後一位數加到反轉後的數字上
        a = a // 10   #移除原數字的最後一位數         
    print(f"反轉結果是: {reversed_a}")

#6.使用者輸入一個正整數n 利用迴圈計算n!的值
n = int(input('請輸入一個正整數n: '))
if n > 0:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{n}! = {result}")
else:
    print("請輸入一個正整數。")

#7.使用者輸入一個正整數n (n < 10)，顯示 n*n乘法表
#每項運算式格式化排列整齊，每個運算子與運算元輸出的欄寬為2，而每項乘積輸出的欄寬為4，皆靠左對齊不跳行
a = int(input("請輸入一個正整數n (n < 10): "))
if a < 10:
    for i in range(1, a+1):
        for j in range(1, a+1):
            print(f"{j:<2d}*{i:<2d}={i*j:<4d}", end="")
        print()
else:
    print("輸入錯誤！數字不能大於或等於10")

#8.讓使用者輸入一個正整數，代表後面要測試的次數。 每次測試都是輸入一個正整數，將所有位數加起來輸出結果
a = int(input("請輸入要測試的次數:"))
for i in range(a):
    b = int(input("請輸入一個正整數:"))
    c = 0
    for i in range(b):
        c += b % 10
        b //= 10
    print(f'數字拆開後相加為{c}')
#9.使用者輸入一筆存款金額、年利率及經過的月份，並顯示每個月存款總額。輸出到小數點第二位數
    
a = int(input("請輸入要存款的金額:"))
b = float(input("請輸入年利率(%):"))
c = int(input("請輸入經過的月份:"))

# 將年利率轉為月利率
b_rate = b / 100 / 12

# total為總金額 初始為本金a
total = a

print("-" * 30)
for i in range(c):
    # 複利計算：利息是基於上個月的總額計算
    total *= (1 + b_rate)
    # 使用 :.2f 格式化輸出到小數點第二位
    print(f'第{i+1} 個月存款總額為: {total:.2f}')

#10. 驗證輸入密碼 允許輸入三次 三次驗證失敗後則退出程式 三次內輸入正確則通過 錯誤則顯示還有幾次機會 三次錯誤則顯示不通過
correct = 1234
max = 3

for i in range(max): #當確定知道要跑幾次迴圈時 適合用for迴圈

    user = int(input(f"請輸入密碼: "))

        # 檢查密碼是否正確
    if user == correct:
            print("密碼正確，驗證通過！")
            break  # 密碼正確，使用 break 立即跳出迴圈
    else:
            # 計算剩餘機會
        teies = max - (i + 1)
        if teies > 0:
            print(f"密碼錯誤，還有 {teies} 次機會。")

# for...else 語法：只有當 for 迴圈是「自然跑完」（沒有被 break 中斷）時，else 區塊才會執行
else:
    print(f"三次機會已用完，驗證失敗。")


#11.使用者會輸入票種張數(生日票220元 全票320元 優待票270元)&人數 重複執行完所有票種後結算訂單再執行下一筆
ticket = {
    "生日票": 220,
    "全票": 320,
    "優待票": 270
    }
totalprice = 0
totaltickets = 0

for ticketname, ticketprice in ticket.items():
    a = int(input(f"請輸入{ticketname}的張數 (價格: {ticketprice}元): "))
        
    # 計算總張數與總金額
    totaltickets += a
    totalprice += a * ticketprice

    # 顯示該筆訂單的結算結果
    print(f"目前買了: {totaltickets} 張")
    print(f"總金額: {totalprice} 元")