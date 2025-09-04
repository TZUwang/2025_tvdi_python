import random                 #載入random模組

# r = random.choice([5,8,7,4,66,33,99,45])
# print(r)         #從串列中隨機產生1個數字
# r = random.choices([5,8,7,4,66,33,99,45],k=4)
# print(r)         #從串列中隨機產生指定個數數字(會重複)
# r = random.sample([5,8,7,4,66,33,99,45],k=4)
# print(r)         #從串列中隨機產生指定個數數字(不重複)

#定數迴圈與不定數迴圈
#定數迴圈-for 迴圈 :確定要重複的具體次數
#不定數迴圈-while 迴圈 :不確定重複次數，但知道停止條件	
#定數迴圈範例
line = 1 #起始為第一行
while line <11: #當跑到第11行之前都會運行迴圈
    for i in range(1 ,7): #每一行都知道要跑6個數字
        num = random.randint(1 , 49) #利用函式隨機生成(範圍1-49)的亂數
        print(f'{num:3}',end=' ') #num變數以至少3個字元的寬度印出
    print() #for 迴圈跑完一輪 (印完 6 個數字) 後執行print()來進行換行
    line += 1 #計數器 line 的值加 1 while 迴圈能夠結束的關鍵，避免無限迴圈
print(f'結束') #迴圈結束，最後印出 '結束'