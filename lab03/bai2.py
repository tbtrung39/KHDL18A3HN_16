n=int(input('Nhap mot so nguyen n: '))
for i in range(2,n):
    tong=int(0)
    for j in range(1,i):
        if i%j==0:
            tong+=j
    if tong==i:
        print(f"Cac so hoan hao nho hon {n} la: {i}")