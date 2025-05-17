import os

def doc_du_lieu_passenger():
    """Đọc dữ liệu từ file PASSENGER.IN"""
    with open('PASSENGER.IN', 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    so_khach = int(lines[0])
    trong_luong_toi_da = float(lines[1])
    danh_sach_khach = []
    
    for i in range(2, len(lines)):
        cac_do = lines[i].split()
        trong_luong = [float(x) for x in cac_do]
        danh_sach_khach.append({
            'so_thu_tu': len(danh_sach_khach) + 1,
            'trong_luong': trong_luong,
            'so_luong_do': len(trong_luong),
            'tong_trong_luong': sum(trong_luong)
        })
    
    return so_khach, trong_luong_toi_da, danh_sach_khach

def xu_ly_va_ghi_file():
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs('files', exist_ok=True)
    
    # Đọc dữ liệu từ file
    so_khach, trong_luong_toi_da, danh_sach_khach = doc_du_lieu_passenger()
    
    # 1. Ghi tổng trọng lượng vào WEIGHT.OUT
    with open('files/WEIGHT.OUT', 'w') as f:
        for khach in danh_sach_khach:
            f.write(f"{khach['tong_trong_luong']:.2f}\n")
    
    # 2. Xác định khách bị hủy chuyến
    khach_huy_chuyen = []
    for khach in danh_sach_khach:
        if khach['tong_trong_luong'] > 23 or khach['so_luong_do'] > 5:
            khach_huy_chuyen.append(khach)
    
    # 3. Ghi thông tin hủy chuyến vào CANCELED.OUT
    with open('files/CANCELED.OUT', 'w') as f:
        for khach in khach_huy_chuyen:
            ly_do = []
            if khach['tong_trong_luong'] > 23:
                ly_do.append(f"vượt quá 23kg ({khach['tong_trong_luong']:.2f}kg)")
            if khach['so_luong_do'] > 5:
                ly_do.append(f"vượt quá 5 đồ ({khach['so_luong_do']} đồ)")
            f.write(f"{khach['so_thu_tu']} -> Khách bị hủy do: {' và '.join(ly_do)}\n")
    
    # 4. Hiển thị thông báo
    print("\nKẾT QUẢ XỬ LÝ")
    print("="*50)
    print(f"Đã xử lý xong {so_khach} hành khách")
    
    if khach_huy_chuyen:
        print("\nCÁC HÀNH KHÁCH BỊ HỦY CHUYẾN:")
        for khach in khach_huy_chuyen:
            ly_do = []
            if khach['tong_trong_luong'] > 23:
                ly_do.append(f"Quá trọng lượng ({khach['tong_trong_luong']:.2f}kg)")
            if khach['so_luong_do'] > 5:
                ly_do.append(f"Quá số lượng đồ ({khach['so_luong_do']} đồ)")
            print(f"- Khách số {khach['so_thu_tu']}: {'; '.join(ly_do)}")
    else:
        print("\nKhông có hành khách nào bị hủy chuyến")
    
    print("\nKết quả đã được lưu vào:")
    print("- WEIGHT.OUT: Tổng trọng lượng từng khách")
    print("- CANCELED.OUT: Danh sách khách bị hủy chuyến")

if __name__ == "__main__":
    xu_ly_va_ghi_file()