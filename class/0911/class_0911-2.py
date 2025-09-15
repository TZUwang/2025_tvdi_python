'''
容器

串列List  [ ]
元組tuple ( )
集合set   { }
字典dic   {a:b,c:d}
字串str   " "

'''
#1.元組  (tuple)

#元組 是以小括號建立，元素間用逗號隔開
tuple0 = (1 ,2 ,3 ,4 ,5)
print(tuple0)
#若括號內為空元素則為空元組
tuple2 = ()
print(tuple2)
#從串列中建立元組
tuple3 = tuple([i for i in range(1,10)])
print(tuple3)
#字串也可以建立元組 有無加上tuple差很多
tuple4 = ('python')
print(tuple4)
tuple5 = tuple('python')
print(tuple5)
#元組函式 可以用 len、max 、min、sum等串列使用的函式，以及in、not in、*、+ 運算子，這些功能和串列相似
a = len(tuple0)
print(a)
b = max(tuple0)
print(b)
c = min(tuple0)
print(c)
d = sum(tuple0)
print(d)
#元組 內的元素不能被刪除，但可以增加，增加方式使用 += 運算符號，要加入的元素放在小括號之中
tuple0 += (6,)  #增加一個元素時後面加逗號 增加一個以上的元素時就可以不用再最後+逗號
print(tuple0)
tuple0 += (7,8)
print(tuple0)
#可以使用索引值來取得所在位置的元素內容
a = tuple0[2]
print(a)
b = tuple0[-1]
print(b)
c = tuple0[2:5]
print(c)
tuple0 = 2 * tuple3
print(tuple0)
#使用迴圈印出元組 中的所有資料
for i in tuple0:
    print(i,end=' ')
'''
元組沒有刪除個別元素的方式 但可以刪除整組元組
del tuple0
print(tuple0)
'''
