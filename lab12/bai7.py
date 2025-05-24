from datetime import datetime, timedelta

def ngay_ke_tiep():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        
        ngay_hien_tai = datetime(nam, thang, ngay)
        ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)
        print(f"Ngày kế tiếp là: {ngay_ke_tiep.strftime('%d-%m-%Y')}")
    
    except ValueError as e:
        print(e)

ngay_ke_tiep()