xA, yA = map(float, input("nhập toạ độ điểm A: ").split())
xB, yB = map(float, input("nhập toạ độ điểm B: ").split())
xC, yC = map(float, input("nhập toạ độ điểm C: ").split())
Gx = (xA + xB + xC) / 3
Gy = (yA + yB + yC) / 3
print(f"toạ điểm trọng tâm cả tam giác: ({Gx:.2f}, {Gy:.2f})")