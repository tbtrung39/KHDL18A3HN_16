# Câu 3 : Viết chương trình tính diện tích xung quanh, diện tích toàn phần và thể tích khối trụvới bán kính và chiều cao nhập từ bàn phím (Làm tròn đến số thập phân thứ hai). Biết𝜋 = 3.14
# from math import *
r = float(input('Nhập bán kính: '))
h = float(input('Nhập chiều cao: '))
pi = 3.14
dt_xq = 2 * pi * r * h
dt_tp = 2 * pi * r * (r + h)
v = pi * r**2 * h
print(f'Diện tích xung quanh: {dt_xq:.2f}')
print(f'Diện tích toàn phần: {dt_tp:.2f}')
print(f'Thể tích: {v:.2f}')
