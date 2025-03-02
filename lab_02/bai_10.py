GIA_3_GIO_DAU = 100000
GIAM_GIA_25 = 0.75  # Giảm 25%
GIAM_GIA_10 = 0.90  # Giảm 10% nếu thuê từ 11h - 15h
gio_bat_dau = int(input("Nhập giờ bắt đầu thuê (5 - 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê (5 - 22): "))
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    print("Giờ nhập không hợp lệ! Vui lòng nhập lại.")
# Tính tổng số giờ thuê
so_gio_thue = gio_ket_thuc - gio_bat_dau
# Tính tiền thuê sân
if so_gio_thue <= 3:
    tong_tien = so_gio_thue * GIA_3_GIO_DAU
else:
    tong_tien = (3 * GIA_3_GIO_DAU) + ((so_gio_thue - 3) * GIA_3_GIO_DAU * GIAM_GIA_25)
# Kiểm tra khung giờ giảm giá 10%
if gio_bat_dau < 15 and gio_ket_thuc > 11:
    tong_tien *= GIAM_GIA_10  # Giảm 10%
print(f"Số giờ thuê: {so_gio_thue}")
print(f"Tổng tiền thuê sân: {tong_tien:,.0f} đồng")
