def main():
    try:
        ten_tap_tin = input("Nhập tên tập tin: ")
        with open(ten_tap_tin, 'r', encoding='utf-8') as file_goc:
            noi_dung = file_goc.read()
        with open('lab12/cau3/copy.dat', 'w', encoding='utf-8') as file_copy:
            file_copy.write(noi_dung)
        print("Đã sao chép nội dung")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tập tin '{ten_tap_tin}'")
if __name__ == "__main__":
    main()
