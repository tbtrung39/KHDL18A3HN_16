# Nhập số KW điện tiêu thụ từ người dùng
so_kw = float(input("Nhập số KW điện tiêu thụ: "))
# Tính toán
if so_kw <= 100:
    don_gia = 2000
elif so_kw <= 200:
    don_gia = 2500
elif so_kw <= 300:
    don_gia = 3000
else:
    don_gia = 5000

tien_dien = so_kw * don_gia
# Tính và in tiền điện
print("Tiền điện phải trả là:",tien_dien,"đồng.")