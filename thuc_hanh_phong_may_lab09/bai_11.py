#Bài 11:
#Phần a
def tinh_giai_thua_kep(so_n):
    if so_n == 0 or so_n == 1:
        return 1
    return so_n * tinh_giai_thua_kep(so_n - 2)

#Phần b
def tinh_tong(so_k):
    tong = 0
    for i in range(1, so_k + 1):
        tong += ((-1) ** i) * tinh_giai_thua_kep(i)
    return tong

so_k = int(input("Nhập k (k<1000): "))
print(f"Giá trị tổng S là: {tinh_tong(so_k)}")