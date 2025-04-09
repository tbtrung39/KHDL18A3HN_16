n = []
m = int(input("Nhập số phần tử cho danh sách n: "))

for i in range(-m, m):
    n.append(i)
print(n)

r = n
r.remove(max(n))
print(r)
print('Số dương lớn thứ 2 là:', max(r))
print('Vị trí sô dương lớn thứ 2 là:', r.index(max(r)))

so_luong_cac_so_duong = 0
tong_so_duong_lien_tiep = 0
for i in n:
    if i > 0:
        so_luong_cac_so_duong += 1
        tong_so_duong_lien_tiep += i
print("Số lương số dương liên tiếp là:", so_luong_cac_so_duong)
print("Số lương số dương liên tiếp có tổng lớn nhất là:", tong_so_duong_lien_tiep)