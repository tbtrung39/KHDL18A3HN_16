thisinh = {}
n = int(input("Nhập số lượng thí sinh ban đầu: "))
for i in range(n):
    print(f"\nNhập thông tin thí sinh thứ {i+1}:")
    sbd = input("Số báo danh: ")
    hoten = input("Họ và tên: ")
    diem = float(input("Điểm thi: "))
    thisinh[sbd] = {"hoten": hoten, "diem": diem}
sbd_tra_cuu = input("\nNhập số báo danh cần tra cứu: ")
if sbd_tra_cuu in thisinh:
    print("\nThông tin thí sinh:")
    print("Họ và tên:", thisinh[sbd_tra_cuu]["hoten"])
    print("Điểm thi:", thisinh[sbd_tra_cuu]["diem"])
else:
    print("\nKhông tìm thấy thí sinh này. Mời nhập thêm thông tin.")
    hoten_moi = input("Họ và tên: ")
    diem_moi = float(input("Điểm thi: "))
    thisinh[sbd_tra_cuu] = {"hoten": hoten_moi, "diem": diem_moi}
    print("Đã thêm thí sinh mới vào danh sách.")
