# Nhập giá trị từ người dùng
d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
# Tính tổng số giây
tong_so_day = d * 86400 + h * 3600 + m * 60 + s
print("Tổng số giây:", tong_so_day)