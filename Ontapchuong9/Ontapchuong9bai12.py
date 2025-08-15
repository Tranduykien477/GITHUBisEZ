integer=int(input('Nhap mot so nguyen bat ki: '))
check=0
for number in range(2,integer): 
    if integer % number == 0:
        check = check + 1
if check == 0:      
        print('So do la so nguyen to')
else: 
        print('So do la hop so')
