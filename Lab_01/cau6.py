# Bài 6: Một bóng đèn khi được sử dụng với hiệu điện thế 220 V, có cường độ dòng điện chạy qua bàn là 2,7 A. Viết chương trình nhập vào thời gian sử dụng bóng đèn (giây) tính toán được tiền điện phải trả với giá tiền điện là 7000 đ/kWh.

t = float(input('Nhập thời gian sử dụng bóng đèn: '))
u = 220  
i = 2.7 
gia_tien = 7000  
cong_suat = u * i 
nang_luong_tieu_thu_kwh = (cong_suat * t) / (1000 * 3600) 
tien_dien = nang_luong_tieu_thu_kwh * gia_tien
print(f'Tiền điện phải trả: {tien_dien:.2f} đ')
