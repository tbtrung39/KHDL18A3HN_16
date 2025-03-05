n =int(input("nhap mot so nguyen n: "))
for i in range(2,n):
    tong=int(0)
    for u in range(1,i):
        if i%u==0:
            tong+=u
    if tong==i:
        print(f"cac so hoan hao nho hon {n} la: {i}")