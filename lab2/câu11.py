# Hàm kiểm tra số ngày của tháng
def so_ngay_thang(thang, nam):
    # Danh sách số ngày của các tháng trong năm không nhuận
    ngay_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Trả về số ngày của tháng
    return ngay_thang[thang - 1]

# Hàm tính ngày tiếp theo
def ngay_tiep_theo(ngay, thang, nam):
    # Lấy số ngày của tháng hiện tại
    so_ngay = so_ngay_thang(thang, nam)
    
    # Nếu ngày hiện tại nhỏ hơn số ngày của tháng, tăng ngày lên 1
    if ngay < so_ngay:
        ngay += 1
    else:
        # Nếu ngày hiện tại là ngày cuối của tháng, reset ngày về 1 và tăng tháng lên 1
        ngay = 1
        thang += 1
        
        # Nếu tháng là 13 (tháng 12 + 1), chuyển sang tháng 1 của năm kế tiếp
        if thang > 12:
            thang = 1
            nam += 1
    
    return ngay, thang, nam

# Nhập vào ngày, tháng, năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tính ngày tiếp theo
ngay, thang, nam = ngay_tiep_theo(ngay, thang, nam)

# In kết quả
print(f"Ngày tiếp theo là: {ngay}/{thang}/{nam}")
