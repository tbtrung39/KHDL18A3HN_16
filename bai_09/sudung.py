import qlyhanghoa

while True:
    ma_hang = int(input("Nhap ma hang: "))
    if len(str(ma_hang)) == 4:
        break
    else:
        print('Nhap lai')
    ten_hang = input("Nhap ten hang: ")
    don_vi_tinh = input("Nhap don vi tinh: ")
    don_gia = int(input('Nhap don vi: '))
    so_luong = int(input('Nhap so luong: '))
    print('Thanh tien: ', qlyhanghoa.thanh_tien(don_gia, so_luong))
    print('Thue VAT:', sorted(qlyhanghoa.thue(don_gia, so_luong)))