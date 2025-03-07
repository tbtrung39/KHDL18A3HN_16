n = int(input("Nhập số n: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n: "))
S, i, sign = 0, 1, 1
while i <= n:
    S += sign * (1/i)
    sign *= -1
print("S =", S)
