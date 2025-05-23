n = int(input("Nhập số lượng phần tử n: "))
S = sum(1/i for i in range(1, n+1))
print(f"Tổng S: {S}")

n = int(input("Nhập số lượng phần tử n: "))
S = sum(1/(i*(i+1)) for i in range(2, n+2))
print(f"Tổng S: {S}")

import math
n = int(input("Nhập số nguyên dương n: "))
while n <= 1:
    n = int(input("Vui lòng nhập số lớn hơn 1: "))
S = 0.0
i = 2  
while i <= n:
    S += 1 / math.sqrt(i)
    i += 1
print("Tổng S =", S)