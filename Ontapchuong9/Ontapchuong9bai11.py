while True: 
    try:
        random_number=int(input("Hay nhap mot so chan: "))
        if random_number % 2 == 1:
            print("Day la so le. Yeu cau nhap lai")
        else:
            break
    except:
        print("Day khong phai la mot so. Vui long nhap lai")
        