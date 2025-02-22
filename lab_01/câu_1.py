# Nhập thông tin sinh viên
def nhap_thong_tin():
    ma_sv = input("Nhập mã số sinh viên: ")
    ho_ten = input("Nhập họ và tên: ")
    que_quan = input("Nhập quê quán: ")
    nam_sinh = input("Nhập năm sinh: ")
    # Nhập điểm trung bình của từng năm học
    diem_trung_binh = []
    so_nam_hoc = int(input("Nhập số năm học: "))
    for i in range(so_nam_hoc):
        diem = float(input(f"Nhập điểm trung bình năm {i+1}: "))
        diem_trung_binh.append(diem)
    return {
        "Mã SV": ma_sv,
        "Họ Tên": ho_ten,
        "Quê Quán": que_quan,
        "Năm Sinh": nam_sinh,
        "Điểm Trung Bình": diem_trung_binh
    }
# Xuất thông tin sinh viên
def xuat_thong_tin(sinh_vien):
    print("\nThông tin sinh viên:")
    print(f"Mã SV: {sinh_vien['Mã SV']}")
    print(f"Họ Tên: {sinh_vien['Họ Tên']}")
    print(f"Quê Quán: {sinh_vien['Quê Quán']}")
    print(f"Năm Sinh: {sinh_vien['Năm Sinh']}")
    print("Điểm Trung Bình Các Năm:", ", ".join(map(str, sinh_vien['Điểm Trung Bình'])))
# Chạy chương trình
sinh_vien = nhap_thong_tin()
xuat_thong_tin(sinh_vien)