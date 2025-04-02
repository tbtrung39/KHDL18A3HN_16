# Nhập số phần tử của danh sách
so_phan_tu = int(input("Nhập số phần tử của danh sách: "))

# Nhập danh sách các số tự nhiên
danh_sach = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(so_phan_tu)]

# 1. Tìm phần tử lớn thứ hai và vị trí của nó
def tim_phan_tu_lon_thu_hai(danh_sach):
    gia_tri_khac_nhau = list(set(danh_sach))  # Loại bỏ các phần tử trùng nhau
    if len(gia_tri_khac_nhau) < 2:
        return None, None  # Không có số lớn thứ hai nếu danh sách không đủ đa dạng
    gia_tri_khac_nhau.sort(reverse=True)  # Sắp xếp giảm dần
    lon_thu_hai = gia_tri_khac_nhau[1]  # Lấy phần tử lớn thứ hai
    vi_tri = [i for i, x in enumerate(danh_sach) if x == lon_thu_hai]
    return lon_thu_hai, vi_tri

phan_tu_lon_thu_hai, vi_tri_lon_thu_hai = tim_phan_tu_lon_thu_hai(danh_sach)
if phan_tu_lon_thu_hai is not None:
    print(f"Phần tử lớn thứ hai: {phan_tu_lon_thu_hai}, Vị trí: {vi_tri_lon_thu_hai}")
else:
    print("Không tồn tại phần tử lớn thứ hai trong danh sách.")

# 2. Tính số lượng các số dương liên tiếp nhiều nhất
def tim_so_duong_lien_tiep_nhieu_nhat(danh_sach):
    chuoi_dai_nhat = 0
    chuoi_hien_tai = 0
    for so in danh_sach:
        if so > 0:
            chuoi_hien_tai += 1
            chuoi_dai_nhat = max(chuoi_dai_nhat, chuoi_hien_tai)
        else:
            chuoi_hien_tai = 0
    return chuoi_dai_nhat

so_duong_lien_tiep_max = tim_so_duong_lien_tiep_nhieu_nhat(danh_sach)
print(f"Số lượng các số dương liên tiếp nhiều nhất: {so_duong_lien_tiep_max}")

# 3. Tính tổng các số dương liên tiếp có tổng lớn nhất
def tim_tong_so_duong_lien_tiep_lon_nhat(danh_sach):
    tong_max = 0
    tong_hien_tai = 0
    for so in danh_sach:
        if so > 0:
            tong_hien_tai += so
            tong_max = max(tong_max, tong_hien_tai)
        else:
            tong_hien_tai = 0
    return tong_max

tong_so_duong_max = tim_tong_so_duong_lien_tiep_lon_nhat(danh_sach)
print(f"Tổng các số dương liên tiếp lớn nhất: {tong_so_duong_max}")