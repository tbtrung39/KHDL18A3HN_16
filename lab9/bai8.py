#a
def tong_a(n):
    if n == 1:
        return 1
    return 1/n + tong_a(n-1)

n = int(input("Nhap n: "))
print("Tong S (a) =", tong_a(n))
#b
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def tong_b(n):
    if n == 1:
        return 1/2
    return 1/factorial(n) + tong_b(n-1)

n = int(input("Nhap n: "))
print("Tong S (b) =", tong_b(n))
#
import math

def tong_c(n):
    if n == 1:
        return math.sqrt(9 + math.sqrt(6 + math.sqrt(3)))
    return math.sqrt(3*n + tong_c(n-1))

n = int(input("Nhap n: "))
print("Tong S (c) =", tong_c(n))
#d
import math

def tong_d(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n + tong_d(n-1))

n = int(input("Nhap n: "))
print("Tong S (d) =", tong_d(n))