# Nhập tọa độ điểm A(x, y, z)
x,y,z = map(float,input('Xin mời nhập tọa độ điểmđiểm A: ').split())
# Tính tọa độ đối xứng
x_oxy = x
y_oxy = y
z_oxy = -z # Đối xứng qua Oxy
x_oxz = x
y_oxz = -y # Đối xứng qua Oxz
z_oxz = z
x_oyz = -x # Đối xứng qua Oyz
y_oyz = y
z_oyz = z
# Xuất kết quả
print(f"Điểm đối xứng qua mặt phẳng Oxy: ({x_oxy}, {y_oxy}, {z_oxy})")
print(f"Điểm đối xứng qua mặt phẳng Oxz: ({x_oxz}, {y_oxz}, {z_oxz})")
print(f"Điểm đối xứng qua mặt phẳng Oyz: ({x_oyz}, {y_oyz}, {z_oyz})")
