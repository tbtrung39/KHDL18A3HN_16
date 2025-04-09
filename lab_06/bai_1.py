a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
Tong = sum(a)
print("Tông các phần tử trong dnh sách a là:", Tong)

so_luong_cac_hang_duong = 0
tong_cac_so_hang_duong = 0
for i in a:
    if i > 0:
        so_luong_cac_hang_duong += 1
        tong_cac_so_hang_duong += i
print("Số lượng của các số hạng dương là:", so_luong_cac_hang_duong)
print("Tông các số hạng dương là:", tong_cac_so_hang_duong)

so_am_dau_tien = 0
for i in a[::-1]:
    if i < 0:
        so_am_dau_tien = i
print('Vị trí số âm đầu tiên là:', a.index(so_am_dau_tien))

so_duong_cuoi_cung = 0
for i in a:
    if i > 0:
        so_duong_cuoi_cung = i
print("Vị trí số dương cuối cùng là:", a.index(so_duong_cuoi_cung))

print("Số lớn nhất của danh sách là:", max(a))
print("Vị trí phần tử lớn nhất là:", a.index(max(a)))