#輸入
seat = input('座位區:')
number = input('人數:')

#轉型
number = int(number)

#計算/判斷
if seat == "A":
    total = 500*number  

if seat == "B":
    total = 450*number

if seat == "C":
    total = 380*number 

if seat == "D":
    total = 310*number

if seat == "E":
    total = 250*number    

#顯示
print(f'{total:,}元')