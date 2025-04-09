ma_sinh_vien = int(input("Nhap ma sinh vien: "))
ten_sinh_vien = input("Nhap ten sinh vien: ")
diem_so = int(input("Nhap diem sinh vien: "))
thong_tin_sinh_vien = {}

diem = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

while len(thong_tin_sinh_vien) < 10:
    if len(str(ma_sinh_vien)) != 6 or str(ma_sinh_vien) == '' or str(ma_sinh_vien) == ' ':
        print("Nhap lai.")
    else:
        if diem_so not in diem:
            print("Nhap lai.")
        else:
            thong_tin_sinh_vien.update({ma_sinh_vien: [ten_sinh_vien, diem_so]})
            break

print(sorted(thong_tin_sinh_vien[1][1], reverse=True))