import math
# Nhập giá trị x
x = float(input("Nhập giá trị x: "))
# Kiểm tra x có hợp lệ không (x phải > 0 và x ≠ 1)
if x > 0 and x != 1:
    log2_x = math.log2(x)  # Tính log cơ số 2 của x
    f_x = (log2_x / 2) + (1 / log2_x)  # Tính giá trị biểu thức
    print(f"Giá trị của f(x) là: {round(f_x, 2)}")  # Làm tròn đến 2 chữ số thập phân
else:
    print("Giá trị x không hợp lệ! x phải lớn hơn 0 và khác 1.")