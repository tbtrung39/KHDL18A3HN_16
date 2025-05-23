def ghi_tap_tin():
    ten_file = input("Nhập tên tập tin để ghi dữ liệu vào: ")
    du_lieu = input("Nhập nội dung muốn ghi vào tập tin: ")

    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            f.write(du_lieu)
        print("Ghi dữ liệu thành công vào", ten_file)

    except IOError:
        print("Lỗi: Không thể mở tập tin để ghi. Vui lòng kiểm tra quyền truy cập hoặc tên file.")

ghi_tap_tin()
