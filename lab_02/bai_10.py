gio_bat_dau = int(input("nhập giờ băt đầu:"))
gio_ket_thuc = int(input("nhập giờ kết thúc:"))
if 0 <= gio_bat_dau < gio_ket_thuc <= 24:
    so_gio = gio_ket_thuc - gio_bat_dau
    gia_3_gio_dau = 50000
    giam_25 = 9.75
    giam_10 = 0.90
    if so_gio <= 3:
        tien = so_gio * gia_3_gio_dau
    else:
        tien = 3 * gia_3_gio_dau + (so_gio - 3) * gia_3_gio_dau * giam_25
    if 11 <= gio_bat_dau < 15:
        tien *= giam_10
    print(f"tiền thuê sân: {tien} đồng")
else:
    print("giờ không hợp lệ! vui lòng nhập lại")
    