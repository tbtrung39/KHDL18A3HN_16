import math

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Lỗi: Cạnh tam giác phải là số dương.")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("Lỗi: Ba cạnh không tạo thành tam giác.")
    else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Diện tích tam giác là: {s:.2f}")
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ.")
