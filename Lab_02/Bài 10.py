gio_bat_dau= int( input(" Nhập giờ bắt đầu: "))
gio_ket_thuc= int( input(" Nhập giờ kết thúc: "))
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    so_gio = gio_ket_thuc - gio_bat_dau
    gia_3_gio_dau = 100000
    gia_giam = gia_3_gio_dau * 0.75
    if so_gio <= 3:
        tong_tien = so_gio * gia_3_gio_dau
    else:
        tong_tien = 3 * gia_3_gio_dau + ( so_gio- 3) * gia_giam
    if 11<= gio_bat_dau< gio_ket_thuc<= 15:
        tong_tien = tong_tien* 0.9
    print(f"Số tiền khách phải trả: {tong_tien} đồng")
else:
    print("Vui lòng nhập giờ hợp lệ trong khoảng 5 đến 22 giờ!")