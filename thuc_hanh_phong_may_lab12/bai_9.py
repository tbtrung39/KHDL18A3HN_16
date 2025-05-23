from datetime import datetime

thu = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    d = datetime(nam, thang, ngay)
    print("Ngày đó là:", thu[d.weekday()])
except ValueError:
    print("Lỗi: Ngày không hợp lệ.")
