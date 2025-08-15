name=input("Nhap ten cua ban: ")
new_list=[]
for i in name:
    if i not in new_list:
        new_list.append(i)
# print(new_list)
# for j in new_list:
        Dem_ki_tu=name.count(i)
        print(f"Ki tu {i} xuat hien {Dem_ki_tu} lan ")


