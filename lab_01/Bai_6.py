t = int(input("Nhập thời gian (giây) sử dụng bóng đèn: "))
hieu_dien_the = 220
cuong_do_dong_dien = 2.7
cong_suat = (hieu_dien_the * cuong_do_dong_dien)/100
dien_nang_tieu_thu = cong_suat * t
print(f"Sử dụng dóng đèn trong {t} giây phải trả {round(dien_nang_tieu_thu * 7000):_} đ/kwh")