n = int(input("Nhập n: "))

for i in range(2, n):
    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong += j
    if tong == i:
        print(i, end=" ")