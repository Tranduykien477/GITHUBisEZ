So_dung=69
while True:
    So_nhap=int(input("Du doan so bat ki tu 1 den 100: "))
    if So_nhap==So_dung:
        print('Chuc mung ban da doan dung so.')
        break
    elif So_nhap<So_dung:
        print('So nay khong dung. Vui long thu lai mot so lon hon')
    else:
        print("So nay khong dung. Vui long thu lai mot so be hon")