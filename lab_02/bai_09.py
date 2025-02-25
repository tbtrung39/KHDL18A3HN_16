kw = float(input("nhập số kw tiêu thụ:"))
if 0 <= kw <= 100:
    don_gia= kw * 2000
elif 101 <= kw <= 200:
    don_gia = 100 * 2000 + (kw - 100) * 2500
elif 201 <= kw <= 300:
    don_gia = 100 * 2000 + 100 * 2500 +(kw - 200) * 3000
else:
    don_gia = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 3500
print(f"tiền điện phải trả là {don_gia} đồng")



