# câu 3
import math 
r = float(input("nhập bán kính đáy (r): "))
h = float(input("nhập chiều cao (h):"))
pi = 3.14 
dien_tich_xung_quanh = 2*pi*r*(r + h )
dien_tich_toan_phan = 2 *pi * r * (r + h )
the_tich = pi * r ** 2 * h 
print("diện tích xung quanh: ", round(dien_tich_xung_quanh, 2))
print("diện tích toàn phần: ", round(dien_tich_toan_phan, 2))
print("thể tích khối trụ: ", round(the_tich, 2))