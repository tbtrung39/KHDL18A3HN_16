# Bài 9: Viết chương trình nhập vào một tọa độ trong không gian Oxyz. Tính tọa độ của điểmđối xứng với nó qua mặt phẳng Oxy, Oxz, Oyz

x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))
dx_Oxy = (x, y, -z)
dx_Oxz = (x, -y, z)
dx_Oyz = (-x, y, z)
print(f"Điểm đối xứng qua mặt phẳng Oxy: {dx_Oxy}")
print(f"Điểm đối xứng qua mặt phẳng Oxz: {dx_Oxz}")
print(f"Điểm đối xứng qua mặt phẳng Oyz: {dx_Oyz}")
