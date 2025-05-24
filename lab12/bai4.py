def doc_va_ghi_tap_tin():
    ten_tap_tin_nhap = input("Nhập tên tập tin để đọc: ")
    ten_tap_tin_xuat = input("Nhập tên tập tin để ghi: ")
    
    try:
        with open(ten_tap_tin_nhap, 'r') as tap_tin_nhap:
            noi_dung = tap_tin_nhap.read()
        
        with open(ten_tap_tin_xuat, 'w') as tap_tin_xuat:
            tap_tin_xuat.write(noi_dung)
        
        print("Nội dung đã được ghi vào tập tin mới.")
    
    except IOError:
        print("Lỗi: Không thể mở tập tin. Vui lòng kiểm tra chế độ mở.")

doc_va_ghi_tap_tin()