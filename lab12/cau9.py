from datetime import datetime

def main():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        ngay_nhap = datetime(nam, thang, ngay)
        so_tuan = ngay_nhap.isocalendar()[1] 
        print(f"Ngày {ngay_nhap.strftime('%d/%m/%Y')} thuộc tuần thứ {so_tuan} trong năm.")
    except ValueError:
        print(" Ngày không hợp lệ")
if __name__ == "__main__":
    main()
