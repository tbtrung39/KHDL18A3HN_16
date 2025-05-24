from datetime import datetime

def tinh_ngay_thuoc_tuan_trong_nam():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        
        ngay_hien_tai = datetime(nam, thang, ngay)
        tuan_so = ngay_hien_tai.isocalendar()[1]
        print(f"Ngày {ngay_hien_tai.strftime('%d-%m-%Y')} thuộc tuần thứ {tuan_so} trong năm.")
    
    except ValueError as e:
        print(e)

tinh_ngay_thuoc_tuan_trong_nam()