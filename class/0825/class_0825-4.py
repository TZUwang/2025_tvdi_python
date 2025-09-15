#if判斷式練習

#1.判斷基數偶數
# a = input("請輸入一個正整數")
# if a % 2 == 0:
#     print("偶數")
# else:
#     print("奇數")

#2.判斷是否為3或5的倍數
# a = int(input("請輸入一個正整數"))
# if a % 3 == 0 and a % 5 == 0:
#     print(f"{a}是3和5的倍數")
# elif a % 3 == 0:
#     print(f"{a}是3的倍數")
# elif a % 5 == 0:
#     print(f"{a}是5的倍數")
# else:
#     print(f"{a}不是3和5的倍數")

#3.輸入年份判斷是否為閏年 (每四年潤一次,但滿百不潤,每四百年還是會潤一次)
# year = int(input("請輸入一個西元年"))
# if year % 400 == 0:
#     print(f"{year}是閏年")
# elif year % 100 == 0:
#     print(f"{year}不是閏年")
# elif year % 4 == 0:
#     print(f"{year}是閏年")
# else:
#     print(f"{year}不是閏年")
#巢狀寫法
# year = int(input("請輸入一個西元年"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year}是閏年")
#         else:
#             print(f"{year}不是閏年)")
#     else:
#         print(f"{year}是閏年")
# else:
#     print(f"{year}不是閏年")

#4.使用者輸入兩個數&一個運算子(+ - * / // %)將整個算式與計算結果列印出來
# a = int(input("請輸入第一個數字:"))
# b = int(input("請輸入第二個數字:"))
# op = input("請輸入運算子(+ - * / // %):")
# if op == "+":
#     print(f"{a}+{b}={a+b}")
# elif op == "-":
#     print(f"{a}-{b}={a-b}")
# elif op == "*":
#     print(f"{a}*{b}={a*b}")
# elif op == "/":
#     print(f"{a}/{b}={a/b}")
# elif op == "//":
#     print(f"{a}//{b}={a//b}")
# elif op == "%":
#     print(f"{a}%{b}={a%b}")
# else:
#     print("輸入錯誤")

#5.使用者輸入一個字元 判斷是英文字母 數字 還是其他符號
# a = input("請輸入一個字元:")
# if a.isalpha(): #isalpha判斷是否為英文字母
#     print(f"{a}為英文字母")
# elif a.isdigit(): #isdigit判斷是否為數字
#     print(f"{a}為數字")
# else:
#     print(f"{a}為其他符號")

#6.根據使用者輸入的分數顯示對應等級
# score = int(input("請輸入分數:"))
# if 100 >= score >= 90:
#     print("你A級")
# elif 90 > score >= 80:
#     print("你B級")
# elif 80 > score >= 70:
#     print("你C級")
# elif 70 > score >= 60:
#     print("你D級")
# else:
#     print("你F級")

#7.使用者輸入一個8000以上的金額,輸出顯示輸入金額與折扣優惠後的金額
# x = int(input("請輸入金額(8000以上):"))
# if x < 8000:
#     print(f"消費金額 {x} 元,你花太少了。")
# else:
#     # 先根據條件計算出折扣後的金額 y
#     if x >= 38000:
#         y = x * 0.7
#     elif x >= 28000:
#         y = x * 0.8
#     elif x >= 18000:
#         y = x * 0.9
#     else: 
#         y = x * 0.95
#     # 最後統一印出結果
#     print(f"你消費的金額為 {x} 元, 折扣後的金額為 {y} 元")

#8.使用者輸入攝氏或華氏溫度,輸出對應轉換的溫度
# x = input("請輸入攝氏或華氏(C/F):")
# y = float(input("請輸入溫度:"))
# if x == "C":
#     z = y * 9 / 5 + 32
#     print(f"攝氏 {y} 度等於華氏 {z} 度")
# elif x == "F":
#     z = (y - 32) * 5 / 9
#     print(f"華氏 {y} 度等於攝氏 {z} 度")
# else:
#     print("輸入錯誤的符號")

#9.使用者輸入三邊的長,檢查是否能成為三角形,可以則輸出三角形的周長,否則顯示"不能成為三角形"
# a = float(input("請輸入第一邊的長度:"))
# b = float(input("請輸入第二邊的長度:"))
# c = float(input("請輸入第三邊的長度:"))
# if a + b > c and a + c > b and b + c > a:
#     print(f'此三角形的周長為{a+b+c}')
# else:
#     print('不能成為三角形')

#10.使用者輸入三個整數,由小排到大輸出
# a = int(input("請輸入第一個整數:"))
# b = int(input("請輸入第二個整數:"))
# c = int(input("請輸入第三個整數:"))

# # 透過三次比較與交換，確保 a <= b <= c
# # 第一次比較：確保 a 比 b 小，若否，則交換
# if a > b:
#     a, b = b, a  

# # 第二次比較：確保 b 比 c 小，若否，則交換
# if b > c:
#     b, c = c, b

# # 第三次比較：經過前兩次交換，c 已經是最大值，但 a 和 b 的順序可能又亂了，所以再檢查一次
# if a > b:
#     a, b = b, a

# print(f"由小到大排序後為: {a}, {b}, {c}")

