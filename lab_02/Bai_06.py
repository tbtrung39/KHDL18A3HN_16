# Nhập thời gian sử dụng (giây)
t = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
# Thông số của bóng đèn
U = 220  # Hiệu điện thế (V)
I = 2.7  # Cường độ dòng điện (A)
P = U * I  # Công suất (W)
# Chuyển đổi thời gian từ giây sang giờ
t_sang_gio = t / 3600
# Điện năng tiêu thụ (Wh)
W = P * t_sang_gio
# Tính tiền điện (7000 đ/kWh)
W = (W / 1000) * 7000
print("Tiền điện phải trả là:", round(W, 2), "đồng")