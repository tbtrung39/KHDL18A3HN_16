def ten_thu(trang_thai):
    # Danh sách tên các ngày trong tuần
    danh_sach_thu = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return danh_sach_thu.get(trang_thai)
def nhap_thu():
    while True:
        try:
            thu = int(input("Nhập thứ trong tuần (1-7): "))
            if 1 <= thu <= 7:
                return thu
            else:
                print("Giá trị không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên từ 1 đến 7.")
# Nhập thứ từ người dùng
thu_nhap = nhap_thu()
# Lấy tên thứ tương ứng
ten_thu_nhap = ten_thu(thu_nhap)
# Xuất kết quả ra màn hình
print(f"Thứ đã nhập là: {ten_thu_nhap}.")