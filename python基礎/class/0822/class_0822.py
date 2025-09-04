# 各種變數
#若要整個部分# 可使用快捷鍵ctrl + /

#整數
a = 10
b = 20
c = a + b
print(c)

#浮點數
d = 10.5
e = 20.3
f = d + e
print(f)

#字串
g = "Hello"
h = "World"
i = g + " " + h
print(i)

#布林值
j = True
k = False

print(f'整數相加: {c} 浮點數相加: {f} 字串相加: {i} 布林值: {j}')

#型別轉換
print(7+float('5'))
print(str(7.0)+'5')
print(int(7/3))
print(bool(0))

#使用Type()函式顯示變數型別
print(type(a))
print(type(d))

#變數有大小寫之分
a = 10
A = 20
print(a)		#這邊輸出10
print(A)		#這邊輸出20

#輸入資料
# name = input("請輸入您的名字: ")
# age = input("請輸入您的年齡: ")
# print(f'你好 {name}，你的年齡是 {age} 歲。')

#算數運算子
print(1>2)
print(50+20)
print("50"+"20")
print("50+20")
print(5**3)   #5的3次方
print(7/3)    #浮點數除法
print(7//3)   #整數除法
print(7%3)    #除(取餘數)

#算術指定運算子
x = 10
x += 5   # 等同於 x = x + 5
x *= 2   # 等同於 x = x * 2
x **= 2  # 等同於 x = x ** 2
x //= 3  # 等同於 x = x // 3


import math #要使用到math模組的函式 需要先import math模組
r = float(input("請輸入圓的半徑: "))             #輸入圓的半徑並轉換成浮點數 鍵盤輸入的資料預設是字串
area = math.pi * r**2       #計算圓的面積
perimeter = 2 * math.pi * r #計算圓的周長
print(f'圓的面積為: {area:.2f} \n圓的周長為: {perimeter:.2f}')  #輸出圓的面積，.2f代表並保留兩位小數 /n代表換行
print("圓面積："+ '%.2f'%(area) +"\n周長："+ '%.2f'% perimeter)  #%格式化輸出 意思是將變數的值插入到字串中

#python內建函式
abs(-69)    #絕對值
max(9,6,3)  #最大值
min(2,5,8)  #最小值   
pow(2,5)    #次方
round(3.14159,2) #四捨五入到小數點後2位