#輸入
# price = input('單價:')
amount = input('數量:')

#轉型
# price = int(price)
amount = int(amount)

#計算
total = 55*amount

#判斷
if amount>= 4 :
    total = total
else:
     total = total+60
        

#顯示
print(f'{total:,.0f}元')