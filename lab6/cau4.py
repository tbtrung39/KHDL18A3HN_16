import random

# 1. Nhập danh sách các số tự nhiên, dừng khi nhập số 0
danh_sach = []
print("Nhập các số tự nhiên (nhập 0 để kết thúc):")
while True:
    so = int(input("Nhập số: "))
    if so == 0:
        break
    danh_sach.append(so)

print(f"\nDanh sách ban đầu: {danh_sach}")

# 2. Chèn [1,2,3] vào đầu, cuối, vị trí thứ 5 nếu danh sách đủ dài
danh_sach[0:0] = [1, 2, 3]  # Chèn vào đầu
danh_sach.extend([1, 2, 3])  # Chèn vào cuối
if len(danh_sach) >= 5:
    danh_sach[4:4] = [1, 2, 3]  # Chèn vào vị trí thứ 5

print(f"\nDanh sách sau khi chèn [1,2,3]: {danh_sach}")

# 3. Xóa phần tử tại vị trí k (nhập từ bàn phím)
k = int(input("\nNhập vị trí k cần xóa (bắt đầu từ 0): "))
if 0 <= k < len(danh_sach):
    del danh_sach[k]
    print(f"Danh sách sau khi xóa phần tử tại vị trí {k}: {danh_sach}")
else:
    print("Vị trí k không hợp lệ!")

# 4. Sắp xếp danh sách theo thứ tự tăng dần, giảm dần
danh_sach_tang = sorted(danh_sach)
danh_sach_giam = sorted(danh_sach, reverse=True)

print(f"\nDanh sách sắp xếp tăng dần: {danh_sach_tang}")
print(f"Danh sách sắp xếp giảm dần: {danh_sach_giam}")

# 5. Tạo danh sách 1000 số tự nhiên ngẫu nhiên từ 1 đến 10000
list_A = [random.randint(1, 10000) for _ in range(1000)]
print(f"\nDanh sách A gồm 1000 số ngẫu nhiên: {list_A[:20]} ...")  # In 20 số đầu tiên