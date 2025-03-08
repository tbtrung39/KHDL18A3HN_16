n = int(input("nhap n:"))
# a) S = 1 + 1/2 + 1/3 + ... + 1/n
S = 0
i = 1
while i <= n:
    S += 1 / i
    i += 1
print("S =", S)

# b) S = 1/2 + 2/3 + 3/4 + ... + n/(n+1)
S = 0
i = 1
while i <= n:
    S += i / (i + 1)
    i += 1
print("S =", S)

# c) S = 1/(1*2) + 1/(2*3) + ... + 1/(n*(n+1))
S = 0
i = 1
while i <= n:
    S += 1 / (i * (i + 1))
    i += 1
print("S =", S)

# d) S = 1 / sqrt(2) + 1 / sqrt(3) + ... + 1 / sqrt(n+1)
S = 0
i = 2
while i <= n + 1:
    S += 1 / (i ** 0.5)
    i += 1
print("S =", S)