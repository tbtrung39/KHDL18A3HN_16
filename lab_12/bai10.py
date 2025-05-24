from datetime import datetime

try:
    date1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    date2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")

    delta = abs(d2 - d1)
    total_days = delta.days

    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30

    print(f"Khoảng cách: {years} năm, {months} tháng, {days} ngày")
except ValueError:
    print("Lỗi định dạng ngày.")
