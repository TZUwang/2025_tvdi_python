#使用者輸入帳號密碼 累積錯3次則退出 
account = 'abc123'
password = '123456'
count = 0
while count < 3:
    input_account = input('請輸入帳號:\n')
    input_password = input('請輸入密碼:\n')
    if input_account == account and input_password == password:
        print('登入成功')
        break
    else:
        count += 1
        print(f'帳號或密碼錯誤 你還有 {3 - count} 次機會')
else:
    print('帳號已被鎖定')