xa, ya = map(float, input("Nhập tọa độ A: ").split())
xb, yb = map(float, input("Nhập tọa độ B: ").split())
xc, yc = map(float, input("Nhập tọa độ C: ").split())
xg = (xa + xb + xc)/3
yg = (ya + yb + yc)/3
print(f"Trọng tâm của tam giác ABC là G({xg:.2f}, {yg:.2f})")