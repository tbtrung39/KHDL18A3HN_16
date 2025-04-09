sinh_vien_dict = {}

n = int(input("Nhập số lượng sinh viên: "))
for _ in range(n):
    while True:
        ma_sinh_vien = input("Nhập mã sinh viên (6 ký tự số): ")
        if len(ma_sinh_vien) == 6 and ma_sinh_vien.isdigit():
            break
        print(" Mã sinh viên không hợp lệ. Vui lòng nhập lại.")

    ten_sinh_vien = input("Nhập tên sinh viên: ")
    
    while True:
        try:
            diem_sinh_vien = float(input("Nhập điểm sinh viên (0-10): "))
            if diem_sinh_vien < 0:
                diem_sinh_vien = 0
            elif diem_sinh_vien > 10:
                diem_sinh_vien = 10
            break
        except ValueError:
            print(" Vui lòng nhập điểm là một số.")

    sinh_vien_dict[ma_sinh_vien] = (ten_sinh_vien, diem_sinh_vien)

# Sắp xếp sinh viên theo điểm giảm dần
sorted_sinh_vien = sorted(sinh_vien_dict, key=lambda ma_sv: sinh_vien_dict[ma_sv][1], reverse=True)

print(" Danh sách sinh viên theo điểm giảm dần:")
for ma_sv in sorted_sinh_vien:
    ten_sv, diem_sv = sinh_vien_dict[ma_sv]
    print(f" Mã: {ma_sv} | Tên: {ten_sv} | Điểm: {diem_sv}")
