
thoi_gian = float(input('Nhập thời gian sử dụng bóng đèn (giây): '))

hieu_dien_the = 220 
cuong_do_dong_dien = 2.7 
gia_dien = 7000 

cong_suat = hieu_dien_the * cuong_do_dong_dien 

thoi_gian_gio = thoi_gian / 3600  

nang_luong_tieu_thu = (cong_suat * thoi_gian_gio) / 1000  # kWh

tien_dien = nang_luong_tieu_thu * gia_dien

print('Tiền điện phải trả là: %0.2f đ' % tien_dien)
