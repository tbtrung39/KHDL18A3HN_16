from datetime import datetime, timedelta

def ngay_truoc_do():
    try:
        d = int(input("Nhập ngày: "))
        m = int(input("Nhập tháng: "))
        y = int(input("Nhập năm: "))

        ngay = datetime(year=y, month=m, day=d)
        ngay_truoc = ngay - timedelta(days=1)

        print("Ngày trước đó là:", ngay_truoc.strftime("%d-%m-%Y"))

    except ValueError:
        print("Lỗi: Ngày không hợp lệ.")

ngay_truoc_do()