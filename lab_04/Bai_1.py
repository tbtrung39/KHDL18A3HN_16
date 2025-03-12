while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập một số nguyên dương!")

# a) Tính S4 = 1^2 + 2^2 + 3^2 + ... + n^2
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1

# b) Tính S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
S5 = 0
i = 1
while i <= (2*n+1):
    S5 += i**3
    i += 2  

# c) Tính S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
S6 = 0
i = 2
while i <= (2*n):
    S6 += i**4
    i += 2  

print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)