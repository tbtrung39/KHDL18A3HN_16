n=int(input('Nhap n: '))
tong=1
tich=1
for i in range(1,n+1):
    phan_so=(2*(i+1))/(2*i+3)
    tich*=phan_so
    tong+=tich
print("%0.3f"%tong)