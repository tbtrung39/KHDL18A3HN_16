
xa, ya = map(float, input('Nhập tọa độ đỉnh A (xa, ya): ').split())
xb, yb = map(float, input('Nhập tọa độ đỉnh B (xb, yb): ').split())
xc, yc = map(float, input('Nhập tọa độ đỉnh C (xc, yc): ').split())

gx = (xa + xb + xc) / 3
gy = (ya + yb + yc) / 3

gx = round(gx, 2)
gy = round(gy, 2)

print('Trọng tâm của tam giác là (%0.2f, %0.2f)' % (gx, gy))
