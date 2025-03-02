x = float(input("Nhập hoành độ x: "))
y = float(input("Nhập tung độ y: "))
z = float(input("Nhập cao độ z: "))
# Tính tọa độ đối xứng
x_oxy = x
y_oxy = y
z_oxy = -z 

x_oxz = x
y_oxz = -y  
z_oxz = z

x_oyz = -x  
y_oyz = y
z_oyz = z
print(f"Điểm đối xứng qua mặt phẳng Oxy: ({x_oxy}, {y_oxy}, {z_oxy})")
print(f"Điểm đối xứng qua mặt phẳng Oxz: ({x_oxz}, {y_oxz}, {z_oxz})")
print(f"Điểm đối xứng qua mặt phẳng Oyz: ({x_oyz}, {y_oyz}, {z_oyz})")