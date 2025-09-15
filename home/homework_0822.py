import math

x = 123
y = 123456
z = 12
p = 12
q = 123
r = 123456

#1.列印練習
#print(x, y, z)
#print(p, q, r)
#將結果排版成為 8位數向右靠齊 Print('格式化參數' %(變數名稱))
print("%8d %8d %8d" % (x, y, z))
print("%8d %8d %8d" % (p, q, r))

#2.單位轉換
#公斤轉換成磅數
kg = int(input("請輸入公斤數:"))
lb = kg * 2.20462
print(f'轉換結果為{lb:.2f}磅') #取小數點後兩位

#3.平均值計算
a = int(input("請輸入第1筆資料:"))
b = int(input("請輸入第2筆資料:"))
c = int(input("請輸入第3筆資料:"))
avg = (a + b + c) / 3
print(f'平均值為{avg:.2f}')

#4.兩點距離計算
x1 = int(input("請輸入第一組X座標:"))
y1 = int(input("請輸入第一組Y座標:"))
x2 = int(input("請輸入第二組X座標:"))
y2 = int(input("請輸入第二組Y座標:"))
distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) #math.sqrt是開根號
print(f'兩者之間的距離為{distance}')

#5.存錢筒
name = input("請輸入你的姓名:")
#於畫面顯示要求輸入銅板個數，並依序要求輸入1元、5元、10元、50元硬幣數量。
money1 = int(input("請輸入1元硬幣個數:"))
money5 = int(input("請輸入5元硬幣個數:"))
money10 = int(input("請輸入10元硬幣個數:"))
money50 = int(input("請輸入50元硬幣個數:"))
total = money1 * 1 + money5 * 5 + money10 * 10 + money50 * 50
print(f'{name},你總共有{total}元')

#6.數學函數
x = float(input("請輸入一個數:"))
y = 3 * (x**3) + (2 * x) - 1
print(f'值為{y}')

#7.圖形面積
#三角形的底=10，高=5 ， 長方形的長=5，寬=10 ， 圓的半徑=5
trangle = 10 * 5 / 2
rectangle = 5 * 10
circle = math.pi * 5**2 
figure = trangle + rectangle + circle
print(f'圖形面積為{figure}')

#8.溫度轉換
k = float(input('請輸入華氏溫度:'))
c = (k - 32) * 5 / 9
print(f'換算攝氏溫度為{c}度')

#9.BMI計算
cm = float(input("請輸入身高(公分):"))
kg = float(input("請輸入體重(公斤):"))
m = cm / 100
bmi = kg / (m**2)
print(f'BMI為{bmi}')