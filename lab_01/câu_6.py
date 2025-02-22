def tinh_tien_dien(thoi_gian):
    hieu_dien_the = 220  # V
    cuong_do_dong_dien = 2.7  # A
    gia_tien_dien = 7000  # đ/kWh
    # Tính công suất (P = U * I)
    cong_suat = hieu_dien_the * cuong_do_dong_dien  # W
    # Tính năng lượng tiêu thụ (E = P * t)
    nang_luong_tieu_thu = (cong_suat * thoi_gian) / 3600000  # kWh
    # Tính tiền điện
    tien_dien = nang_luong_tieu_thu * gia_tien_dien
    return round(tien_dien, 2)
# Nhập thời gian sử dụng (giây)
thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
# Tính và hiển thị kết quả
so_tien = tinh_tien_dien(thoi_gian)
print(f"Số tiền điện phải trả: {so_tien} đ")