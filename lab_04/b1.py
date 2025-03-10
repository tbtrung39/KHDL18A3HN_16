while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập lại số nguyên dương!")

# Tính tổng S4 = 1^2 + 2^2 + ... + n^2
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print("Tổng S4 =", S4)

# Tính tổng S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
S5 = 0
j = 1
count = 0
while count < n:
    S5 += j**3
    j += 2
    count += 1
print("Tổng S5 =", S5)

# Tính tổng S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
S6 = 0
k = 2
while k <= 2*n:
    S6 += k**4
    k += 2
print("Tổng S6 =", S6)
