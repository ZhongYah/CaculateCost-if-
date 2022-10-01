#輸入
# price = input('單價:')
kilometers = input('公里數:')

#轉型
# price = int(price)
kilometers = float(kilometers)

#判斷
if kilometers >= 10 :
    total = int(48.5*kilometers) 
else:
    total = int(55.7*kilometers) 
                

#顯示
print(f'{total:,}元')