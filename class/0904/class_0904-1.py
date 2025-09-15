#1.猜大小 使用者輸入點數後選擇比大小或猜點數 2.選擇比7大則進行押注贏的話獲得2倍點數 選擇猜點數後進行押注贏的話獲得10倍點數 3.輸出點數算輸贏 4.繼續下一輪直到退出 

import random

point = 1000
print('賭博開始 你有 1000 點')
while True:
    bet = int(input('請輸入你要押注的點數:\n'))
    if point <= 0:
        print('點數不足，遊戲結束')
        break
    choice=int(input('請選擇: 1.比大小 2.猜點數 3.退出遊戲\n'))
    if choice == 1:
        choice2 = int(input('請選擇: 1.比7大 2.比7小\n'))
        dice = random.randint(1, 13)
        print(f'骰子點數為: {dice}')
        if (choice2 == 1 and dice > 7) or (choice2 == 2 and dice < 7):
            point = point - bet + bet * 2
            print(f'你贏了 你現在有 {point} 點')
        elif dice == 7:
            point = point
            print(f'平手 你現在有 {point} 點')
        else:
            point -= bet
            print(f'你輸了 你現在有 {point} 點')
    elif choice == 2:
        guess = int(input('請猜點數(1-13):\n'))
        dice = random.randint(1, 13)
        print(f'骰子點數為: {dice}')
        if guess == dice:
            point = point - bet + bet * 10
            print(f'你贏了 你現在有 {point} 點')
        else:
            point -= bet
            print(f'你輸了 你現在有 {point} 點')
    elif choice == 3:
        print('遊戲結束')
        break
    else:
        print('無效選擇 請重新輸入')
        continue
    