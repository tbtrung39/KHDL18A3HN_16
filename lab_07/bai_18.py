so_bao_danh = int(input("Nhap so bao danh: "))
ho_ten = input("Nhap ho va ten: ")
diem_thi = float(input("Nhap diem thi: "))
thong_tin_sinh_vien = {}

while True:
    if str(so_bao_danh) == '' and ho_ten == '':
        print("Nhap lai.")
    else:
        if 0 <= diem_thi <= 10:
            thong_tin_sinh_vien.update({so_bao_danh: [ho_ten, diem_thi]})
            break
        else:
            print("Nhap lai")

if so_bao_danh in thong_tin_sinh_vien:
    thong_tin_sinh_vien[0] = so_bao_danh
    print("Da cap nhat")
else:
    thong_tin_sinh_vien[0] = so_bao_danh
    print("Da cap nhat lam moi")
print(thong_tin_sinh_vien)