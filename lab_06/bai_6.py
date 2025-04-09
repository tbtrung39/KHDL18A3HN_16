import random

A = []

for i in range(1000):
    x = random.randint(0, 99999)
    A.append(x)

print(A)
print(sorted(A))