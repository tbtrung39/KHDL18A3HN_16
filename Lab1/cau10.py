#câu 10 : Cho biểu thức 𝑓(𝑥) = log4 𝑥 + log𝑥 2Viết chương trình nhập vào x và tính giá trị của biểu thức (Làm tròn đến số thập phân thứhai).
import math

# Hàm tính giá trị của biểu thức f(x)
def calculate_expression(x):
    if x > 0:
        # Tính log4(x) = log(x) / log(4)
        log4_x = math.log(x, 4)
        
        # Tính log_x(2) = log(2) / log(x)
        log_x_2 = math.log(2) / math.log(x)
        
        # Tính giá trị của f(x)
        result = log4_x + log_x_2
        return round(result, 2)
    else:
        return "Giá trị x phải lớn hơn 0!"

# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị x: "))

# Tính và in kết quả
result = calculate_expression(x)
print(f"Giá trị của biểu thức f(x) là: {result}")

