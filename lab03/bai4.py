n = int(input("Nhập số nguyên từ bàn phím : "))
print("Các số nguyên tố bé hơn hoặc bằng",n)
for a in range(2,n+1):
    so_nguyen_to=True
    for i in range(2,a):
        if a % i == 0:
            so_nguyen_to = False
            break
    if  so_nguyen_to:
        print(a,end=",")