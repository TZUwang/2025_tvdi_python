#1.2.6	使用者輸入十個數字，做為樣本數，輸出眾數(出現最多次數的數字
a = [int(input(f'請輸入{i+1}個數字'))for i in range(10)]

max = 0
for num in a:
    count = a.count(num)
    if count > max:
        max = count

ans = []
for num in a:
    count = a.count(num)
    if count == max and num not in ans:
        ans.append(num)
print(f'眾數為{ans} 出現了{max}次')
