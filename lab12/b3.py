def doc_va_ghi_tap_tin():
    ten_tap_tin = input("Nhập tên tập tin cần đọc: ")

    try:
        with open(ten_tap_tin, 'r', encoding='utf-8') as f:
            noi_dung = f.read()

        with open("copy.dat", 'w', encoding='utf-8') as f_moi:
            f_moi.write(noi_dung)

        print("Đã sao chép nội dung sang file copy.dat.")

    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tập tin. Kết thúc chương trình.")

doc_va_ghi_tap_tin()
