# from math import *
# total=0
# scores=[85,90,78,92,88]
# for i in scores:
#     print(i)
#     total=total+i
# average=total/len(scores)
# print(f'Diem trung binh la {average}')

print('Khi muon dung lai, nhap e')
total=0
Socacso=0
while True:
    ran_numbers=input('Nhap nhieu so bat ki, cach nhau boi dau cach: ')
    if ran_numbers == 'e':
        break
    Cacso=ran_numbers.split(' ')
    for i in Cacso:
        total=total+int(i)
    Socacso+=len(Cacso)
    average=total/Socacso
    print(f'Trung binh cua cac so la {average}')