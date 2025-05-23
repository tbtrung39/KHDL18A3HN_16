from datetime import datetime, timedelta
def main():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        ngay_hien_tai = datetime(nam, thang, ngay)
        ngay_truoc = ngay_hien_tai - timedelta(days=1)
        print("Ngày trước đó là:", ngay_truoc.strftime("%d/%m/%Y"))
    except ValueError:
        print("Ngày không hợp lệ")
if __name__ == "__main__":
    main()
