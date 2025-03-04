n = int(input("Nhập số hoàn hảo n: "))
for a in range(1,n):
    tong = 0
    for i in range(1,a):
        if a % i == 0:
            tong += 1 
    if tong == 0:
        print("Số hoàn hảo nhỏ hơn a:",a)