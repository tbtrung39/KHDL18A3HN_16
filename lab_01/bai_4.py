import math
x = float(input("nhập giá trị của n:"))
f_x = (-x + math.sqrt(x**2 + 4)) / math.sqrt(x**4 + 1)
print(f"giá trị của f(x) là: {f_x:.2f}")
