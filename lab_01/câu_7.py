def tinh_dinh_parabola(a, b, c):
    if a == 0:
        return "Lỗi: Đây không phải phương trình bậc 2"
    x_dinh = -b / (2 * a)
    y_dinh = (a * x_dinh ** 2) + (b * x_dinh) + c
    return round(x_dinh, 2), round(y_dinh, 2)
# Nhập hệ số a, b, c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
# Tính tọa độ đỉnh
dinh = tinh_dinh_parabola(a, b, c)
# Xuất kết quả
if isinstance(dinh, tuple):
    print(f"Tọa độ đỉnh của parabol: ({dinh[0]}, {dinh[1]})")
else:
    print(dinh)