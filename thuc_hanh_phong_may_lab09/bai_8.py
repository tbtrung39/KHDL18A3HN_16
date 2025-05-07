#Bài 8:
import math

#Phần a
def tinh_tong_a(so_n):
    if so_n == 1:
        return 1
    return 1/so_n + tinh_tong_a(so_n - 1)

so_n = int(input("Nhập n: "))
print(f"Tổng S (a) = {tinh_tong_a(so_n)}")

#Phần b
def giai_thua(so_n):
    if so_n == 0 or so_n == 1:
        return 1
    return so_n * giai_thua(so_n - 1)

def tinh_tong_b(so_n):
    if so_n == 1:
        return 1/2
    return 1/giai_thua(so_n) + tinh_tong_b(so_n - 1)

so_n = int(input("Nhập n: "))
print(f"Tổng S (b) = {tinh_tong_b(so_n)}")

#Phần c
def tinh_tong_c(so_n):
    if so_n == 1:
        return math.sqrt(9 + math.sqrt(6 + math.sqrt(3)))
    return math.sqrt(3 * so_n + tinh_tong_c(so_n - 1))

so_n = int(input("Nhập n: "))
print(f"Tổng S (c) = {tinh_tong_c(so_n)}")

#Phần d
def tinh_tong_d(so_n):
    if so_n == 1:
        return math.sqrt(1)
    return math.sqrt(so_n + tinh_tong_d(so_n - 1))

so_n = int(input("Nhập n: "))
print(f"Tổng S (d) = {tinh_tong_d(so_n)}")