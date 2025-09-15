#基礎迴圈概念

# i = 0 
# x = 0
# while i < 100 :
#     x += i
#     i += 1
#     print('i = ',i,'x = ',x) 

#     i += 1
#     x += i
#     print('i = ',i,'x = ',x)

#先後順序的不同影響很大 迴圈要注意

total = 0       
i = 1           
while i < 101: # 迴圈的條件：當 i 小於 101 時，就重複執行以下的程式碼
    total += i  # total = total + i 將目前的 i 值，累加到 total 變數中
    i += 1      # 將 i 的值加 1，以便下一輪計算下一個數字，並確保迴圈最終會停止
print('i =', i, 'total =', total)    # 當迴圈結束後 (i 變成 101 > 100 跳出迴圈)，印出 total 的最終結果

