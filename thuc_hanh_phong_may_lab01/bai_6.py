#Bài 6:
thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
hieu_dien_the = 220
cuong_do_dong_dien = 2.7
gia_tien_dien = 7000
cong_suat = hieu_dien_the * cuong_do_dong_dien
nang_luong = (cong_suat * thoi_gian) / 3600000
tien_dien = nang_luong * gia_tien_dien
print(f"Tiền điện phải trả là: {tien_dien:.2f} đồng")