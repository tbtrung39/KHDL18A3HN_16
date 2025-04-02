# Danh sách đã cho
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# Tính tổng các phần tử của danh sách
tong = sum(a)
print(f"Tổng các phần tử của danh sách: {tong}")

# Đếm số lượng số hạng dương và tổng của các số hạng dương
so_duong = [x for x in a if x > 0]
tong_duong = sum(so_duong)
print(f"Số lượng các số hạng dương: {len(so_duong)}")
print(f"Tổng các số hạng dương: {tong_duong}")

# Tìm vị trí của phần tử âm đầu tiên trong danh sách
vi_tri_am_dau = next((i for i, x in enumerate(a) if x < 0), None)
if vi_tri_am_dau is not None:
    print(f"Vị trí phần tử âm đầu tiên: {vi_tri_am_dau}")
else:
    print("Không có phần tử âm nào trong danh sách.")

# Tìm vị trí của phần tử âm cuối cùng trong danh sách
vi_tri_am_cuoi = next((i for i in range(len(a)-1, -1, -1) if a[i] < 0), None)
if vi_tri_am_cuoi is not None:
    print(f"Vị trí phần tử âm cuối cùng: {vi_tri_am_cuoi}")
else:
    print("Không có phần tử âm nào trong danh sách.")

# Tìm phần tử lớn nhất của danh sách và vị trí của nó
max_value = max(a)
vi_tri_max = [i for i, x in enumerate(a) if x == max_value]
print(f"Phần tử lớn nhất trong danh sách: {max_value}")
print(f"Vị trí của phần tử lớn nhất: {vi_tri_max}")
