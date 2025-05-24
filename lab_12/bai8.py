import calendar
from datetime import datetime

try:
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    dt = datetime(year, month, day)
    print("Ngày đó là:", dt.strftime("%A"))
except ValueError:
    print("Ngày không hợp lệ.")

