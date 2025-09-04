#迴圈練習題
#10. 驗證輸入密碼 允許輸入三次 三次驗證失敗後則退出程式 三次內輸入正確則通過 錯誤則顯示還有幾次機會 三次錯誤則顯示不通過
# correct = 1234
# max = 3

# for i in range(max): #當確定知道要跑幾次迴圈時 適合用for迴圈
#     # try:
#         # 讓使用者輸入密碼，並轉成整數
#         user = int(input(f"請輸入密碼: "))

#         # 檢查密碼是否正確
#         if user == correct:
#             print("密碼正確，驗證通過！")
#             break  # 密碼正確，使用 break 立即跳出迴圈
#         else:
#             # 計算剩餘機會
#             teies = max - (i + 1)
#             if teies > 0:
#                 print(f"密碼錯誤，還有 {teies} 次機會。")

#     # except ValueError:
#     #     # 如果使用者輸入的不是數字，會觸發這個錯誤
#     #     teies = max - (i + 1)
#     #     if teies > 0:
#     #         print(f"輸入無效，請輸入數字。您還有 {teies} 次機會。")

# # for...else 語法：只有當 for 迴圈是「自然跑完」（沒有被 break 中斷）時，else 區塊才會執行
# else:
#     print(f"三次機會已用完，驗證失敗。")


#11.使用者會輸入票種張數(生日票220元 全票320元 優待票270元)&人數 重複執行完所有票種後結算訂單再執行下一筆
# ticket = {
#     "生日票": 220,
#     "全票": 320,
#     "優待票": 270
#     }
# totalprice = 0
# totaltickets = 0

# for ticketname, ticketprice in ticket.items():
#     a = int(input(f"請輸入{ticketname}的張數 (價格: {ticketprice}元): "))
        
#     # 計算總張數與總金額
#     totaltickets += a
#     totalprice += a * ticketprice

#     # 顯示該筆訂單的結算結果
#     print(f"目前買了: {totaltickets} 張")
#     print(f"總金額: {totalprice} 元")

#===================================================

space = " "
while space != "done": #while 迴圈 只要使用者沒有輸入 "done"，這個迴圈就會一直重複執行

    totalprice = 0
    totaltickets = 0
    ticket = {
        "生日票": 220,
        "全票": 320,
        "優待票": 270
        }
    while True: #無限迴圈 (while True) 會不斷執行 直到遇到 break 指令為止
        a = input("請輸入您要購買的票種名稱 (或輸入結算完成訂單): ")
        if a == "結算":
            break
        # 如果使用者不是輸入 "結算"，程式會繼續執行這裡
        b = int(input(f"請輸入 '{a}' 的張數: "))
        totalprice += ticket[a] * b
        totaltickets += b
        
        print(f"加入 {b} 張 {a}。目前訂單金額: {totalprice} 元")

    # 結算訂單
    print("========== 訂單結算 ==========")
    print(f"總張數: {totaltickets} 張")
    print(f"總金額: {totalprice} 元")
    print("============================")

    #使用者輸入"done"，這個值就會被存到 space 變數中 最外層的 while 迴圈條件 (space != "done") 會變成 False，迴圈結束
    space = input("輸入done結束程式，或按Enter開始下一筆新訂單: ")