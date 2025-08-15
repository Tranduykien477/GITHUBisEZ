def nhap_ten_va_mat_khau(c,d):
    while True:
        a=input('Nhap ten: ')
        b=input('Nhap mat khau: ')
        if c==a and b==d:
            print("Dang nhap thanh cong")
            break
        else: 
            print('Sai mat khau')
nhap_ten_va_mat_khau('admin','123456')
