import math
# Nhập giá trị x từ người dùng
x = int(input("Nhập giá trị x: "))
# Tính giá trị của biểu thức (giả sử người dùng nhập đúng x > 0 và x ≠ 1)
f_x = (math.log(x) / math.log(4)) + (math.log(2) / math.log(x))
print("Giá trị của biểu thức là:", round(f_x, 2))