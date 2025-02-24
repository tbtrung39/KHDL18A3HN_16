# Đơn giá thuê sân
gia_3_gio_dau = 100000
giam_gia_gio_sau = 0.25  
giam_gia_trong_khung_gio = 0.10  
gio_bat_dau = int(input("Nhập giờ bắt đầu (5 - 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5 - 22): "))
if gio_bat_dau < 5 or gio_ket_thuc > 22 or gio_bat_dau > gio_ket_thuc:
    tong_tien = -1  # Dùng giá trị -1 để báo lỗi giờ không hợp lệ
else:
    tong_gio = gio_ket_thuc - gio_bat_dau
    if tong_gio <= 3:
        tong_tien = tong_gio * gia_3_gio_dau
    else:
        tong_tien = (3 * gia_3_gio_dau) + ((tong_gio - 3) * gia_3_gio_dau * (1 - giam_gia_gio_sau))
    if (gio_bat_dau < 15 and gio_ket_thuc > 11):
        tong_tien = tong_tien * (1 - giam_gia_trong_khung_gio)
if tong_tien == -1:
    print("Giờ không hợp lệ! Vui lòng nhập lại.")
else:
    print("Số tiền khách phải trả:", int(tong_tien), "VND")
