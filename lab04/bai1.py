n=int(input('Nhap so nguyen duong n: '))
if n<=0:
    print('Nhap sai vui long nhap lai!')
else:
    s4=0
    i=1
    while i<=n:
        s4+=i**2
        i+=1
    s5=0
    i=1
    while i<=(2*n+1):
        if i%2==1:
            s5+=i**3
        i+=1
    s6=0
    i=2
    while i<=(2*n):
        if i%2==0:
            s6+=i**4
        i+=2
    print(f"s4 = {s4}")
    print(f"s5 = {s5}")
    print(f"s6 = {s6}")
