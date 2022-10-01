#輸入
price = input('單價:')
amount = input('數量:')

#轉型
price = int(price)
amount = int(amount)

#計算
total = price*amount

#判斷
if total>= 2000 :
    total = total*0.9
else:
     total = total*0.95
        

#顯示
print(f'{total:,.0f}元')