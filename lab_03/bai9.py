n = int(input("Nhập n: "))

S4 = sum(i ** 2 for i in range(1, n + 1))  # S4 = 1^2 + 2^2 + ... + n^2
S5 = sum(i ** 3 for i in range(1, n + 1))  # S5 = 1^3 + 3^3 + ... + (2n+1)^3
S6 = sum((2 * i) ** 4 for i in range(1, n + 1))  # S6 = 2^4 + 4^4 + ... + (2n)^4

print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)
