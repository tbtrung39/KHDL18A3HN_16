n = int(input("Nhập số phần tử của danh sách: "))
danh_sach = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(so)
# 1. Tìm phần tử lớn thứ hai và vị trí của nó
lon_nhat = max(danh_sach)
lon_thu_hai = None
for so in danh_sach:
    if so != lon_nhat:
        if lon_thu_hai is None or so > lon_thu_hai:
            lon_thu_hai = so
vi_tri = []
for i in range(n):
    if danh_sach[i] == lon_thu_hai:
        vi_tri.append(i)
print("Phần tử lớn thứ hai:", lon_thu_hai)
print("Vị trí của phần tử lớn thứ hai:", vi_tri)
#2 Tính số lượng các số dương liên tiếp nhiều nhất
dem_hien_tai = 0
dem_max = 0
for so in danh_sach:
    if so > 0:
        dem_hien_tai += 1
        if dem_hien_tai > dem_max:
            dem_max = dem_hien_tai
    else:
        dem_hien_tai = 0
print("Số lượng số dương liên tiếp nhiều nhất:", dem_max)
#3 Tính số lượng các số dương liên tiếp có tổng lớn nhất
tong_max = 0
tong_hien_tai = 0
dem_hien_tai = 0
dem_max = 0
for so in danh_sach:
    if so > 0:
        tong_hien_tai += so
        dem_hien_tai += 1
        if tong_hien_tai > tong_max:
            tong_max = tong_hien_tai
            dem_max = dem_hien_tai
    else:
        tong_hien_tai = 0
        dem_hien_tai = 0
print("Số lượng các số dương liên tiếp có tổng lớn nhất:", dem_max)
