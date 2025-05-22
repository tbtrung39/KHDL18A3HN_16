import csv
from libs.xu_ly_thong_tin_nhanvien import *
FILE_PATH='ds_nhanvien.csv'
def nhap_nhan_vien():
    danh_sach=[]
    n=int(input('nhap so nhan vien:'))
    for _ in range(n):
        ma_nv=input('ma nv:')
        ten_nv=input('ten nv:')
        chuc_vu=input('chuc vu:')
        he_so_luong=float(input('he so luong:'))
        luong=tinh_luong(he_so_luong)
        phu_cap=phu_cap_cv(chuc_vu)
        thuc_linh=luong+phu_cap
        danh_sach.append([ma_nv,ten_nv,chuc_vu,he_so_luong,luong,phu_cap,thuc_linh])
    return danh_sach
def ghi_file(danh_sach):
    with open(FILE_PATH,'w',newline='',encoding='utf-8')as f:
        writer=csv.writer(f)
        writer.writerow(['ma nv','ten nv','chuc vu','he so luong','luong','phu cap','thuc linh'])
        writer.writerows(danh_sach)
def doc_file():
    with open(FILE_PATH,newline='',encoding='utf-8')as f:
        reader = csv.reader(f)
        next(reader)
        return [row for row in reader]
def in_danh_sach(danh_sach):
    print('{:<10}{:<20}{:<10}{:<15}{:<15}{:<15}{:<15}'.format('ma nv','ten nv','chuc vu','he so luong','luong','phu cap','thuc linh'))
    for row in danh_sach:
        print('{:<10}{:<20}{:<10}{:<15}{:<15}{:<15}{:<15}'.format(*row))
def sap_xep_theo_thuc_linh(danh_sach):
    return sorted(danh_sach,key=lambda x: float(x[6]),reverse=True)
def menu():
    while True:
        print('1.nhap danh sach nhan vien')
        print('2.in danh sach nhan vien')
        print('3.sap xep theo thuc linh')
        print('4.thoat')
        chon=input('chon:')
        if chon=='1':
            ds=nhap_nhan_vien()
            ghi_file(ds)
        elif chon=='2':
            ds=doc_file()
            in_danh_sach(ds)
        elif chon=='3':
            ds=doc_file()
            ds_sorted=sap_xep_theo_thuc_linh(ds)
            in_danh_sach(ds_sorted)
        elif chon=='4':
            break
        else:
            print('chon khong hop le')
if __name__=='__main__':
    menu()
    