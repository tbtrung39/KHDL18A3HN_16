try:
    ten_tap_tin = input("Nhập tên tập tin: ")
    with open(ten_tap_tin, 'r', encoding='utf-8') as f:
        noi_dung = f.read()
    with open("copy.dat", 'w', encoding='utf-8') as f_copy:
        f_copy.write(noi_dung)
    print("Đã sao chép nội dung sang copy.dat")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy tập tin.")
