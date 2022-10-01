#輸入
gram = input('公克數:')

#轉型
gram = int(gram)

#判斷/計算
if gram >= 200 :
    total = int(0.65*gram*0.9)
else:
    total = int(0.65*gram)

#顯示
print(f'{total:,}元')