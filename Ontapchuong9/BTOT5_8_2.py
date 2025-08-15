Ran_num=int(input('Nhap mot so bat ki: '))
total = 1
for i in range(1,Ran_num):
    if Ran_num % i == 0:
        total = total + i
if total == Ran_num:
    print("So do la so hoan hao")
else:
    print('So do khong la so hoan hao')
