# list_num=[10,20,30,40,50]
# total=0
# for i in list_num:
#     total=total + i
# print(f"Tong tat ca cac so la {total}")

# random_num=input('Nhap nhieu so bat ki, cach nhau boi dau cach: ')
# Cac_so=random_num.split(" ")
# total=0
# for i in Cac_so:
#     total = total + int(i)
# print(f'Tong cac so la {total}')

print("Khi khong muon nhap nua, nhap E")
total=0
while True:
    ran_num=input('Hay nhap nhieu so bat ki, cach nhau boi dau cach: ')
    if ran_num == "E":
        break
    Cacso=ran_num.split(' ')
    for i in Cacso:
        total=total+int(i)
print(f'Tong cac so la {total}')
    
   




