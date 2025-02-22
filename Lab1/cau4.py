#câu 4 : Cho biểu thức 𝑓(𝑥) = −𝑥+√𝑥2+47√𝑥4+1Viết chương trình nhập vào x và tính giá trị của biểu thức (Làm tròn đến số thập phân thứhai).
import math

# Hàm tính giá trị của biểu thức f(x)
def calculate_expression(x):
    if x >= 0:  # Đảm bảo x là số không âm, vì căn bậc hai không xác định cho số âm
        # Tính giá trị biểu thức f(x)
        part1 = -x
        part2 = math.sqrt(x**2 + 4)
        part3 = (x**4 + 1)**(1/7)  # Tính căn bậc 7 của (x^4 + 1)
        
        result = part1 + (part2 / part3)
        return round(result, 2)
    else:
        return "Giá trị x phải lớn hơn hoặc bằng 0!"

# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị x: "))

# Tính và in kết quả
result = calculate_expression(x)
print(f"Giá trị của biểu thức f(x) là: {result}")
