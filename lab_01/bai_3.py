r = float(input("nhập bán kính khối trụ:"))
h = float(input("nhập chiều cao khối trụ:"))
pi = 3.14
dien_tich_xq = 2*pi*r*h
dien_tich_tp = dien_tich_xq + 2 * pi * r ** 2
print(f"dien_tich_xung_quanh: {dien_tich_xq:.2f}")
print(f"dien_tich_toan_phan: {dien_tich_tp:.2f}")
