from datetime import datetime

def tinh_khoang_cach():
    try:
        ngay1_str = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
        ngay2_str = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
        
        ngay1 = datetime.strptime(ngay1_str, "%d-%m-%Y")
        ngay2 = datetime.strptime(ngay2_str, "%d-%m-%Y")
        
        delta = abs(ngay2 - ngay1)
        nam = delta.days // 365
        thang = (delta.days % 365) // 30
        ngay = (delta.days % 365) % 30
        
        print(f"Hai ngày cách nhau {nam} năm, {thang} tháng, và {ngay} ngày.")
    
    except ValueError as e:
        print(e)

tinh_khoang_cach()