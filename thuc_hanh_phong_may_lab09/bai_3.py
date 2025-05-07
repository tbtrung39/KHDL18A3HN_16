#Bài 3:
def tinh_tong_luy_thua_2(so_n):
    if so_n == 2:
        return 2
    return 2**so_n + tinh_tong_luy_thua_2(so_n - 1)

so_n = int(input("Nhập số n: "))
ket_qua = tinh_tong_luy_thua_2(so_n)
print(f"Tổng lũy thừa của 2 là: {ket_qua}")