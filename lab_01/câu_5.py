def tich_vo_huong(a, b):
    if len(a) != len(b):
        return "Lỗi: Hai vector phải có cùng số phần tử"
    return sum(a[i] * b[i] for i in range(len(a)))
# Nhập số chiều của vector
n = int(input("Nhập số phần tử của vector: "))
# Nhập vector a
a = [float(input(f"Nhập a[{i}]: ")) for i in range(n)]
# Nhập vector b
b = [float(input(f"Nhập b[{i}]: ")) for i in range(n)]
# Tính tích vô hướng
tich = tich_vo_huong(a, b)
# Xuất kết quả
print(f"Tích vô hướng của hai vector: {tich}")
