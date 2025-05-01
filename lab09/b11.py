# Hàm tính giai thừa kép
def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)

# Hàm tính tổng theo công thức
def tinh_tong(k):
    tong = 0
    for i in range(1, k + 1):
        tong += (i * giai_thua_kep(i))
    return tong

# Nhập giá trị k từ người dùng
k = int(input("Nhập giá trị k (k ≤ 1000): "))
print("Giá trị tổng là:", tinh_tong(k))
