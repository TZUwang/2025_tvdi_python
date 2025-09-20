#1.建立一個函式compute()，讓使用者輸入學號、姓名、科系，透過呼叫顯示這些訊息
def compute():
    id = input('請輸入學號:\n')
    name = input('請輸入姓名:\n')
    department = input('請輸入科系:\n')
    print(f'你的學號: {id} 姓名: {name} 科系: {department}')

def main():
    print('請輸入學號、姓名、科系')
    compute()

main()

#2.建立一個函式compute(x,y)。讓使用者輸入2個數字做為參數，透過呼叫函式，回傳(return x*y)的乘積
def compute(x,y):
    return x*y

def main():
    a = int(input('請輸入第一個數字:\n'))
    b = int(input('請輸入第二個數字:\n'))
    print(f'{a}和{b}乘積為: {compute(a,b)}')

main()

#3.讓使用者輸入2個整數，呼叫函式compute(x,y) 並傳送2個參數給函數，讓函數回傳從x到y連續加總的結果
def compute(x,y):
    total = 0
    for i in range(x,y+1):
        total += i
    return total

def main():
    a = int(input('請輸入第一個數:\n'))
    b = int(input('請輸入第二個數:\n'))
    sol = compute(a,b)
    print(f'從 {a} 到 {b} 的連續加總為: {sol}')

main()

#4.讓使用者輸入2個整數，呼叫函式compute(x,y) 並傳送2個參數給函數，讓函數回傳x^y的值
def compute(x,y):
    return x**y

def main():
    x = int(input('請輸入x值:\n'))
    y = int(input('請輸入y值:\n'))
    print(f'{x}的{y}次方 = {compute(x,y)}')

main()

#5.建立一個函式compute(a,x,y) 使用者輸入3個參數：a (字元)、x(個數)、y(列數)，印出 y列 x個的a字元
def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print(a, end='')
        print()
    


def main():
    q = input('請輸入字元:\n')
    w = int(input('請輸入個數:\n'))
    e = int(input('請輸入列數:\n'))
    compute(q, w, e)

main()

#6.撰寫圓面積、長方形面積、三角形面積函式，透過輸入圓形半徑、長方形長、寬，三角形底和高，計算並輸出三個圖形面積與三個面積和
def circle_area(a):
    import math
    b = math.pi * a**2
    return b

def rectangle_area(a,b):
    c = a * b
    return c

def triangle_area(a,b):
    c = a * b / 2
    return c

def main():
    a = float(input('請輸入圓形半徑:\n'))
    b = float(input('請輸入長方形長:\n'))
    c = float(input('請輸入長方形寬:\n'))
    d = float(input('請輸入三角形底:\n'))
    e = float(input('請輸入三角形高:\n'))
    print(f'圓形面積為: {circle_area(a)} 長方形面積為: {rectangle_area(b,c)} 三角形面積為: {triangle_area(d,e)} 三個面積和為: {circle_area(a)+rectangle_area(b,c)+triangle_area(d,e)}')

main()

#7.輸入2個正整數x,y，傳入最大公因數函式內，函式回傳最大公因數計算結果
def GreatestCommonDivisor(x ,y):
    if y > x:
        x,y = y,x
    for i in range(x,0,-1):
        if x % i == 0 and y % i == 0:
            return i

def main():
    x = int(input('請輸入第一個數字:\n'))
    y = int(input('請輸入第二個數字:\n'))
    print(f'{x}與{y}的最大公因數為: {GreatestCommonDivisor(x,y)}')

main()

'''
8.某市區停車場車位不足，為鼓勵車輛提早移出，進行如下規範：  
(a). 2小時以內(含2小時)，每小時以30元計算  
(b). 2小時以上到4小時(含4小時)，每小時以50元計算  
(c). 4小時以上到6小時(含6小時)，每小時以80元計算  
(d). 6小時以上，每小時以100元計算  
請撰寫程式輸入停車時數，傳入函數參數內，函數傳回停車費計算結果
'''
def parkfee(hours):
    if hours <= 2:
        money = hours * 30
    elif hours <= 4:
        money = 2 * 30 + (hours - 2) * 50
    elif hours <= 6:
        money = 2 * 30 + 2 * 50 + (hours - 4) * 80
    else:
        money = 2 * 30 + 2 * 50 + 2 * 80 + (hours - 6) * 100
    return money

def main():
    time = int(input('請輸入停車時數:\n'))
    money = parkfee(time)
    print(f'你停了{time}小時 停車費為: {money} 元')

main()

#9.使用函數撰寫骰子比大小程式，先由電腦模擬投擲三個骰子和，再由使用者輸入一個值(自訂)模擬投擲動作，透過亂數產生三個骰子和，並和電腦輸出結果比大小，印出"你贏了"或"你輸了"
import random
def dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    sum = dice1 + dice2 + dice3
    return dice1, dice2, dice3, sum

def main():
    import random
    a = int(input(f'請按1進行投擲骰子'))
    if a == 1:
        Userdice1 = random.randint(1, 6)
        Userdice2 = random.randint(1, 6)
        Userdice3 = random.randint(1, 6)
        Usersum = Userdice1 + Userdice2 + Userdice3
    
        a ,b ,c ,d = dice()
        if d > Usersum:
            print(f'你的點數是{Userdice1},{Userdice2},{Userdice3}總和是{Usersum} 電腦的點數是{a},{b},{c}總和是{d}')
            print('\n你輸慘了')
        elif d < Usersum:
            print(f'你的點數是{Userdice1},{Userdice2},{Userdice3}總和是{Usersum} 電腦的點數是{a},{b},{c}總和是{d}')
            print('\n你贏麻了')
        else:
            print('平手')
    else:
        print('不玩就滾')

main()