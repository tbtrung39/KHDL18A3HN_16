import csv
from xuly_tt_nvien import *

ds_nhan_vien = []

with open('ds_nhanvien.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        ma_nv, ho_ten, chuc_vu, he_so_str = row
        he_so = float(he_so_str)
        luong = tinh_luong(he_so)
        phu_cap = tinh_phu_cap(chuc_vu)
        thuc_linh = tinh_thuc_linh(luong, phu_cap)
        ds_nhan_vien.append([ma_nv, ho_ten, chuc_vu, he_so, luong, phu_cap, thuc_linh])

# Sắp xếp theo thực lĩnh giảm dần
ds_nhan_vien.sort(key=lambda x: x[6], reverse=True)

# Ghi ra file kết quả
with open('files/Ketqua.txt', 'w', encoding='utf-8') as f:
    for nv in ds_nhan_vien:
        f.write(f'{nv[0]}, {nv[1]}, {nv[6]:,.0f} VND\n')

print("Đã ghi kết quả vào file Ketqua.txt")
