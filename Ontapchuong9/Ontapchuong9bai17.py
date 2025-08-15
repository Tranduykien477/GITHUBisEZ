def tinh_nang_1():
    print('1. Cong')
    Phep_cong=input('Nhap hai so ban muon cong, cach nhau boi dau cach: ')
    list=Phep_cong.split(' ')
    a=int(list[0])
    b=int(list[1])
    print(a+b)
def tinh_nang_2():
    print('2. Hieu')
    Phep_tru=input('Nhap hai so ban muon tru, cach nhau boi dau cach: ')
    Phep_tru.split(' ')
    c=int(list[0])
    d=int(list[1])
    print(c-d)
def tinh_nang_3():
    print('3. Nhan')
    Phep_nhan=input('Nhap hai so ban muon nhan, cach nhau boi dau cach: ')
    Phep_nhan.split(' ')
    e=int(list[0])
    f=int(list[1])
    print(e*f)
def tinh_nang_4():
    print('4. Chia')
    Phep_chia=input('Nhap hai so ban muon chia, cach nhau boi dau cach: ')
    Phep_chia.split(' ')
    g=int(list[0])
    h=int(list[1])
    print(g//h)
while True:
    print('Chao mung ban den voi chuong trinh')
    print('1. Cong')
    print('2. Tru')
    print('3. Nhan')
    print('4. Chia')
    Tinhnangduocchon=input("Chon mot so tu 1 toi 4: ")
    if Tinhnangduocchon=="1":
        tinh_nang_1()
    if Tinhnangduocchon=="2":
        tinh_nang_2()
    if Tinhnangduocchon=="3":
        tinh_nang_3()
    if Tinhnangduocchon=='4':
        tinh_nang_4()