a=int(input('Nhap mot so bat ki: '))
b=int(input('Nhap mot so bat ki: '))
def UCLN():
    list_a=[]
    list_b=[]
    list_common=[]
    for i in range(1,a):
        if a % i == 0:
            list_a.append(i)
    print(list_a)

    for j in range(1,b):
        if b % j == 0:
            list_b.append(j)
    print(list_b)

    for k in list_b:
        if k in list_a:
            list_common.append(k)
        
    print(max(list_common))
    
    

