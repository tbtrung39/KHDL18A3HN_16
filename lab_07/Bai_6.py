n = int(input("Nhap so nguyen duong n: "))
print("Cac so nguyen to nho hon", n, "la:")
for i in range(2, n):
    la_nto = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            la_nto = False
            break
    if la_nto:
        print(i, end=" ")