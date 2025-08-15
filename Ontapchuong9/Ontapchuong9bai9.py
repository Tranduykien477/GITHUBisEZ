while True:
    ran_num=int(input('Nhap mot so nguyen trong khoang tu 1 den 10: '))
    if ran_num not in range(1,11):
        new_num=int(input('Vui long nhap lai'))
    else:
        print('Cam on ban da nhap dung')
        break
            