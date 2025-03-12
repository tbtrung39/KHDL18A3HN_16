while True:
    n = int(input("Nhap so nguyen duong n: "))
    if n > 0:
        break
    print("Vui long nhap lai so nguyen duong!")

#a
S1 = 0
kc = 1
for i in range(1, n + 1):
    S1 += kc * (1 / i)
    kc *= -1
print("a) S = ", S1)

#b
S2 = 0
for i in range(2, n + 1):
    S2 += 1 / (i * (i - 1))
print("b) S = ", S2)

#c
import math
S3 = 0
i = 2
while i <= n:
    S3 += 1 / math.sqrt(i)
    i += 1
print("c) S = ", S3)

        