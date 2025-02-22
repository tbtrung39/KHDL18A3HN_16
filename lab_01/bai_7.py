a = float(input("nhập hệ số a:"))
b = float(input("nhập hệ số b:"))
c = float(input("nhập hệ số c:"))
x_dinh = -b / (2*a)
y_dinh = a * x_dinh**2 + b * x_dinh + c
print(f"toạ độ đỉnh của parabol là: ({x_dinh:.2f}, {y_dinh:.2f})")