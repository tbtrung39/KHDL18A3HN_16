gio_bat_dau = int(input("Nhập giờ bắt đấu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    tong_so_tien = 0
    thoi_gian_thue = 0
    giam_gia = 1
    if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
        giam_gia = 0.9
    if gio_bat_dau < gio_ket_thuc and gio_bat_dau < gio_bat_dau + 3:
        thoi_gian_dau = gio_ket_thuc - gio_bat_dau
        if thoi_gian_dau > 3:
            thoi_gian_dau = 3
        tong_so_tien = thoi_gian_dau * 100000
        gio_bat_dau += thoi_gian_dau
    if gio_ket_thuc > gio_bat_dau:
        thoi_gian_tiep_theo = gio_ket_thuc - gio_bat_dau
        tong_so_tien += thoi_gian_tiep_theo * 100000 * 0.75
    tong_so_tien *= giam_gia
    print(f"Tiền phải trả là: {round(tong_so_tien):_} đồng")
else:
    print("Nhập lại")