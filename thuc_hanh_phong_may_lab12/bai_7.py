from datetime import datetime, timedelta

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    d = datetime(nam, thang, ngay) + timedelta(days=1)
    print("Ngày kế tiếp: ", d.strftime('%d/%m/%Y'))
except ValueError:
    print("Lỗi: Vui lòng nhập ngày, tháng, năm hợp lệ!")