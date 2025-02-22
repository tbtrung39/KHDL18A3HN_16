# Nhập tọa độ điểm từ người dùng
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))
# Tính toán tọa độ đối xứng
oxy_symmetry = (x, y, -z)   # Đối xứng qua Oxy
oxz_symmetry = (x, -y, z)   # Đối xứng qua Oxz
oyz_symmetry = (-x, y, z)   # Đối xứng qua Oyz
# Xuất kết quả
print(f"Tọa độ đối xứng qua mặt phẳng Oxy: {oxy_symmetry}")
print(f"Tọa độ đối xứng qua mặt phẳng Oxz: {oxz_symmetry}")
print(f"Tọa độ đối xứng qua mặt phẳng Oyz: {oyz_symmetry}")