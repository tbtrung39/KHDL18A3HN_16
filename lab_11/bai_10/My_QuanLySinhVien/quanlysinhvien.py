import csv

def nhap_sv():
    ma_sv = int(input('Nhap ma sinh vien: '))
    ho_ten = input('Nhap ho ten sinh vien: ')
    diem_tb = float(input('Nhap diem trung binh cua sinh vien: '))
    diem_rl = float(input('Nhap diem ren luyen cua sinh vien: '))
    diem_tl = (diem_tb + diem_rl)/2
    return {'Ma sinh vien: ': ma_sv, 'Ho ten sinh vien: ': ho_ten,
            'Diem trung binh: ': diem_tb, 'Diem ren luyen: ': diem_rl, 'Diem tich luy: ': diem_tl}

def nhap_ds_sv():
    ds = []
    n = int(input('Nhap so luong sinh vien: '))
    for i in range(n):
        print(f'Nhap thong tin sinh vien {i + 1}:')
        sv = nhap_sv()
        ds.append(sv)
    return ds

def in_ds(ds):
    print({'Ma sinh vien:': 10, 'Ho ten sinh vien: ': 25,
           'DIem trung binh: ': 10, 'Diem ren luyen: ': 10, 'Diem tich luy: ': 10})
    for i in ds:
        print(f'{i['ma_sv'] :10}, {i['ho_ten']: 25},'
              f'{i['diem_tb']: 10.2f}, {i['diem_rl']: 10.2f}, {i['diem_tl']: 10.2f}')

def luu(ds):
    with open(file= 'ds_sinhvien.csv', mode= 'w', newline= '', encoding= 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Ma sinh vien', 'Ho ten sinh vien', 'Diem trung binh', 'Diem ren luyen', 'Diem tich luy'])
        for i in ds:
            writer.writerow([i['ma_sv'], i['ho_ten'], i['diem_tb'], i['diem_rl'], i['diem_tl']])

def sap_xep(ds):
    return sorted(ds, key= lambda i: i['diem_rl'])

def tim_sv_dtl_max(ds):
    d_max = max(i['diem_tl'] for i in ds)
    return [i for i in ds if i['diem_tl'] == d_max]