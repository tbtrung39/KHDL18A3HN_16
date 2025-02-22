# Nhập số phần tử của vector
n = int(input("Nhập số phần tử của vector: "))
# Khai báo vector a
print("Nhập các phần tử của vector a:")
a0 = float(input("a[0] = "))
a1 = float(input("a[1] = "))
a2 = float(input("a[2] = "))
# Khai báo vector b
print("Nhập các phần tử của vector b:")
b0 = float(input("b[0] = "))
b1 = float(input("b[1] = "))
b2 = float(input("b[2] = "))
tich_vo_huong = a0 * b0 + a1 * b1 + a2 * b2
print("Vector a:", a0, a1, a2)
print("Vector b:", b0, b1, b2)
print("Tích vô hướng của hai vector:", tich_vo_huong)