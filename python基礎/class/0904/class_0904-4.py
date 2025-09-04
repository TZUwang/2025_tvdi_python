#9.	使用函數撰寫骰子比大小程式，先由電腦模擬投擲三個骰子和，再由使用者輸入一個值(自訂)模擬投擲動作，透過亂數產生三個骰子和，並和電腦輸出結果比大小，印出"你贏了"或"你輸了"

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



