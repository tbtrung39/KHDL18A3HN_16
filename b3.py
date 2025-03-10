import math
while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập lại số nguyên dương!")

# Tính tổng a: S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ...
S_a = 0
sign = 1
for i in range(1, n + 1):
    S_a += sign * (1 / i)
    sign *= -1
print("Tổng S_a =", S_a)

# Tính tổng b: S = 1/2 + 1/(2.3) + 1/(3.4) + 1/(4.5) + ...
S_b = 0
for i in range(2, n + 1):
    S_b += 1 / (i * (i - 1))
print("Tổng S_b =", S_b)

# Tính tổng c: S = 1/sqrt(2) + 1/sqrt(3) + 1/sqrt(4) + 1/sqrt(5) + ...
S_c = 0
i = 2
while i <= n:
    S_c += 1 / math.sqrt(i)
    i += 1
print("Tổng S_c =", S_c)

# Tính cos(x) theo công thức truy hồi với sai số 10^-4
x = float(input("Nhập giá trị x (radian): "))
cos_x = 1
term = 1  # Giá trị của từng hạng tử
k = 1
fact = 1  # Gán giá trị giai thừa ban đầu
while abs(term) > 1e-4:
    fact *= (2 * k - 1) * (2 * k)  # Tính giai thừa theo cách truy hồi
    term *= - (x ** 2) / fact
    cos_x += term
    k += 1
print("Giá trị xấp xỉ của cos(x) là:", cos_x)