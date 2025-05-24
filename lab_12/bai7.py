from datetime import datetime

try:
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    d = datetime(year, month, day)
    print("Ngày hợp lệ:", d.strftime("%d-%m-%Y"))
except ValueError:
    print("Ngày không hợp lệ.")
