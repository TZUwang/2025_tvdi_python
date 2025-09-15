#亂數產生器
import random #載入random模組 #若後續很常用到名稱又很長時 可使用import random as rnd 後續使用就可以改為EX:r = rnd.random()

# random.seed() #若()內設定數字 無論隨機幾次都會產生固定結果 將()內數字儲存固定亂數

# r = random.random()  #隨機產生0-1(不含1)的浮點數
# print(r)
# r = random.uniform(1, 50)     #隨機產生1-50的浮點數
# print(r)
# r = random.randint(1,50)      #隨機產生1-50的整數
# print(r)
# r = random.randrange(1,50,2)  #隨機產生1-49的整數(奇數)
# print(r)
# r = random.randrange(0,50,2)  #隨機產生1-49的整數(偶數)

#若只使用到特定其中一個函式(random.randint) 可以指呼叫特定不占用記憶體 EX: from random import randint

eve = 0
odd = 0
for i in range(100):
    r = random.randint(1,100)  # 利用random.randint函式隨機產生一個 1 到 100 之間的整數，並存到變數 r
    print(r,end=" ")           # end=" "以空格結尾，讓下一個數字接在後面，而不是換行
    if r % 2 == 0:             # 判斷 r 是否為偶數 (如果 r 除以 2 的餘數等於 0)
        eve += 1               # 如果是偶數，偶數計數器 eve 就加 1
    else:                      # 如果不是 奇數計數器 odd 就加 1
        odd += 1
print(f'\n偶數有{eve}個,奇數有{odd}個') #(\n)換行 讓結果好閱讀

