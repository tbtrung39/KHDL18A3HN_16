def so_ngay_trong_thang(thang, nam):
    # Kiểm tra tháng hợp lệ
    if thang < 1 or thang > 12:
        return "Tháng không hợp lệ. Vui lòng nhập tháng từ 1 đến 12."
    # Số ngày trong các tháng
    so_ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Kiểm tra năm nhuận
    if thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29 
        else:
            return 28  
    return so_ngay[thang - 1]
# Nhập tháng và năm từ người dùng
thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
# Gọi hàm và in kết quả
ngay = so_ngay_trong_thang(thang, nam)
print(f"Tháng {thang} năm {nam} có {ngay} ngày.")