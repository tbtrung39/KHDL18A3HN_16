import math
def tinh_fx(x):
    try:
        # Tính toán biểu thức f(x)
        tu_so = -x + math.sqrt(x)
        mau_so = (2 + 4 * math.sqrt(x)) * (4 + 1) * 7
        f_x = tu_so / mau_so
        return round(f_x, 2)  # Làm tròn đến 2 chữ số thập phân
    except ValueError:
        return "Lỗi: Giá trị đầu vào không hợp lệ"
# Nhập giá trị x từ bàn phím
x = float(input("Nhập giá trị x: "))
# Tính và hiển thị kết quả
ket_qua = tinh_fx(x)
print(f"Giá trị của f(x): {ket_qua}")