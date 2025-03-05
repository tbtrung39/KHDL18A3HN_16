n = int(input("Nhập n: "))

S1 = sum(range(1, n + 1))  # S1 = 1 + 2 + ... + n
S2 = sum(range(1, 2 * n, 2))  # S2 = 1 + 3 + 5 + ... + (2n+1)
S3 = sum(range(2, 2 * n + 1, 2))  # S3 = 2 + 4 + 6 + ... + 2n

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
