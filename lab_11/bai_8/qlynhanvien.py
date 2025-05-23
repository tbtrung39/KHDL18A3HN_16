import libs.xu_ly_thong_tin_nhan_vien as xu_ly
import files

ds_nv = []
while True:
    var = 'Quan ly nhan vien'
    print(f'{var:_123}')
    print('Danh sach nhan vien: ')
    try:
        file = input('Nhap ten file: ')
    except:
        print('Nhap lai ten file')
    else:
        print('Doc file nhan vien: ')
        xu_ly.doc_file(file, ds_nv)
        print()
        print('Danh sach nhan vien: ')
        xu_ly.danh_sach_nhan_vien(ds_nv)
        print('Luu file.')
        xu_ly.luu_file(ds_nv)
        break