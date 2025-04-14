# câu2
# Nhập số phần tử của danh sách
so_phan_tu = int(input("Nhập số phần tử của danh sách: "))

# Nhập danh sách các số tự nhiên
danh_sach = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(so_phan_tu)]

# 1. Tìm phần tử lớn thứ hai và vị trí của nó
gia_tri_khac_nhau = list(set(danh_sach))  # Loại bỏ các phần tử trùng nhau
if len(gia_tri_khac_nhau) < 2:
    print("Không tồn tại phần tử lớn thứ hai trong danh sách.")
else:
    gia_tri_khac_nhau.sort(reverse=True)  # Sắp xếp giảm dần
    phan_tu_lon_thu_hai = gia_tri_khac_nhau[1]  # Lấy phần tử lớn thứ hai
    vi_tri_lon_thu_hai = [i for i, x in enumerate(danh_sach) if x == phan_tu_lon_thu_hai]
    print(f"Phần tử lớn thứ hai: {phan_tu_lon_thu_hai}, Vị trí: {vi_tri_lon_thu_hai}")

# 2. Tính số lượng các số dương liên tiếp nhiều nhất
chuoi_dai_nhat = 0
chuoi_hien_tai = 0
for so in danh_sach:
    if so > 0:
        chuoi_hien_tai += 1
        if chuoi_hien_tai > chuoi_dai_nhat:
            chuoi_dai_nhat = chuoi_hien_tai
    else:
        chuoi_hien_tai = 0
print(f"Số lượng các số dương liên tiếp nhiều nhất: {chuoi_dai_nhat}")

# 3. Tính tổng các số dương liên tiếp có tổng lớn nhất
tong_max = 0
tong_hien_tai = 0
for so in danh_sach:
    if so > 0:
        tong_hien_tai += so
        if tong_hien_tai > tong_max:
            tong_max = tong_hien_tai
    else:
        tong_hien_tai = 0
print(f"Tổng các số dương liên tiếp lớn nhất: {tong_max}")