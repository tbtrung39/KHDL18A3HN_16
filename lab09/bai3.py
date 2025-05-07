def luy_thua(a, n):
    if n == 0:
        return 1
    else:
        return a * luy_thua(a, n - 1)
a = float(input("Nhập a: "))
n = int(input("Nhập số mũ n (n ≥ 0): "))
if n < 0:
    print("n phải lớn hơn hoặc = 0!")
else:
    ket_qua = luy_thua(a, n)
    print(f"{a}^{n} =", ket_qua)
