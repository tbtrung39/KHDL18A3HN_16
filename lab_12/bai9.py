from datetime import datetime

try:
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    dt = datetime(year, month, day)
    week_number = dt.isocalendar()[1]
    print(f"Tuần thứ: {week_number}")
except ValueError:
    print("Ngày không hợp lệ.")

