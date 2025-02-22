import math
# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị x: "))

# Tính toán
if x <= 0 or x == 1:
 print(input("Giá trị x không hợp lệ (x > 0 và x != 1)."))

log4_x = math.log(x, 4)  # logarit cơ số 4 của x
logx_2 = math.log(2, x)  # logarit cơ số x của 2
ket_qua = round(log4_x + logx_2, 2)

# In kết quả
print("f(x) =", ket_qua)