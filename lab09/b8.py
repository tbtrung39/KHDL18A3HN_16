# Hàm tính giai thừa
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

# Tính tổng S(b) = 1/2! + 1/3! + ... + 1/n!
def tong_b(n):
    if n == 2:
        return 1 / giai_thua(2)
    return 1 / giai_thua(n) + tong_b(n - 1)

n = int(input("Nhập số nguyên n để tính tổng S(b): "))
print("Tổng S(b) =", tong_b(n))
import math

# Tính tổng căn bậc hai: S(d) = √n + √(n-1) + ... + √1
def tong_d(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n) + tong_d(n - 1)

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
print("Tổng S(d) =", tong_d(n))
