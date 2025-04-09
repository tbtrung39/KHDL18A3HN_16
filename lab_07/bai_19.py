n = int(input("Nhap so luong nhan vien: "))
thong_tin_nhan_vien = {}

while len(thong_tin_nhan_vien) < n:
    ma_nhan_vien = int(input("Nhap ma nhan vien: "))
    ho_ten = input("Nhap ho ten nhan vien: ")
    nam_sinh = int(input("Nhap nam sinh nhan vien: "))
    luong = int(input("Nhap luong nhan vien: "))
    if len(str(ma_nhan_vien)) != 4 and len(ho_ten) != 20 and str(nam_sinh) == '' and str(luong) == '':
        print("Nhap lai.")
    else:
        for i in str(ma_nhan_vien):
            if i == '2':
                luong += 1_000_000
        thong_tin_nhan_vien.update({ma_nhan_vien: [ho_ten, nam_sinh, luong]})
        break

print(thong_tin_nhan_vien)

while True:
    tim_kiem = int(input("Nhap 1 de tim kiem nhan vien co ma so 1 hoac 0 de quen:"))
    if tim_kiem == 0:
        break
    elif tim_kiem != 1:
        print("Nhap lai")
    else:
        for i in str(thong_tin_nhan_vien[0]):
            if i == 1:
                print(thong_tin_nhan_vien[0])
                break
            else:
                print("Khong co ma nhan vien")
                break

for i in str(thong_tin_nhan_vien[0]):
    if i == '3':
        del thong_tin_nhan_vien[0]
        print("Da xoa nhan vien")

print(sorted(thong_tin_nhan_vien[1][1]))