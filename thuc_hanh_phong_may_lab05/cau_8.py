#Bài 8:
#Cách 1:
doan_van = input("Nhập đoạn văn: ")
tu_tim_kiem = input("Nhập từ cần tìm: ")
for dau_cau in ",.::!?-()\"'":
    doan_van = doan_van.replace(dau_cau, " ")
doan_van = doan_van.lower()
tu_tim_kiem = tu_tim_kiem.lower()
danh_sach_tu = doan_van.split()
so_lan_xuat_hien = 0
for tu in danh_sach_tu:
    if tu == tu_tim_kiem:
        so_lan_xuat_hien += 1
print(f"Từ '{tu_tim_kiem}' xuất hiện {so_lan_xuat_hien} lần.")

#Cách 2:
doan_van = input("Nhập đoạn văn: ")
tu_tim_kiem = input("Nhập từ cần tìm: ")
for dau_cau in ",.::!?-()\"'":
    doan_van = doan_van.replace(dau_cau, " ")
danh_sach_tu = doan_van.lower().split()
tu_tim_kiem = tu_tim_kiem.lower()
so_lan_xuat_hien = danh_sach_tu.count(tu_tim_kiem)
print(f"Từ '{tu_tim_kiem}' xuất hiện {so_lan_xuat_hien} lần.")