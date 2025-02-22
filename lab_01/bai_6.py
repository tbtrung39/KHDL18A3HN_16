hieu_dien_the = 220
cuong_do_dien = 2.7
gia_dien = 7000
t = float(input("nhập thời gian sử dụng bóng đèn:"))
cong_suat = hieu_dien_the * cuong_do_dien
nang_luong = (cong_suat * t) / (3600 * 1000)
tien_dien = nang_luong * gia_dien
print(f"tiền điện là: {tien_dien:.2f} VNĐ")
