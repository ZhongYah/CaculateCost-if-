#輸入
price = input('單價:')
amount = input('數量:')

#轉型
price = int(price)
amount = int(amount)

#計算
total = price*amount

#顯示
print(f'{total:,}元')