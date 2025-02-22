# Nhập hệ số a,b,c
a,b,c = map(float,input('Nhập hệ số a,b,c: ').split())
# Tính tọa độ đỉnh
x_đỉnh = -b/(2*a)
y_đỉnh = -((b**2)-4*a*c)/(4*a)
# Làm tròn 
x_đỉnh=round(x_đỉnh,2)
y_đỉnh=round(y_đỉnh,2)
# Kết quả
print(f'Tọa độ đỉnh là: ({x_đỉnh},{y_đỉnh})')
 
