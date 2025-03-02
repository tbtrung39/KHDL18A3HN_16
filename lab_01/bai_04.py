import math
# Nhập giá trị x từ người dùng
x = int(input("Nhập giá trị x: "))
# Tính giá trị của biểu thức
f_x = (-x + math.sqrt(x**2 + 4)) / ((x**4 + 1) ** (1/7))
print("Giá trị của biểu thức là:", round(f_x, 2))