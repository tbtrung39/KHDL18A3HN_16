def doc_du_lieu(file_vao):
    with open(file_vao, 'r') as f:
        dong = f.readlines()
    so_khach = int(dong[0].strip())
    hanh_ly = [list(map(float, dong[i].split())) for i in range(1, so_khach + 1)]
    return hanh_ly
def xu_ly_du_lieu(du_lieu):
    danh_sach_tong = []
    huy_chuyen = []
    for i, hanh_ly in enumerate(du_lieu):
        tong = sum(hanh_ly)
        danh_sach_tong.append(tong)
        if tong > 23:
            huy_chuyen.append(i + 1)
            print(f"Hành khách thứ {i+1} bị hủy chuyến: tổng trọng lượng > 23kg ({tong:.2f} kg)")
        elif len(hanh_ly) > 5:
            huy_chuyen.append(i + 1)
            print(f"Hành khách thứ {i+1} bị hủy chuyến: có quá 5 kiện hành lý ({len(hanh_ly)} kiện)")
    return danh_sach_tong, huy_chuyen
def ghi_file_weight(tong_cac_kg, ten_file='lab11/cau9/WEIGHT.OUT'):
    with open(ten_file, 'w') as f:
        for so in tong_cac_kg:
            f.write(f"{so:.2f}\n")
def ghi_file_huy_chuyen(ds_huy, ten_file='lab11/cau9/CANCELED.OUT'):
    with open(ten_file, 'w') as f:
        for stt in ds_huy:
            f.write(f"{stt}\n")
# ------------------- CHƯƠNG TRÌNH CHÍNH -------------------
du_lieu = doc_du_lieu("lab11/cau9/PASSENGERS.IN")
tong_kg, huy_chuyen = xu_ly_du_lieu(du_lieu)
ghi_file_weight(tong_kg)
ghi_file_huy_chuyen(huy_chuyen)

