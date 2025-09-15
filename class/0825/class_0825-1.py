#數字判斷

a = int(input("你的成績為:"))
if 100 >= a >= 0:
    if a >= 60:
        print("成績及格" ,end=" ")

        if a >= 90:
            print("表現優異")
    else:
        print("成績不及格")

else:
    print("成績不在範圍內")
print("判斷結束")