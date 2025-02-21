# Nhập các giá trị s tính bằng giây, m tính bằng phút, h tính bằng giờ, d tính bằng ngày
s = float(input('Nhập số giây: '))
m = float(input('Nhập số phút: '))
h = float(input('Nhập số giờ: '))
d = float(input('Nhập số ngày: '))

tong_giay = s + m*60 + h*3600 + d*86400

print('Tổng thời gian tính bằng giây là:', tong_giay)
