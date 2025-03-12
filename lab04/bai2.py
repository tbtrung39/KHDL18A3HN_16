while True:
    n = int(input("Nhap so nguyen duong n: "))
    if n > 0:
        break
    print("Vui long nhap lai so nguyen duong!")

# Tinh tong a: S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ...
S1 = 0
kc = 1
for i in range(1, n + 1):
    S1 += kc * (1 / i)
    kc *= -1
print("a) S = ", S1)

# Tinh tong b: S = 1/2 + 1/(2.3) + 1/(3.4) + 1/(4.5) + ...
S2 = 0
for i in range(2, n + 1):
    S2 += 1 / (i * (i - 1))
print("b) S = ", S2)

# Tinh tong c: S = 1/sqrt(2) + 1/sqrt(3) + 1/sqrt(4) + 1/sqrt(5) + ...
import math
S3 = 0
i = 2
while i <= n:
    S3 += 1 / math.sqrt(i)
    i += 1
print("c) S = ", S3)