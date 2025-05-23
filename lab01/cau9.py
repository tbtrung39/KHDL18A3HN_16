import math
x = float(input("Nhập giá trị x (> 0): "))
if x <= 0:
    print("x phải lớn hơn 0")
else:
    log10_x = math.log10(x)
    log4_x = log10_x / math.log10(4)
    log10_x2 = 2 * log10_x
    fx = log4_x + log10_x2
    print("Giá trị của f(x) là:", round(fx, 2))