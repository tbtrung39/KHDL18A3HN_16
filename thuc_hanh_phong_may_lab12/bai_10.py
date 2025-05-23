from datetime import datetime

try:
    d1 = input("Nhập ngày thứ nhất (dd/mm/yyyy): ")
    d2 = input("Nhập ngày thứ hai (dd/mm/yyyy): ")

    ngay1 = datetime.strptime(d1, "%d/%m/%Y")
    ngay2 = datetime.strptime(d2, "%d/%m/%Y")

    if ngay1 > ngay2:
        ngay1, ngay2 = ngay2, ngay1

    chenh_lech = ngay2 - ngay1
    tong_ngay = chenh_lech.days

    print(f"Hai ngày cách nhau {tong_ngay} ngày.")

except ValueError:
    print("Lỗi: Vui lòng nhập ngày theo định dạng dd/mm/yyyy!")