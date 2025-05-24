def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)
n = int(input("Nhap so nguyen duong n: "))
if n < 0:
    print("Khong tinh duoc giai thua cua so am.")
else:
    ket_qua = giai_thua(n)
    print(f"Giai thua cua {n} la: {ket_qua}")