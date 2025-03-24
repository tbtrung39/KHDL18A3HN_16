chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
chuoi_con_chung_max = ""
for vi_tri_bat_dau in range(len(chuoi_1)):
    for vi_tri_ket_thuc in range(vi_tri_bat_dau + 1, len(chuoi_1) + 1):
        chuoi_con = chuoi_1[vi_tri_bat_dau:vi_tri_ket_thuc]
        if chuoi_con in chuoi_2 and len(chuoi_con) > len(chuoi_con_chung_max):
            chuoi_con_chung_max = chuoi_con
if chuoi_con_chung_max:
    print("Chuỗi con chung dài nhất là:", chuoi_con_chung_max)
else:
    print("Không có chuỗi con chung nào.")