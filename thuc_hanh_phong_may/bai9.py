x=float(input("nhập điểm x trong vecto tọa độ: "))
y=float(input("nhập điểm x trong vecto tọa độ: "))
z=float(input("nhập điểm x trong vecto tọa độ: "))
dx_qua_Oxy=x, y, -z
dx_qua_Oxz=x, -y, z
dx_qua_Oyz=-x, y, z
print(f"vecto đối xứng qua mặt phẳng Oxy: ({dx_qua_Oxy[0]:.2f},{dx_qua_Oxy[1]:.2f},{dx_qua_Oxy[2]:.2f})")
print(f"vecto đối xứng qua mặt phẳng Oxz: ({dx_qua_Oxz[0]:.2f},{dx_qua_Oxz[1]:.2f},{dx_qua_Oxz[2]:.2f})")
print(f"vecto đối xứng qua mặt phẳng Oyz: ({dx_qua_Oyz[0]:.2f},{dx_qua_Oyz[1]:.2f},{dx_qua_Oyz[2]:.2f})")