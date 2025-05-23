import My_QuanLySinhVien.quanlysinhvien as ql

def main():
    print('Nhap danh sach:')
    ds = ql.nhap_ds_sv()

    print('In danh sach:')
    ql.in_ds(ds)

    print('Luu danh sach:')
    ql.luu(ds)

    print('Danh sach duoc sap xep theo thu tu tang dan cua diem RL:')
    ql.sap_xep(ds)

    print('Sinh vien co diem TL cao nhat:')
    ql.tim_sv_dtl_max(ds)

if __name__ == '__main__':
    main()