import math
def tinh_toan_khoi_tru(r, h):
    pi = 3.14
    dien_tich_xung_quanh = round(2 * pi * r * h, 2)
    dien_tich_toan_phan = round(2 * pi * r * (r + h), 2)
    the_tich = round(pi * r**2 * h, 2)
    return dien_tich_xung_quanh, dien_tich_toan_phan, the_tich
# Nhập dữ liệu từ người dùng
r = float(input("Nhập bán kính khối trụ: "))
h = float(input("Nhập chiều cao khối trụ: "))
# Tính toán
dtxq, dttp, tt = tinh_toan_khoi_tru(r, h)
# Xuất kết quả
print(f"Diện tích xung quanh: {dtxq} m^2")
print(f"Diện tích toàn phần: {dttp} m^2")
print(f"Thể tích: {tt} m^3")