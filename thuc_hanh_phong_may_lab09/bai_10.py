#Bài 10:
def tinh_x(so_n):
    if so_n == 0:
        return 1
    tong = 0
    for i in range(so_n):
        tong += (so_n - 1) ** 2 * tinh_x(i)
    return tong

so_n = int(input("Nhập n: "))
print(f"Giá trị X_{so_n} là: {tinh_x(so_n)}")