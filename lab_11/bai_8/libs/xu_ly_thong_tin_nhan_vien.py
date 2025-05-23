import csv

def doc_file(file_path, n: list):
    with open(file= file_path, mode= 'r', encoding= 'utf-8') as open_file:
        csvreader = csv.reader(open_file)
        for i in csvreader:
            n.append(i)
    return n.sort(reverse= True)

def danh_sach_nhan_vien(nv: list):
    while True:
        try:
            ma_nv = int(input('Nhap ma nhan vien: '))
            ten_nv = input('Nhap ten nhan vien: ')
            chuc_vu = input('Nhap chuc vu nhan vien: ').upper()
            he_so_luong = int(input('Nhap he so luong nhan vien: '))
            luong = he_so_luong * 1_490_000
        except Exception:
            print('NHap lai.')
        else:
            phu_cap_chuc_vu = 0
            if chuc_vu == 'TP':
                phu_cap_chuc_vu = 1_000_000
            elif chuc_vu == 'PP':
                phu_cap_chuc_vu = 700_000
            elif chuc_vu == 'NV':
                phu_cap_chuc_vu = 300_000
            thuc_linh = luong + phu_cap_chuc_vu
            nv.append([ma_nv, ten_nv, chuc_vu, he_so_luong, luong, phu_cap_chuc_vu, thuc_linh])
            break

def luu_file(n: list):
    with open(file= 'ds_nhan_vien.csv', mode= 'w', encoding= 'utf-8') as save_file:
        csvwriter = csv.writer(save_file)
        for i in n:
            csvwriter.writerow(i)