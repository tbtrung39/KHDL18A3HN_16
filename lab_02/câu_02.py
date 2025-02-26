import math
def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình vô số nghiệm."
            else:
                return "Phương trình vô nghiệm."
        else:
            # Phương trình bậc nhất bx + c = 0
            x = -c / b
            return f"Phương trình có một nghiệm: x = {x:.2f}"
    else:
        # Tính delta
        delta = b**2 - 4*a*c
        if delta > 0:
            # Hai nghiệm phân biệt
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return f"Phương trình có hai nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}"
        elif delta == 0:
            # Nghiệm kép
            x = -b / (2 * a)
            return f"Phương trình có nghiệm kép: x = {x:.2f}"
        else:
            # Không có nghiệm thực
            return "Phương trình vô nghiệm thực."
# Nhập các hệ số a, b, c từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
# Gọi hàm và in kết quả
ket_qua = giai_phuong_trinh_bac_hai(a, b, c)
print(ket_qua)