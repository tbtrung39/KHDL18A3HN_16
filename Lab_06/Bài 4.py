list1 = []
while True:
    n = int(input("Nhập số: "))
    if n== 0:
        break
    list1.append(n)
print(" Danh sách ban đầu: ", list1)
list1[0:0] = [1, 2, 3]
list1.extend([1, 2, 3])
if len(list1) >= 5:
    list1[5:5] = [1, 2, 3]
print(" Danh sách sau khi chèn [1,2,3]: ", list1)
k = int(input(" Nhập vị trí cần xóa: "))
if 0 <= k < len(list1):
    list1.remove(list1[k])
    print(f"Danh sách sau khi xóa phần tử thứ {k}: {list1}")
else:
    print(" Không hợp lệ")
danh_sach_tang = sorted(list1)
danh_sach_giam = sorted(list1, reverse=True)
print(" Danh sách sắp xếp tăng dần: ", danh_sach_tang)
print(" Danh sách sắp xếp giảm dần: ", danh_sach_giam)