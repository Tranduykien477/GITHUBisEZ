def phan_loai_diem(score):
    print("Kiem tra trinh do hoc tap cua hoc sinh: ")
    if score >= 8:
        print("Gioi")
    elif score >= 6.5:
        print("Kha")
    elif score >= 5:
        print("Trung binh")
    else:
        print('Yeu')
phan_loai_diem(9)