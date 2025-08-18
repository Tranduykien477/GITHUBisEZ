n=int(input('Nhap so thu n trong day Fibonacci: '))
x=0
y=1
total=2
while True:
    z=x+y
    total+=1
    if total == n:
        print(z)
        break       
    x=y
    y=z
 
    


