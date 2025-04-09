import random

a = []

for i in range(200):
    x = random.randint(0, 200)
    if x % 5 == 0 or x % 7 == 0:
        a.append(x)

print(a)