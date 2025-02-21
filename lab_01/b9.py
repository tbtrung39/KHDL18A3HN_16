#câu 9

x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

doi_xung_oxy = (x, y, -z)
doi_xung_oxz = (x, -y, z)
doi_xung_oyz = (-x, y, z)

print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy là:", doi_xung_oxy)
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz là:", doi_xung_oxz)
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz là:", doi_xung_oyz)
