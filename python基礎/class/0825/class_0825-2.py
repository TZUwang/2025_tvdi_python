#條件式巢狀結構

a = int(input("請輸入你的成績:"))
if 100 >= a >= 0:
    if a >= 60:
        print("成績及格" ,end=" ")
        if 80 > a >= 70:
            print("表現尚可")
        elif 90 > a >= 80:
            print("表現良好")
        elif  a >= 90:
            print("表現優異")
        else:
            print("別高興太早")
    else:
        print("爛成績", end=" ")
        if 50 <= a < 60:
            print("去重修")
        else:
            print("請休學")
else:
    print("成績不在範圍內")
print("判斷結束")

#數字以外 文字也可以
# a = input("請輸入蘋果的英文：")
# if a == "apple":
#     print("符合")
# else:
#     print("不符合")
# print("判斷結束")

#判斷一元二次方程式的根的情況
a,b,c = eval(input("請輸入a,b,c三個數字(使用,隔開):"))
d = b**2 - 4*a*c
if d > 0:
    print("有兩個不相等的實根")
elif d == 0:
    print("方程式有一解")
else:
    print("方程式無解")
print("判斷結束")

#BMI量測表
height = float(input("請輸入你的身高(cm)"))
weight = float(input("請輸入你的體重(kg)"))

bmi = weight / (height/100)**2
print("你的BMI值為%.2f"%bmi)

if bmi < 18.5:
    weight1 = ((height/100)**2) * 18.5
    w = weight1 - weight
    print(f"你的體重過輕,請你增重{w:.2f}公斤")
elif 25.0 > bmi >= 18.5:
    print("體重正常,你很健康")
elif bmi < 30.0:
    weight2 = ((height/100)**2) * 24.9
    w = weight - weight2
    print(f"體重過重,請你減重{w:.2f}公斤")
else:
    weight2 = ((height/100)**2) * 24.9
    w = weight - weight2
    print(f"你的體重已達肥胖標準,建議至少減重{w:.2f}公斤才能達到正常體重範圍")
