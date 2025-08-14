
# for i in range(0,100,1):
#     for j in range(0,100,1):
#         if i == j*j:
#             print(i)

# for i in range(0,100,1):
#     a=i*i
#     if a < 100:
#         print(a)

from math import *
ran_num=int(input('Vui long nhap mot so bat ki: '))
So_can_check=sqrt(ran_num)
if So_can_check == int(So_can_check):
    print('Day la mot so chinh phuong !!!')
else:
    print('Day khong phai la mot so chinh phuong :(')



            