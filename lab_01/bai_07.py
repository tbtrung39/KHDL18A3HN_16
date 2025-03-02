a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
# Tính tọa độ đỉnh
x_d = -b / (2 * a)
y_d = a * (x_d ** 2) + b * x_d + c  
# Làm tròn kết quả đến 2 chữ số thập phân
x_d = round(x_d, 2)
y_d = round(y_d, 2)
print(f"Tọa độ đỉnh của parabol: ({x_d}, {y_d})")