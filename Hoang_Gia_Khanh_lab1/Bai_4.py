import math
x = float(input("Nhập x: "))
f = (-x + math.sqrt((x**2) + 4))/(((x**4) + 1)**(1/7))
print(f"Với x = {x} <=> f(x) = {f:.2f}")