# 1. Nhập danh sách các số tự nhiên cho đến khi nhập số 0
danh_sach = []
print("Nhập các số tự nhiên (nhập 0 để kết thúc):")
while True:
    so = int(input("Nhập số: "))
    if so == 0:
        break
    danh_sach.append(so)

print(f"\nDanh sách ban đầu: {danh_sach}")

# 2. Chuyển các số dương lên đầu danh sách
so_duong = [x for x in danh_sach if x > 0]  # Danh sách các số dương
so_khac = [x for x in danh_sach if x <= 0]  # Danh sách các số khác (âm và 0 nếu có)

danh_sach_moi = so_duong + so_khac  # Ghép lại danh sách với số dương lên đầu
print(f"\nDanh sách sau khi chuyển số dương lên đầu: {danh_sach_moi}")

# 3. Nhập số m và chèn vào danh sách
m = int(input("\nNhập số m cần chèn vào danh sách: "))

# Chèn vào đầu danh sách
danh_sach_moi.insert(0, m)

# Chèn vào cuối danh sách
danh_sach_moi.append(m)

# Chèn vào vị trí thứ 5 (nếu danh sách đủ dài)
if len(danh_sach_moi) >= 5:
    danh_sach_moi.insert(4, m)  # Chỉ số 4 là vị trí thứ 5

print(f"\nDanh sách sau khi chèn số {m}: {danh_sach_moi}")
