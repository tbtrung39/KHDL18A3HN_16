# Hàm hiển thị thời gian dưới dạng "d ngày, h giờ, m phút, s giây"
def hien_thi_thoi_gian(d, h, m, s):
    print(f"{d} ngày, {h} giờ, {m} phút, {s} giây")
# Nhập dữ liệu từ người dùng
d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
# Hiển thị thời gian theo định dạng yêu cầu
hien_thi_thoi_gian(d, h, m, s)