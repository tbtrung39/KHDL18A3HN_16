from datetime import datetime, timedelta
def main():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        ngay_hien_tai = datetime(nam, thang, ngay)
        ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)
        print("Ngày kế tiếp là:", ngay_ke_tiep.strftime("%d/%m/%Y"))
    except ValueError:
        print("Lỗi: Ngày không hợp lệ")
if __name__ == "__main__":
    main()
