#輸入
from re import A


drink = input('飲料:')
cups = input('杯數:')

#轉型
cups = int(cups)
# amount = int(amount)

#計算/判斷
if drink == "A":
    total = 50*cups

if drink == "B":
    total = 40*cups

if drink == "C":
    total = 30*cups        

#顯示
print(f'{total:,}元')