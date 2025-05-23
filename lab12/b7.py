from datetime import datetime, timedelta

def ngay_ke_tiep():
    try:
        d = int(input("Nhập ngày: "))
        m = int(input("Nhập tháng: "))
        y = int(input("Nhập năm: "))

        ngay = datetime(year=y, month=m, day=d)
        ngay_sau = ngay + timedelta(days=1)

        print("Ngày kế tiếp là:", ngay_sau.strftime("%d-%m-%Y"))

    except ValueError:
        print("Lỗi: Ngày không hợp lệ.")

ngay_ke_tiep()