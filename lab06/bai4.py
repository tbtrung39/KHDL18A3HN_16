danh_sach = []
while True:
    so = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
    if so == 0:
        break
    danh_sach.append(so)
chen = [1, 2, 3]
# Chèn vào đầu
danh_sach = chen + danh_sach
# Chèn vào cuối
danh_sach += chen
# Chèn vào vị trí thứ 5 (chỉ khi danh sách có ít nhất 5 phần tử)
if len(danh_sach) >= 5:
    danh_sach = danh_sach[:4] + chen + danh_sach[4:]
print("Danh sách sau khi chèn:", danh_sach)
# Xóa phần tử thứ k (k nhập từ bàn phím)
k = int(input("Nhập vị trí phần tử cần xóa (bắt đầu từ 1): ")) - 1
if 0 <= k < len(danh_sach):
    del danh_sach[k]
    print("Danh sách sau khi xóa phần tử thứ", k + 1, ":", danh_sach)
else:
    print("Vị trí không hợp lệ!")
# Sắp xếp danh sách tăng dần
danh_sach_tang = sorted(danh_sach)
print("Danh sách sắp xếp tăng dần:", danh_sach_tang)
# Sắp xếp danh sách giảm dần
danh_sach_giam = sorted(danh_sach, reverse=True)
print("Danh sách sắp xếp giảm dần:", danh_sach_giam)
