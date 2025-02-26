# Nhập giờ bắt đầu và giờ kết thúc từ người dùng
gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))
# Tính toán
if (5 <= gio_bat_dau <= gio_ket_thuc <= 22): 
  thoi_gian_thue = gio_ket_thuc - gio_bat_dau
  tien_thue = 0
  if thoi_gian_thue <= 3:
    tien_thue = thoi_gian_thue * 100000
  else:
    tien_thue = 3 * 100000 + (thoi_gian_thue - 3) * 100000 * 0.75
  if 11 <= gio_bat_dau <= 15:
    tien_thue *= 0.9

# Tính và in tiền thuê sân
print("Tiền thuê sân là: ",tien_thue)

