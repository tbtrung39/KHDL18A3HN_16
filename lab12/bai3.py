def doc_va_ghi_tap_tin():
    filename = input("Nhập tên tập tin: ")
    try:
        with open(filename, 'r') as file:
            noi_dung = file.read()
        
        with open('copy.dat', 'w') as copy_file:
            copy_file.write(noi_dung)
        
        print("Nội dung đã được sao chép vào copy.dat.")
    
    except FileNotFoundError:
        print("Lỗi: Tập tin không tồn tại.")

doc_va_ghi_tap_tin()