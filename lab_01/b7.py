# câu 7

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))

x_dinh = -b / (2 * a)

y_dinh = a * x_dinh**2 + b * x_dinh + c

x_dinh = round(x_dinh, 2)
y_dinh = round(y_dinh, 2)

print("Đỉnh của phương trình bậc 2 có tọa độ (x, y) là: (", x_dinh, ",", y_dinh, ")")
