so_kw = int(input("Nhập số kWh điện tiêu thụ: "))
if so_kw >= 0:
    print("Số kWh không hợp lệ! Vui lòng nhập lại.")
if so_kw <= 100:
    don_gia = 2000
elif so_kw <= 200:
    don_gia = 2500
elif so_kw <= 300:
    don_gia = 3000
else:
    don_gia = 5000
tien_dien = so_kw * don_gia
print(f"Đơn giá: {don_gia:,} đồng/kWh")
print(f"Tiền điện phải trả: {tien_dien:,} đồng")
