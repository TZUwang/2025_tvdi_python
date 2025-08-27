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