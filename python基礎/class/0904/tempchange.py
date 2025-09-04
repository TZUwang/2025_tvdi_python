#函式(Function)的使用

# #未使用函式
# for i in range (20):
#     print('*',end='')
# print()

# for i in range (30):
#     print('*',end='')
# print()

# for i in range (40):
#     print('*',end='')
# print()

# #使用函式
# def starPrint(a):
#     for i in range (a):
#         print('*',end='')
#     print()

# starPrint(20)
# starPrint(30)
# starPrint(40)

# #函式裡面還可以呼叫函式 執行完在執行下一個函式或其他工作
# def starPrint2(a):
#     for i in range (a):
#         print('*',end='')
#     print()

# def boxPrint(a,b):
#     starPrint2(a) #長方形上邊框
#     for i in range (b-2): #長方形中間部分
#         print('*',end='') #長方形的「左邊框」
#         for j in range (a-2):
#             print(' ',end='') #中間部分
#         print('*')  #長方形的「右邊框」
#     starPrint2(a) #長方形下邊框


# boxPrint(20,5)
# boxPrint(30,10)

#透過函式 將華氏轉攝氏/攝氏轉華氏 寫成兩個函式
def FtoC():
    F = float(input('請輸入華氏溫度:\n'))
    C = (F-32)*5/9
    print(f'攝氏溫度為: {C}',end='')
    if C < 10:
        print('好冷')
    elif C < 30:
        print('正常')
    else:
        print('好熱')

def CtoF():
    C = float(input('請輸入攝氏溫度:\n'))
    F = C*9/5+32
    print(f'華氏溫度為: {F}',end='')
    if F < 32:
        print('好冷')
    elif F < 86:
        print('正常')
    else:
        print('好熱')

def main():
    a = int(input('請選擇溫度轉換方式: 1.華氏轉攝氏 2.攝氏轉華氏\n'))
    if a == 1:
        FtoC()
    elif a == 2:
        CtoF()
    else:
        print('無效選擇')



