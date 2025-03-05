n=int(input('Nhap so nguyen duong n: '))
print(f"Phan tich thua so nguyen to {n}: ",end="")
for i in range(2,n+1):
    if n%i==0:
        print(i,end=" ")
        n//=i