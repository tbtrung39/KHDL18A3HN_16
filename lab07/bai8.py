A = {1, 3.14, "hello" , 42, "dung", 2.718, "trung", 0, -5, 1.0,}
dem_so_nguyen = 0
dem_so_thuc = 0
dem_chuoi = 0
for x in A:
    if type(x) == int:
        dem_so_nguyen += 1
    elif type(x) == float:
        dem_so_thuc += 1
    elif type(x) == str:
        dem_chuoi += 1
print("Tập hợp A:", A)
print("Số phần tử là số nguyên :", dem_so_nguyen)
print("Số phần tử là số thực :", dem_so_thuc)
print("Số phần tử là chuỗi :", dem_chuoi)
