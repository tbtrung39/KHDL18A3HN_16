# Nhập tọa độ các đỉnh của tam giác
x1, y1 = map(float, input("Nhập tọa độ điểm A (x1, y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ điểm B (x2, y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ điểm C (x3, y3): ").split())
# Tính tọa độ trọng tâm
Gx = (x1 + x2 + x3) / 3
Gy = (y1 + y2 + y3) / 3
print(f"Tọa độ trọng tâm G: ({round(Gx, 2)}, {round(Gy, 2)})")