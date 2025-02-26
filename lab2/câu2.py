import math

# Hàm giải phương trình bậc 2
def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        print("Không phải phương trình bậc hai vì a = 0.")
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            # Trường hợp phương trình bậc nhất bx + c = 0
            x = -c / b
            print(f"Phương trình có nghiệm x = {x}")
    else:
        # Tính delta
        delta = b**2 - 4*a*c

        if delta > 0:
            # Hai nghiệm phân biệt
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
        elif delta == 0:
            # Nghiệm kép
            x = -b / (2*a)
            print(f"Phương trình có nghiệm kép: x = {x}")
        else:
            # Vô nghiệm
            print("Phương trình vô nghiệm trong tập số thực.")

# Nhập vào các hệ số a, b, c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm giải phương trình bậc hai
giai_phuong_trinh_bac_hai(a, b, c)
