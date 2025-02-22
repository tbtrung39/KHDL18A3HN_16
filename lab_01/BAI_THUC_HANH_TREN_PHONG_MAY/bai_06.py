# Nhập dữ liệu từ người dùng
thoi_gian_su_dung_giay = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
hieu_dien_the_volt = 220.0  # Hiệu điện thế không đổi
cuong_do_dong_dien_amp = 2.7  # Cường độ dòng điện không đổi
gia_dien_kwh = 7000.0  # Giá tiền điện không đổi
# Công thức tính tiền điện
cong_suat_watt = hieu_dien_the_volt * cuong_do_dong_dien_amp
cong_suat_kilowatt = cong_suat_watt / 1000.0
thoi_gian_su_dung_gio = thoi_gian_su_dung_giay / 3600.0
dien_nang_tieu_thu_kwh = cong_suat_kilowatt * thoi_gian_su_dung_gio
tien_dien = dien_nang_tieu_thu_kwh * gia_dien_kwh
# In kết quả
print("Tiền điện phải trả:", tien_dien, "đồng")


