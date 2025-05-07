def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)
def tinh_tong(k):
    if k == 0:
        return 0
    return ((-1) ** k) * giai_thua_kep(k) + tinh_tong(k - 1)
k = int(input("Nhập k: "))
if 0 < k < 1000:
    print("Tổng S =", tinh_tong(k))
else:
    print("Vui lòng nhập k là số tự nhiên nhỏ hơn 1000.")
