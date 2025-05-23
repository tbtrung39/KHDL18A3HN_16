try:
    ten_nguon = input("Nhập tên tập tin nguồn: ")
    ten_dich = input("Nhập tên tập tin đích: ")

    with open(ten_nguon, 'r', encoding='utf-8') as f_nguon:
        noi_dung = f_nguon.read()

    with open(ten_dich, 'w', encoding='utf-8') as f_dich:
        f_dich.write(noi_dung)

    print("Đã sao chép nội dung thành công.")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy tập tin nguồn.")
except OSError:
    print("Lỗi: Không thể mở tập tin.")
