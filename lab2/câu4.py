# Câu 10 : Một điểm cho thuê sân tập bóng đá theo công thức sau: Mỗi giờ trong 03 giờ đầu tiên tính 100000đ/giờ Mỗi giờ tiếp theo có đơn giá giảm 25% so với đơn giá trong 3 giờ đầu tiên.Ngoài ra nếu thời gian thuê sân từ 11 giờ đến 15 giờ thì được giảm giá 10%.Viết chương trình nhập vào giờ bắt đầu, giờ kết thúc và in ra số tiền khách thuê sân tậpphải trả, biết rằng 5 giờ giờ bắt đầu  giờ kết thúc  22 giờ
def tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc):
    # Đơn giá 3 giờ đầu tiên
    don_gia_3_gio_dau = 100000
    
    # Tính số giờ thuê
    so_gio_thue = gio_ket_thuc - gio_bat_dau
    
    # Kiểm tra nếu thời gian thuê từ 11 giờ đến 15 giờ có giảm giá 10%
    thoi_gian_giam_gia = 0
    if 11 <= gio_bat_dau < 15 or 11 <= gio_ket_thuc < 15:
        thoi_gian_giam_gia = 10  # Giảm giá 10%

    # Tính tiền cho 3 giờ đầu tiên
    tien_3_gio_dau = min(so_gio_thue, 3) * don_gia_3_gio_dau
    
    # Tính tiền cho các giờ tiếp theo
    tien_them = 0
    if so_gio_thue > 3:
        so_gio_tiep_theo = so_gio_thue - 3
        don_gia_tiep_theo = don_gia_3_gio_dau * 0.75  # Giảm giá 25% cho các giờ tiếp theo
        tien_them = so_gio_tiep_theo * don_gia_tiep_theo
    
    # Tổng tiền
    tong_tien = tien_3_gio_dau + tien_them
    
    # Áp dụng giảm giá 10% nếu trong khoảng thời gian từ 11h đến 15h
    if thoi_gian_giam_gia > 0:
        tong_tien *= 0.9
    
    return tong_tien

# Nhập vào giờ bắt đầu và giờ kết thúc
gio_bat_dau = int(input("Nhập giờ bắt đầu (từ 5 đến 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (từ 5 đến 22): "))

# Kiểm tra điều kiện nhập liệu
if gio_bat_dau < 5 or gio_bat_dau > 22 or gio_ket_thuc < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    print("Giờ bắt đầu và giờ kết thúc không hợp lệ. Vui lòng nhập lại trong khoảng từ 5 giờ đến 22 giờ.")
else:
    # Tính và in ra số tiền khách phải trả
    tien = tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc)
    print(f"Số tiền khách phải trả là: {tien:.0f} đồng.")
