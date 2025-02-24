
gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))

if gio_bat_dau < 5 or gio_ket_thuc > 22 or gio_bat_dau > gio_ket_thuc:
    print("Giờ không hợp lệ!")
else:
    so_gio = gio_ket_thuc - gio_bat_dau
    gia_3_gio_dau = 100000
    gia_sau_3_gio = gia_3_gio_dau * 0.75
    if so_gio <= 3:
        tien_thue = so_gio * gia_3_gio_dau
    else:
        tien_thue = 3 * gia_3_gio_dau + (so_gio - 3) * gia_sau_3_gio
    if gio_bat_dau < 15 and gio_ket_thuc > 11:
        tien_thue = tien_thue * 0.9 
    print("Số tiền thuê sân phải trả là:", int(tien_thue), "VNĐ")
