giay = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
U = 220
I = 2.7
tien_dien = 7000
power = U * I
print(" Công suất tiêu thụ: ", power)
gio = giay / 3600
nang_luong_tieu_thu = (power / 1000) * gio
print(f" Năng lượng tiêu thụ trong {gio} : {nang_luong_tieu_thu}")
electricity_cost = nang_luong_tieu_thu* tien_dien
print(f"Tiền điện phải trả: {electricity_cost:.2f} đ")