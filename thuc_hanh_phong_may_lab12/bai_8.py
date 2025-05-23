from datetime import datetime, timedelta

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    d = datetime(nam, thang, ngay) - timedelta(days=1)
    print("Ngày trước đó là:", d.strftime("%d-%m-%Y"))
except ValueError:
    print("Lỗi: Ngày không hợp lệ.")
