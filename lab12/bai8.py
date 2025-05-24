from datetime import datetime, timedelta

from datetime import datetime, timedelta

def ngay_truoc_do():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        
        ngay_hien_tai = datetime(nam, thang, ngay)
        ngay_truoc = ngay_hien_tai - timedelta(days=1)
        print(f"Ngày trước là: {ngay_truoc.strftime('%d-%m-%Y')}")
    
    except ValueError as e:
        print(e)

ngay_truoc_do()