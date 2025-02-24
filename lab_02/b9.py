
print("Nhập số kW và số tiền là:")
kw = int(input("Nhập số kW: "))

if 0 <= kw <= 100:
    don_gia = 2000
    print("Đơn giá: 2000 đồng/kW")
elif 101 <= kw <= 200:
    don_gia = 2500
    print("Đơn giá: 2500 đồng/kW")
elif 201 <= kw <= 300:
    don_gia = 3000
    print("Đơn giá: 3000 đồng/kW")
elif kw > 300:
    don_gia = 5000
    print("Đơn giá: 5000 đồng/kW")
else:
    don_gia = 0
    print("Không hợp lệ, xin vui lòng nhập lại.")

if don_gia > 0:
    so_tien = kw * don_gia
    print("Số tiền phải trả là:", so_tien, "đồng")
