'''
撲克牌
共有四種花色
比大小時依序為：
spade 黑桃 / heart 紅心 / diamond 方塊 / club 梅花

一種花色有 13 張數字
1 點為 A / Jack J（騎士，11 點）/ Queen Q（皇后，12點）/ King K（國王，13 點）
'''

import random

def transform(num):
    if num == 1:
        return 'A'
    elif num == 11:
        return 'J'
    elif num == 12:
        return 'Q'
    elif num == 13:
        return 'K'
    else:
        return num

    
#先做電腦的抽卡    
#花色
suits = ['♣','♦','♥','♠'] 

a=random.choice(suits) #隨機取得撲克牌花色
b=random.randint(1,13) #隨機取得撲克牌數字

#玩家抽卡
x = input('請按1抽一張卡:')
if x == '1':
    c=random.choice(suits)
    d=random.randint(1,13)

    # 將數字轉換為 A, J, Q, K 以便顯示，但保留原始數字 b, d 用於比較
    trans_b = transform(b)
    trans_d = transform(d)
    
    # 先印出雙方抽到的牌
    print(f'你抽到的卡為 {c}{trans_d}, 電腦抽到的卡為 {a}{trans_b}')

    # 比較數字大小；如果數字相同，再比較花色的索引值
    # 電腦的牌 (a, b), 玩家的牌 (c, d)
    if b > d or (b == d and suits.index(a) > suits.index(c)):
        print('電腦獲勝')
    else:
        print('玩家獲勝')
else:
    print('結束')

'''題目2.請將A改為最大牌'''
'''題目3.將範例改為只有一副牌(也就是不可能出現同花色同數字)'''

'''
練習題2
某大學系入學考採計國英數三科，輸入考生各科成績，並進行計算個人總分及平均，並且計算每個人的各科平均值。連續輸入，直到姓名處不輸入，直接按 enter 跳出結束
'''
