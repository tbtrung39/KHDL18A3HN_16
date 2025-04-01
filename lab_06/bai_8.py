import math

n = int(input("Nhập n = "))
m = []

for i in range(0, n + 1):
    x = (1/math.sqrt(5)) * ((((1 + math.sqrt(5))/2)**i) - (((1 - math.sqrt(5))/2)**i))
    m.append(round(x))

print(m)