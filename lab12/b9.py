from datetime import datetime

def tinh_tuan_trong_nam():
    try:
        d = int(input("Nhập ngày: "))
        m = int(input("Nhập tháng: "))
        y = int(input("Nhập năm: "))

        ngay = datetime(year=y, month=m, day=d)
        so_tuan = ngay.isocalendar()[1]  # Lấy số tuần ISO

        print(f"Ngày {ngay.strftime('%d-%m-%Y')} thuộc tuần thứ {so_tuan} trong năm.")
    except ValueError:
        print("Lỗi: Ngày không hợp lệ.")

tinh_tuan_trong_nam()