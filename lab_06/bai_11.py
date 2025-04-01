import random

A = []

for i in range(100):
    x = random.randint(0, 100)
    if x % 3 == 0:
        A.append(x)

print(A[5:])

C = A * 2