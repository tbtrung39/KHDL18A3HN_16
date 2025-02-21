a, b, c = map(float, input("Nhập a, b, c: ").split())
delta = (b**2) - 4*a*c
x = -b/(2*a)
y = -delta/(4*a)
print(f"Tọa độ đỉnh của phương trình bậc 2 là: ({x:.2f},{y:.2f}")