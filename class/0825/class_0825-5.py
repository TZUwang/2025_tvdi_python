#練習1
#有一矩形 中心點座標為(0,0) 此矩形x軸長度為8 y軸長度為6 使用者輸入一個座標確認是否在矩形裡面
x1 = float(input("請輸入x座標"))
y1 = float(input("請輸入y座標")) #或是合併為 x1,y1 = eval(input("請輸入一個座標(x,y)"))
if abs(x1) <= 4 and abs(y1) <= 3:
    print("在矩形內")
else:
    print("在矩形外")

#練習2
#生日優惠票220 全票310 優待票270 選擇票券的種類以及張數計算價格
# a = 220
# b = 310
# c = 270
# x = input('選擇票種(a.生日票,b.全票,c.優待票):')
# y = int(input('張數:'))
# if x == 'a':
#     print(f'{y}張生日票需要{a*y}元')
# elif x == 'b':
#     print(f'{y}張全票需要{b*y}元')
# elif x == 'c':
#     print(f'{y}張優待票需要{c*y}元')
# else:
#     print('輸入錯誤的票種')

