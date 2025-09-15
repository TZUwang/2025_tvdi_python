#邏輯運算子 and or not

#and判斷介於85-95之間的數字
num = int(input("請輸入一個數字:"))
if num >= 85 and num <= 95:
    print("在範圍內")
else:
    print("不再範圍內")

#or與and混合使用 先and後or
#檢查是否為英文字元
ch = input("請輸入一個英文字母:")
if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
    print("是英文字母")
else:
    print("不是英文字母")

#檢查是否為大寫的英文字母
ch = input("請輸入一個英文字母:")
if ch >= 'A' :
    if ch <= 'Z': #可將條件與上一行合併成 if ch >= 'A' and ch <= 'Z' 就不需要多一層if條件
        print("是英文大寫字母")
    else:
        print("不是大寫字母")
else:
    print("不是大寫字母")