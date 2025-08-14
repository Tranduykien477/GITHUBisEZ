print('Cac so khong chia het cho 3 la: ')
for i in range(1,16):
    if i % 3 == 0:
        continue
    if i % 3 != 0:
        print(i)