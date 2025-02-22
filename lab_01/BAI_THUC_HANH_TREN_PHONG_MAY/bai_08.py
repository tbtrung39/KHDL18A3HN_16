# Nhập tọa độ từ người dùng
xA = float(input("Nhập tọa độ x của đỉnh A: "))
yA = float(input("Nhập tọa độ y của đỉnh A: "))
xB = float(input("Nhập tọa độ x của đỉnh B: "))
yB = float(input("Nhập tọa độ y của đỉnh B: "))
xC = float(input("Nhập tọa độ x của đỉnh C: "))
yC = float(input("Nhập tọa độ y của đỉnh C: "))

# Tính tọa độ đỉnh
xG = round((xA + xB + xC) / 3, 2)
yG = round((yA + yB + yC) / 3, 2)


# IN ra kết quả
print("Tọa độ trọng tâm của tam giác là:", (xG, yG))

