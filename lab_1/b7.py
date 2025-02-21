# câu 7 
a = float(input("nhập hệ số a: "))
b = float(input("nhập hệ số b: "))
c = float(input("nhập hệ số c: "))
# tính tọa độ đỉnh 
x_dinh = -b / (2*a)
y_dinh = a*x_dinh**2 + b*x_dinh + c 
print("tọa độ đỉnh: ({}, {})".format(round(x_dinh, 2), round(y_dinh, 2)))