listnum=[0,1,2,3,4,5,6,7,8,9,10]
target=7
found=False
print('Tim kiem so 7:')
for num in listnum:
    if num == 7:
        print(f"Da tim thay so {target} lol")
        found=True
        break
    if num != 7:
        print(f'Dang kiem tra so: {num}')
if not found:
    print(f'Khong tim thay so {target}')