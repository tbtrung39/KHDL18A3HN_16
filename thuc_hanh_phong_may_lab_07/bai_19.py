#Bài 19:
nhan_vien = {}

while True:
    print("\n--- MENU QUẢN LÝ NHÂN VIÊN ---")
    print("1. Tạo mới từ điển")
    print("2. Thêm nhân viên")
    print("3. Tìm kiếm nhân viên theo mã")
    print("4. Tăng lương cho nhân viên")
    print("5. Xóa nhân viên")
    print("6. Sắp xếp theo năm sinh")
    print("7. Thoát chương trình")
    
    chon = int(input("Chọn chức năng (1-7): "))
    
    if chon == 1:
        nhan_vien = {}
        print("Đã tạo mới từ điển nhân viên!")
    
    elif chon == 2:
        while True:
            ma_nv = input("Nhập mã nhân viên (4 ký tự): ").strip()
            if len(ma_nv) != 4:
                print("Mã phải đúng 4 ký tự!")
                continue
            if ma_nv in nhan_vien:
                print("Mã đã tồn tại! Vui lòng nhập lại.")
            else:
                break
                
        ho_ten = input("Nhập họ tên: ").strip()[:20]
        nam_sinh = int(input("Nhập năm sinh: "))
        luong = float(input("Nhập lương: "))
        
        nhan_vien[ma_nv] = {
            'ho_ten': ho_ten,
            'nam_sinh': nam_sinh,
            'luong': luong
        }
        print(f"Đã thêm nhân viên {ma_nv} thành công!")
    
    elif chon == 3:
        ma_nv = input("Nhập mã nhân viên cần tìm: ")
        if ma_nv in nhan_vien:
            print(f"\nThông tin nhân viên {ma_nv}:")
            print(f"Họ tên: {nhan_vien[ma_nv]['ho_ten']}")
            print(f"Năm sinh: {nhan_vien[ma_nv]['nam_sinh']}")
            print(f"Lương: {nhan_vien[ma_nv]['luong']:,.0f} VND")
        else:
            print("Không tìm thấy nhân viên!")
    
    elif chon == 4:
        ma_nv = input("Nhập mã nhân viên cần tăng lương: ")
        if ma_nv in nhan_vien:
            nhan_vien[ma_nv]['luong'] += 1000000
            print(f"Đã tăng lương cho {ma_nv}. Lương mới: {nhan_vien[ma_nv]['luong']:,.0f} VND")
        else:
            print("Không tìm thấy nhân viên!")
    
    elif chon == 5:
        ma_nv = input("Nhập mã nhân viên cần xóa: ")
        if ma_nv in nhan_vien:
            del nhan_vien[ma_nv]
            print(f"Đã xóa nhân viên {ma_nv}!")
        else:
            print("Không tìm thấy nhân viên!")
    
    elif chon == 6:
        if not nhan_vien:
            print("Danh sách nhân viên trống!")
        else:
            sorted_nv = sorted(nhan_vien.items(), key=lambda x: x[1]['nam_sinh'])
            print("\nDANH SÁCH THEO NĂM SINH")
            print("-" * 50)
            for ma_nv, thong_tin in sorted_nv:
                print(f"{ma_nv} | {thong_tin['ho_ten']:20} | {thong_tin['nam_sinh']} | {thong_tin['luong']:,.0f} VND")
    
    elif chon == 7:
        print("Cảm ơn đã sử dụng chương trình!")
        break
    
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn 1-7")