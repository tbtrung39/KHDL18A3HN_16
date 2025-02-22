A=float(input("nhập hệ số a của phương trình bậc 2: "))
B=float(input("nhập hệ số b của phương trình bậc 2: "))
C=float(input("nhập hệ số c của phương trình bậc 2: "))
denta=B**2-4*A*C
x=-B/2*A
y=-denta/4*A
print(f"tọa độ đỉnh của phương trình là: ({x:.2f},{y:.2f})")